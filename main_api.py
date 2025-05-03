# main_api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper_module import scrape_vinted_api
from pydantic import BaseModel
from typing import Optional

class SearchParams(BaseModel):
    item_type: str
    search_query: str
    price_to: Optional[float] = None
    size: Optional[str] = None
    cond: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    uploaded_since: Optional[str] = None
    max_items: int = 10

app = FastAPI()

# Enable CORS for all origins (so Flutter can call it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/search")
async def search(params: SearchParams):
    return await scrape_vinted_api(params.dict())
