from flask import Flask, jsonify, render_template, request
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

app = Flask(__name__, template_folder=os.path.join(PROJECT_DIR, 'frontend'))

REGRESSION_MODEL_PATH = os.path.join(PROJECT_DIR, 'Swiggy_FoodDeliveryTimePrediction_Model.pkl')
CLASSIFICATION_MODEL_PATH = os.path.join(PROJECT_DIR, 'Price_Classification.pkl')

regression_model = joblib.load(REGRESSION_MODEL_PATH)
classification_model = joblib.load(CLASSIFICATION_MODEL_PATH)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


def get_request_data(required_fields):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = request.form.to_dict()

    missing_fields = [field for field in required_fields if field not in data or str(data[field]).strip() == '']
    if missing_fields:
        raise ValueError('Missing required fields: ' + ', '.join(missing_fields))
    return data


@app.route('/predict', methods=['POST'])
def predict_delivery_time():
    try:
        data = get_request_data([
            'Area', 'City', 'Restaurant', 'Price', 'Avg ratings',
            'Total ratings', 'Address'
        ])
        single_data = pd.DataFrame({
            'Area': [data['Area']],
            'City': [data['City']],
            'Restaurant': [data['Restaurant']],
            'Price': [float(data['Price'])],
            'Avg ratings': [float(data['Avg ratings'])],
            'Total ratings': [int(data['Total ratings'])],
            'Address': [data['Address']],
        })

        pred = regression_model.predict(single_data)[0]
        return jsonify({
            'predicted_delivery_time': round(float(pred), 2),
            'prediction': round(float(pred), 2),
        })
    except (TypeError, ValueError, KeyError) as error:
        return jsonify({'error': str(error)}), 400
    except Exception:
        return jsonify({'error': 'The delivery-time model could not make a prediction.'}), 500


@app.route('/predict-price-segment', methods=['POST'])
def predict_price_segment():
    try:
        data = get_request_data([
            'Area', 'City', 'Restaurant', 'Avg ratings',
            'Total ratings', 'Food type', 'Address'
        ])
        single_data = pd.DataFrame({
            'Area': [data['Area']],
            'City': [data['City']],
            'Restaurant': [data['Restaurant']],
            'Avg ratings': [float(data['Avg ratings'])],
            'Total ratings': [int(data['Total ratings'])],
            'Food type': [data['Food type']],
            'Address': [data['Address']],
        })

        pred = classification_model.predict(single_data)[0]
        return jsonify({
            'price_segment': str(pred),
            'prediction': str(pred),
        })
    except (TypeError, ValueError, KeyError) as error:
        return jsonify({'error': str(error)}), 400
    except Exception:
        return jsonify({'error': 'The price-classification model could not make a prediction.'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)