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
