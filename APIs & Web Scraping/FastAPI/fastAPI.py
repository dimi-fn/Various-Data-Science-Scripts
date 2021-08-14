# install fastapi: python -m pip install fastapi
# install uvicorn for running the webserver: pip install uvicorn

import fastapi
from fastapi import FastAPI, Path
from typing import Optional #for displaying optional query parameters
from pydantic import BaseModel
from starlette.background import BackgroundTask # create request body with Post method



# create instance of the FastAPI object
app = FastAPI()

cars = {
    1: {
        "brand" : "mercedes",
        "model" : "mclaren",
        "make_year" : "2015"
    },

    2: {
        "brand" : "mercedes",
        "model" : "CClass",
        "make_year" : "2010"
    },

    3: {
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

# to activate the web server, run via terminal: uvicorn fastAPI:app --reload


'''Path Parameters'''
@app.get("/get-car/{car_id}")
# if Path is "None" then give a description
# number should be greater (gt) than -1 and less than 3001
def get_car(car_id: int = Path(None, description= "Type below the correct ID of the car you want to view", gt=-1, lt=3001)):
    return cars[car_id]

# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/1 will give the values of the car with key==1
# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/10 will give Error 500 "Internal Server Error" because no such value exists

# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/-1 will give Error 422 "Unprocessable Entity" because we ask for numbers greater than lt=-1
# URL/<path parameter>/<value> --> e.g.: http://127.0.0.1:8000/get-car/3001 will give Error 422 "Unprocessable Entity" because we ask for numbers less than lt=3001

'''Query Parameter'''
@app.get("/get-by-model")
def get_car(model: Optional[str] = None): #so that the query parameter "model" is optional and not required in the doc
    for car_id in cars:
        if cars[car_id]["model"] == model:
            return cars[car_id]

    # else
    return {"Data": "Not found"}

# e.g. URL/get-by-model?model=BMW    


'''Combine Path and Query Parameters'''
@app.get("/get-by-many-data")
def get_car(*, car_id:int, brand: Optional [str]=None, model: Optional[str]=None): 
    '''
    "*" -> so that the order of optional/non-optional parameters does not matter inside the function
    - car_id -> required parameter
    - brand -> optional parameter
    - model -> optional parameter
    '''
    return cars[car_id]

'''Request Body via BaseModel - Post Method'''
class Car(BaseModel):
    brand: str
    model: str
    make_year: int

# create Path with Post method
@app.post("/create-car/{car_id}")
def create_car(car_id : int, car : Car ):
    if car_id in cars:
        return {"Error": "Car with id {} already exists!".format(car_id)}

    cars[car_id] = car
    return cars[car_id]

'''Put Method: update something that already exists'''
class UpdateCar(BaseModel):
    brand: Optional[str] = None
    model: str = None
    make_year: int = None



@app.put("/update-car/{car_id}")
def update_car(car_id:int, car:UpdateCar):
    if car_id not in cars:
        return {"Error":"This car id cannot be updated because it does not exist!"}

    #if car.brand

    #else
    cars[car_id] = car
    return cars[car_id]