TASK

Create a simple Python web application with a single REST endpoint that takes two date arguments and retrieves the list of near-Earth space objects approaching Earth in that time interval. Output the list of the objects, sorted by their closest approach distance, containing  the object name, size estimate, time and distance of the closest encounter.

The data should come from the API of NeoWs service at https://api.nasa.gov/ (free registration required). The application should also properly handle data ranges larger than the 7-day limit imposed by the Nasa API.

Be prepared to explain how the application works, including the data formats and network protocols used.

REST API endpoint:
* GET /objects
* query parameter 'start_date' in format YYYY-MM-DD
* query parameter 'end_date' in format YYYY-MM-DD
* returns JSON array of JSON objects

Implementation:
--------------------
* Python 3, web framework of your choice (FastAPI, Flask, Django, etc)
* Include a Dockerfile

--------------------------------------------------------------------------------------------------------------------------------------------

SOLUTION

Q: How Do I run the app?
A: run $ docker-compose build && docker-compose up -d 


Q: How Do I know if the application is working at all or How do I check endpoints and validations?
A: By accessing the endpoints on OpenAPI generated pages on localhost.


### My Solution TODO: REMOVE THIS SECTION ONCE git pushed
1. Register on nasa site
2. Find out which data they are talking about think how to extract it.
3. Create a FastAPI application with just one file
4. docker-compose and dockerfile . docker-compose should have 2 services -> redis and the fastapi framework itself.
5. Create requirements.txt 
6. Create a seperate module which will connect to nasa api and extract the data.
7. Create a seperate modules namely models to represent the data type with PyDantic.
8. Find out and write tests inside of tests/ folder 
9. Test it out and if it works add a picture on this README and a video loaded to git repo.
