"""main api entry point."""
from functools import lru_cache

from fastapi import FastAPI
from retry import retry
import httpx

from services.nasa_apod  import NasaNeo
from models.models import SpaceObjects


app = FastAPI()

@retry(httpx.ReadTimeout, tries=3, delay=2)    
@lru_cache(maxsize=128)
@app.get("/space_objects/{start_date}&{end_date}")
async def get_space_objects(start_date, end_date):
    space_objects: SpaceObjects = await NasaNeo(start_date=start_date, end_date=end_date).near_space_objects()
    
    return space_objects


@app.get("/ping")
def health_check_pong():
    return {"ping": "pong!"}