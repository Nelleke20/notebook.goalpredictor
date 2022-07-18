from joblib import load
import pandas as pd
import requests
from flask import Flask, request, jsonify   #jsonify data  is json dump for flask app with correct content-type hearders
import numpy as np
from flask import render_template


app = Flask(__name__)

# Load the model
model = load("best_model.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data-test', methods=['GET'])
def data_test():
    data = {"input-data": "Hello World"}
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    features = request.form["features"]
    integer_features = []
    for item in features:
        try:
            item_integer = int(item)
            integer_features.append(item_integer)
        except ValueError:
            pass
    prediction = model.predict([integer_features])
    if prediction == 0:
        result = 'NO GOAL! relax, no goal will be scored, you have time to take a pee'
    if prediction == 1:
        result = "GOAL! or soon to be. Pay attention, it's goal scoring time the next minute."
    return render_template('index.html', prediction_text=f'{result}')


# @app.route('/predict', methods=['POST'])
# def create_prediction_bag():
#     data = request.get_json()
#     prediction = np.array2string(model.predict(data))
#     return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)