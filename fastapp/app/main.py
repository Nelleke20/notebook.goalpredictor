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
    return {"message": "demo-model"}


class RequestData(BaseModel):
    features: List[List[float]]


# defining prediction endpoint
@app.post("/predict")
def predict(data: RequestData):
    data_selection = data.features
    prediction = model.predict(data_selection)[0]
    return prediction


if __name__ == "__main__":
    # uvicorn.run(app, host="localhost", port=8000)
    uvicorn.run(app)
