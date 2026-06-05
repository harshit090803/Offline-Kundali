from fastapi import FastAPI
from app.api.cities import router as city_router
from app.api.chart import router as chart_router
app = FastAPI(title="AstroAI Engine", version="0.1.0")
app.include_router(city_router)
app.include_router(chart_router)
@app.get("/")
def home():
    return {"message": "AstroAI Running"}