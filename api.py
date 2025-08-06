from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import pickle

app = Flask(__name__)

# Load trained model and scaler
model = tf.keras.models.load_model("genomic_model.h5")

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    genomic_data = np.array(data['input'])
    scaled_input = scaler.transform(genomic_data)
    variation_results = model.predict(scaled_input)
    return jsonify({'variations': variation_results.tolist()})

if __name__ == '__main__':
    app.run(debug=True)