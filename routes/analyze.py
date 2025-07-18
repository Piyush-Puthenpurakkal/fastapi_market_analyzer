from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import PlainTextResponse
from fastapi.security import HTTPAuthorizationCredentials
import asyncio

from services.rate_limiter import limiter
from services.collector import fetch_sector_news
from services.analyzer import analyze_with_gpt
from utils.markdown_generator import generate_report
from utils.security import verify_token
from utils.sector_enum import SectorEnum

router = APIRouter()

async def _analyze_logic(sector: SectorEnum) -> str:
    print(f"🔍 Starting analysis for: {sector}")

    news_data = await fetch_sector_news(sector.value)
    if not news_data:
        raise HTTPException(status_code=404, detail="No news data found.")

    analysis = await analyze_with_gpt(news_data)
    return generate_report(sector.value, news_data, analysis)

@router.get("/{sector}", response_class=PlainTextResponse, summary="Analyze market sector")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: SectorEnum,
    credentials: HTTPAuthorizationCredentials = Depends(verify_token)
):
    try:
        return await asyncio.wait_for(_analyze_logic(sector), timeout=30)  # ✅ overall route timeout
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request timed out.")
