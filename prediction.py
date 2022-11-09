import pandas as pd
import joblib
import json

def predict(data):
   
    # Dictionary to interpret results
    dictionary = {0: {'Road Condition':'Poor', 'Vehicle Config':'986P.X'},
                  1: {'Road Condition':'Average', 'Vehicle Config':'456A.4'}, 
                  2: {'Road Condition':'Great', 'Vehicle Config':'166Y.2'}
                 }
    jsondata = json.loads("[" + json.dumps(data) + "]")
    model = joblib.load("road-model.joblib")
    # Run prediction
    prediction = model.predict(jsondata)
    result = dictionary[prediction[0]]

    return {'prediction': result}

#predict([0.36, 0.20, 9.79, 0.009, -0.13, -0.02, 0.14])
