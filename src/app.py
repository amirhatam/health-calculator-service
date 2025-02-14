from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue sur l'API Health Calculator!"}), 200


@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        result = calculate_bmi(height, weight)
        return jsonify({'bmi': round(result, 2)}), 200
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender'].lower()
        
        if gender not in ['male', 'female']:
            raise ValueError("Invalid gender. Use 'male' or 'female'")
            
        result = calculate_bmr(height, weight, age, gender)
        return jsonify({'bmr': round(result, 2)}), 200
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)