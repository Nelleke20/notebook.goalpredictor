from imp import reload
from joblib import load
import pandas as pd
import requests
# from flask import Flask, request, jsonify   #jsonify data  is json dump for flask app with correct content-type hearders
import numpy as np
from fastapi import FastAPI
import uvicorn


#####
# The data sent from the client side to the API is called a request body. The data sent from API to the client is called a response body. 
# To define our request body we’ll use BaseModel ,in pydantic module, and define the format of the data we’ll send to the API. To define our request body, we’ll create a class that inherits BaseModel and define the features as the attributes of that class along with their type hints. What pydantic does is that it defines these type hints during runtime and generates an error when data is invalid. So let’s create our request_body class:-
####

###
# uvicorn fast_app:app --reload
###

#### SWAGGER
# http://127.0.0.1:8000/docs
###

from pydantic import BaseModel
from typing import List


app = FastAPI()

modelBagging = load("best_model_svc.joblib")

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to nelleke-machinelearning-api!'}

class RequestBody(BaseModel):
    features: List[List[float]]

@app.post('/predict')
def predict(data: RequestBody):
    data_selection = data.features
    prediction = modelBagging.predict(data_selection)[0]
    return {'prediction' : prediction}
