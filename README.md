# 📊 FastAPI Market Analyzer

A modern FastAPI microservice that analyzes Indian market sectors in real-time, collects fresh news, uses an LLM (OpenAI or Gemini) for AI insights, and generates a clean **markdown report** — all secured with token auth and rate limiting.

---

## ✅ Features

- **One simple GET endpoint**: `/analyze/{sector}`
- Allowed sectors: `pharmaceuticals`, `technology`, `agriculture`
- Uses [NewsData.io](https://newsdata.io) for live news scraping
- Uses [OpenAI GPT](https://platform.openai.com) or [Gemini](https://ai.google.dev/)
- Generates `.md` reports
- Token-based auth (`Bearer SECRET_TOKEN`)
- Per-IP rate limiting
- No database — in-memory only

---

## ✅ Setup

1️⃣ Clone & create virtual environment:

```bash
git clone https://github.com/yourusername/fastapi_market_analyzer.git
cd fastapi_market_analyzer
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```
