import httpx
from app.config import GEMINI_API_KEY

async def analyze_with_gemini(sector: str, data: str) -> str:
    prompt = f"""
Analyze the following data and generate a Markdown report.

Sector: {sector}

Data:
{data}

Include:
- Market Overview
- Key Trends
- Trade Opportunities
- Risks
- Short-term Outlook
"""

    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.post(url, json=payload)

    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
