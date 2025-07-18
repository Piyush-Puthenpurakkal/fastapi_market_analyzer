def generate_report(sector: str, news_data: str, analysis: str) -> str:
    return f"""# 📊 Market Analysis Report – {sector.title()}

## 📰 Recent Sector News

{news_data}

---

## 🤖 AI Analysis & Trade Opportunities

{analysis}
"""
