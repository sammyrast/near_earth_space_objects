"""Represents data."""
from pydantic import BaseModel

# Interesting fields from assignment are the following:
# the object name, 
# size estimate, 
# time and distance of the closest encounter

# Input data:
#  links -> dictionary and holds the key "name" 
#  estimated_diameter -> dictionary and we need only the "kilometeres" key
#  close_approach_data -> "close_approach_date_full" key and "miss_distance"->"kilometers" key

# # {'links': {'self': 'http://api.nasa.gov/neo/rest/v1/neo/3611402?api_key=5g619Mo83GAVBpmJrvyj5pg95RT7hzT6nZeMFpCa'},
#  'id': '3611402',
#  'neo_reference_id': '3611402',
#  'name': '(2012 TR231)',
#  'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3611402',
#  'absolute_magnitude_h': 23.9,
#  'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.04411182,
#    'estimated_diameter_max': 0.0986370281},
#   'meters': {'estimated_diameter_min': 44.1118199997,
#    'estimated_diameter_max': 98.6370281305},
#   'miles': {'estimated_diameter_min': 0.0274098057,
#    'estimated_diameter_max': 0.0612901888},
#   'feet': {'estimated_diameter_min': 144.7238235278,
#    'estimated_diameter_max': 323.6123073718}},
#  'is_potentially_hazardous_asteroid': False,
#  'close_approach_data': [{'close_approach_date': '2022-10-15',
#    'close_approach_date_full': '2022-Oct-15 01:04',
#    'epoch_date_close_approach': 1665795840000,
#    'relative_velocity': {'kilometers_per_second': '16.7224576722',
#     'kilometers_per_hour': '60200.8476200208',
#     'miles_per_hour': '37406.4655670068'},
#    'miss_distance': {'astronomical': '0.0812045325',
#     'lunar': '31.5885631425',
#     'kilometers': '12148025.096345775',
#     'miles': '7548432.769390695'},
#    'orbiting_body': 'Earth'}],
#  'is_sentry_object': False}

#! todo ideal data structure is below
#
                    # near_earth_objects = {'name': data_extract[i][0]['name'], 
                    #                     'estimated_diameter':f"{data_extract[i][0]['estimated_diameter']['kilometers']}km",
                    #                     'close_approach_date':data_extract[i][0]['close_approach_data'][0]['close_approach_date_full'],
                    #                      'miss_distance': f"{data_extract[i][0]['close_approach_data'][0]['miss_distance']['kilometers']}km"}

class SpaceObjects(BaseModel):
    name: str  # can be extracted directly from the list value as a key , not action is needed here
    estimated_diameter_km: str # this is a dictionary which has kilometers and then estimated_diamter_min - estimated_diameter_max 
    close_approach_date: str # this is a dictionary and the key we need is close_approach_date_full 
    miss_distance_km: str  # this is a dictionary with kilometers key which the value is given as a string

