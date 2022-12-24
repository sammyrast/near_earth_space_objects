"""
Make connections to Nasa REST web service, extract data , make data ready for consumption.

Neo - Feed
Retrieve a list of Asteroids based on their closest approach date to Earth. GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY

Query Parameters
Parameter	Type	Default	Description
start_date	YYYY-MM-DD	none	Starting date for asteroid search
end_date	YYYY-MM-DD	7 days after start_date	Ending date for asteroid search
api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage

Example query
https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

"""
from os import environ as env
import json 
import logging 
import asyncio 
from operator import itemgetter

import httpx 
from dotenv import load_dotenv
from retry import retry
import pandas as pd


load_dotenv()

# Create logger 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class NasaNeo:
    """
    Gets with a date range the json objects from Nasa's api feed.
    """
    def __init__(self, start_date, end_date ) -> None:
        self.api_key = env['NASA_API_KEY']
        self.start_date = start_date
        self.end_date = end_date
        logger.info(f"Starting Instance of {__class__.__name__}")

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.start_date!r}, {self.end_date!r})' 

    async def near_space_objects(self):
        """
        given start and end date, gets the near earth space objects from NASA api.
        """
        async with httpx.AsyncClient(verify=False) as client:
            logger.info(f"{__class__.__name__}: getting the resources from NASA api...")
            try:
                resp = await client.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={self.start_date}&end_date={self.end_date}&api_key={self.api_key}")
            
            # Output the list of the objects, sorted by their closest approach distance, 
            # containing  the object name, size estimate, time and distance of the closest encounter.
                response = resp.json()
          
                list_of_near_earth_object = response['near_earth_objects'][self.start_date] + response['near_earth_objects'][self.end_date]

                return sorted(list_of_near_earth_object, key=lambda d: d['close_approach_data'][0]['miss_distance']['kilometers'])
            except httpx.ReadTimeout:
                logger.warning("looks like we finished our time of trying to reach the NASA API. Let's try again...")    

