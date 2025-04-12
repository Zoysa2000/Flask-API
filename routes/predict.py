from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os

predict_route = Blueprint('predict_route', __name__)

# Load model from model folder
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'log_model.pkl')
log_model = joblib.load(model_path)

@predict_route.route('/', methods=['POST'])  # just root of the blueprint
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = log_model.predict(features)
    return jsonify({'prediction': prediction.tolist()})