# TASK

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

# SOLUTION

Q: How Do I run the app?
A: run $ docker-compose build && docker-compose up -d 

Q: Run testing?
A: $ docker-compose exec app python -m pytest .

Q: How Do I know if the application is working at all or How do I check endpoints and validations?
A: By accessing the endpoints on OpenAPI generated pages on localhost. Besides there's a health check command on docker-compose..

Q: I would like to see how it all work briefly?
A: Please check out the video associated with the running of the app.

### My Solution
1. Register on nasa site
2. Find out which data we are dealing with and think how to extract it.
3. Create a FastAPI application with just one file.
4. docker-compose and dockerfile . docker-compose should have 2 services -> redis and the fastapi framework itself( atlast I used lru_cache for simplicty)
5. Create requirements.txt 
6. Create a seperate module which will connect to nasa api and extract the data.
7. Create a seperate modules namely models to represent the data type with PyDantic.
8. Write tests inside of tests/ folder - use PyTest
9. Test it out and if it works add a video loaded to git repo for more clarity.

### TODOs & Improvement Ideas
A. Expand on unit testing.
B. Maybe add redis for robust caching.
C. Most importantly I am not sure how I extracted the data from the nasa api (If I did it correctly or not , this might need further investigations)...

### Corrections 
1. App isn't able to handle intervals larger than 7 days (this was mentioned in the task description). Server responds with 500 Internal Server Error in such cases.
-> Possible solution : 1. check if the interval is larger than 7 days , if yes make request first to the range 6 days interval and then add the remaining interval . For example if we have 9 days interval . first I will check for 6 days data and then make another request for 3 days data. 
-> Possible solution: 2. maybe update the x-RATE if possible , check github 

2. Result only contains near-Earth objects from 2 days -- start_date and end_date, but the days inbetween are missing. For example if I ask for objects from 2022-12-12 to 2022-12-15, the result only contains asteroids for these 2 dates, but not for dates 2022-12-13 and 2022-12-14.
-> **Possible solution: Iterate through the interval or check docs/forums how it really works again. CORRECTION: I was not considering the dates between the ranges , now all dates in the range are covered.**

3. Sorting based on the distance doesn't work.
-> **Possible solution: After filtering the relevant data based on #4 try to check the sorting of the data based on the distance.CORRECTION: Now data is sorted by distance.**

4. There is no filtering out of the irrelevant data. This might not be clear from the task description (I'm sorry if that's the case), but we're interested only in a few attributes -- the object name, size estimate, time and distance of the closest encounter. Other attributes can be ignored and not returned by the endpoint.
-> **Possible solution: Make use of the pydantic class and read from dictionary data to filter , check it works.CORRECTION: only relevant data is extracted now.**

5. An Http client you're using ('httpx' library) has a default timeout and if this timeout exceeds, the app just logs a warning message, but the endpoint returns 'null' as response.
-> **Possible solution: check the default timeout for httpx and update this and also test it out. Updated the default timeout to None.**