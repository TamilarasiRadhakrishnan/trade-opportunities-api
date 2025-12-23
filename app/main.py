from fastapi import FastAPI, Depends, HTTPException
from slowapi.middleware import SlowAPIMiddleware

from app.rate_limiter import limiter
from app.security import verify_token
from app.services.search_service import fetch_market_news
from app.services.ai_service import analyze_with_gemini
from app.services.report_service import generate_markdown

app = FastAPI(
    title="Trade Opportunities API",
    description="Market analysis for Indian sectors",
    version="1.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    sector: str,
    user=Depends(verify_token)
):
    try:
        market_data = await fetch_market_news(sector)
        analysis = await analyze_with_gemini(sector, market_data)
        report = generate_markdown(sector, analysis)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
