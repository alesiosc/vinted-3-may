# main_api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper_module import scrape_vinted_api

app = FastAPI()

# —————— CORS Middleware ——————
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # for dev: allow all origins
    allow_methods=["*"],      # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],      # allow any headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/search")
async def search(params: dict):
    return await scrape_vinted_api(params)
