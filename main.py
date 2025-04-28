from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler



def preprocess_data(df):
    preprocessor = joblib.load("preprocessor.pkl")
    return preprocessor.transform(df)



app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    data = {'message': 'Hello from the API!'}
    return jsonify(data)


@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        # Parse JSON data from the incoming request
        data = request.get_json()

        # Load data into variables
        pclass = data.get('pclass')
        sex = data.get('sex')
        sibsp = data.get('sibsp')
        parch = data.get('parch')
        fare = data.get('fare')
        embarked = data.get('embarked')

        newdata_df = pd.DataFrame([pclass, sex, sibsp, parch, fare, embarked]).T
        newdata_preprocessed = preprocess_data(newdata_df)
        print(newdata_df)
        
        with open("model.pickle", 'rb') as file:
            prediction_model = pickle.load(file)

        result = prediction_model.predict(newdata_preprocessed)

        response = {
            "prediction":result
        }

        # Use these variables for processing or prediction
        # For now, just return them in the response for testing
        # response = {
        #     "pclass": pclass,
        #     "sex": sex,
        #     "sibsp": sibsp,
        #     "parch": parch,
        #     "embarked": embarked,
        #     "fare": fare
        # }

        print(response)

        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)