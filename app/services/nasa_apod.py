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
import logging 
from typing import List
from datetime  import datetime

import httpx 
from dotenv import load_dotenv
from cachetools import cached, TTLCache

from models import models


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

    @cached(cache=TTLCache(maxsize=2, ttl=900))
    async def near_space_objects(self):
        """
        given start and end date, gets the near earth space objects from NASA api.
        """
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            logger.info(f"{__class__.__name__}: getting the resources from NASA api...")
            api_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={self.start_date}&end_date={self.end_date}&api_key={self.api_key}"
            final_list = []
            try: 
                self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
                self.end_date = datetime.strptime(self.end_date, "%Y-%m-%d")
                date_difference = self.end_date - self.start_date

                if date_difference <= 7:
                    # TODO call function which will get space objects and process them
                    resp = await client.get(api_url)
                
                # Output the list of the objects, sorted by their closest approach distance, 
                # containing  the object name, size estimate, time and distance of the closest encounter.
                    response = resp.json()

                    data_extract = response['near_earth_objects']        
                    list_of_date_keys = [i for i in data_extract.keys()]   

                    near_earth_objects: List[near_earth_objects] = []
                    for i in list_of_date_keys:
                        near_earth_objects.append({'name': data_extract[i][0]['name'], 
                                            'estimated_diameter_km':f"{data_extract[i][0]['estimated_diameter']['kilometers']}",
                                            'close_approach_date':data_extract[i][0]['close_approach_data'][0]['close_approach_date_full'],
                                            'miss_distance_km': f"{data_extract[i][0]['close_approach_data'][0]['miss_distance']['kilometers']}"} )
                    
                    near_earth_objects_list = [i for i in near_earth_objects]
                    sorted_space_objects = sorted(near_earth_objects_list, key=lambda data:data['miss_distance_km'])

                    space_objects_list = [models.SpaceObjects(**i) for i in sorted_space_objects ]

                    return space_objects_list
                elif date_difference > 7:                    
                    self.end_date = self.start_date + 7




            except httpx.ReadTimeout:
                logger.warning("looks like we finished our time of trying to reach the NASA API. Let's try again...")    



    