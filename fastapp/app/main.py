from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn


class RequestData(BaseModel):
    features: List[List[float]]


# create app
app = FastAPI()

# import the model
model = load("best_model_svc.joblib")


# home
@app.get("/")
def main():
    return {"message": "demo-model"}


# defining prediction endpoint
@app.post("/predict")
def predict(data: RequestData):
    data_selection = data.features
    prediction = model.predict(data_selection)[0]
    return prediction


if __name__ == "__main__":
    uvicorn.run(app)
