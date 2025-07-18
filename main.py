from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pathlib import Path
from slowapi.middleware import SlowAPIMiddleware
from services.rate_limiter import limiter

from routes.analyze import router as analyze_router

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

app = FastAPI(
    title="📊 FastAPI Market Analyzer",
    description="Analyzes Indian market data for sectors and generates markdown trade insights.",
    version="1.0.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(analyze_router, prefix="/analyze", tags=["Market Analysis"])

@app.get("/", tags=["Root"])
def read_root():
    return {"msg": "✅ FastAPI Market Analyzer is running."}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal server error: {exc}"}
    )
