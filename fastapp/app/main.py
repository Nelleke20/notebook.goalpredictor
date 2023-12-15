from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

# create app
app = FastAPI()

# import a model
model = load("best_model_svc.joblib")


# Defining path operation for root endpoint
@app.get("/")
def main():
    return {"message": "Welcome to nelleke-machinelearning-api!"}


class RequestData(BaseModel):
    features: List[List[float]]


# defining prediction endpoint
@app.post("/predict")
def predict(data: RequestData):
    data_selection = data.features
    prediction = model.predict(data_selection)[0]
    return prediction


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


# #####################################################################EXTRA INFO##################################################################################
# FastApi is a framework, univicorn is the server where we run our API
# The data sent from the client side to the API is called a request body. The data sent from API to the client is called a response body.
# To define our request body we’ll use BaseModel ,in pydantic module, and define the format of the data we’ll send to the API.
# To define our request body, we’ll create a class that inherits BaseModel and define the features as the attributes of that class along with their type hints.
# What pydantic does is that it defines these type hints during runtime and generates an error when data is invalid.
# uvicorn fast_app:app --reload
# # http://127.0.0.1:8000/docs
######################################################################EXTRA INFO##################################################################################
