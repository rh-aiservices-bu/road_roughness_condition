import pandas as pd
import joblib
import json

def predict(data):
   
    # Dictionary to interpret results
    dictionary = {0: 'Bad Road',1:'Regular Road', 2: 'Good Road'}

    jsondata = json.loads("[" + json.dumps(data) + "]")
    model = joblib.load("road-model.joblib")
    # Run prediction
    prediction = model.predict(jsondata)
    result = dictionary[prediction[0]]

    return {'prediction': result}

predict([0.3,0.2, 9.8, 0.009, -0.13, -0.01, 0.14])