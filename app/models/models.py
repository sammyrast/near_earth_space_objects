"""Represents data."""
from pydantic import BaseModel


class SpaceObjects(BaseModel):
    links: dict
    id: str 
    neo_reference_id: str
    name: str
    nasa_jpl_url: str 
    absolute_magnitude_h: float
    estimated_diameter: dict
    is_potentially_hazardous_asteriod: bool
    close_approach_data: dict
    is_sentry_object: bool
