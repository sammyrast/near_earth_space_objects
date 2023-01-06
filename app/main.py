"""main api entry point."""
from typing import List

from fastapi import FastAPI

from services.nasa_apod  import NasaNeo
from models.models import SpaceObjects


app = FastAPI()


@app.get("/space_objects/{start_date}&{end_date}")
async def get_space_objects(start_date, end_date):
    space_objects: List[SpaceObjects] = await NasaNeo(start_date=start_date, end_date=end_date).near_space_objects()
    return space_objects


@app.get("/ping")
def health_check_pong():
    return {"ping": "pong!"}