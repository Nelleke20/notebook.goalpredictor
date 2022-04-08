from joblib import load
import pandas as pd
import requests
from flask import Flask, request, jsonify   #jsonify data  is json dump for flask app with correct content-type hearders
import numpy as np

app = Flask(__name__)

# Load the model
modelBagging = load("best_model_svc.joblib")
modelSVC = load("best_model.joblib")

@app.route('/', methods=['GET'])
def helloworld():
    data = {"data": "Hello World"}
    return jsonify(data)

@app.route('/api/predictBAGGING', methods=['POST'])
def create_prediction_bag():
    data = request.get_json()
    prediction = np.array2string(modelBagging.predict(data))
    return jsonify(prediction)

@app.route('/api/predictSVC', methods=['POST'])
def create_prediction_svc():
    data = request.get_json()
    prediction = np.array2string(modelSVC.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':
    model = load("best_model.joblib")  
    app.run(host='0.0.0.0', port=5000)