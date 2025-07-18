from openai import OpenAI
import traceback
import os

async def analyze_with_gpt(news_data: str) -> str:
    # ✅ Create client here so it picks up .env properly
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("🛑 OpenAI API key missing.")
        return "❌ OpenAI API key missing."

    client = OpenAI(api_key=api_key)  # ✅ pass the key explicitly

    try:
        prompt = (
            "Analyze the following Indian market news and highlight "
            "key investment insights:\n\n" + news_data
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful market analyst."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:        
        print(f"🛑 OpenAI API call failed: {e}")
        traceback.print_exc()
        return f"❌ OpenAI API error: {e}"
