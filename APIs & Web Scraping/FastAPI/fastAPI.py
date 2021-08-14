# install fastapi: python -m pip install fastapi
# install uvicorn for running the webserver: pip install uvicorn

import fastapi
from fastapi import FastAPI, Path

# create instance of the FastAPI object
app = FastAPI()

cars = {
    1: {
        "brand" : "mercedes",
        "model" : "mclaren",
        "make_year" : "2015"
    },

    2: {
        "brand" : "BMW",
        "model" : "i4",
        "make_year" : "2014"
    } 
}

# create endpoint instances of the communication channel 
'''
* GET: get an information
* POST: create something new
* PUT: update something that already exists
* DELETE: delete something
'''

# @ create API which will trigger data from the fastAPI instance
@app.get("/")
def index():
    # JSON
    return {"name": "First Data"}

# run via terminal: uvicorn fastAPI:app --reload

@app.get("/get-car/{car_id}")
# if Path is none then give a description
def get_car(car_id: int = Path(None, description= "Type below the correct ID of the car you want to view")):
    return cars[car_id]

# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/1 will give the values of the car with key==1
# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/10 will give "Internal Server Error" because no such value exists