import os
import httpx

async def fetch_sector_news(sector: str) -> str:
    NEWS_API_KEY = os.getenv("NEWSDATA_API_KEY")  # ✅ Load only when called
    if not NEWS_API_KEY:
        print("🛑 NEWS_API_KEY is missing.")
        return ""

    try:
        url = "https://newsdata.io/api/1/news"
        params = {
            "apikey": NEWS_API_KEY,
            "q": sector,
            "country": "in",
            "language": "en"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10)

        print("📡 NewsData API status:", response.status_code)
        print("🔍 Final URL:", response.url)

        if response.status_code != 200:
            print("🛑 NewsData Error Response:", response.text)
            return ""

        data = response.json()
        articles = data.get("results", [])
        if not articles:
            print("🛑 No articles found.")
            return ""

        news_summary = "\n\n".join(
            f"- {article['title']}: {article.get('description', '')}"
            for article in articles if article.get("title")
        )

        return news_summary[:4000]

    except Exception as e:
        print(f"🛑 NewsData API failed: {e}")
        return ""
