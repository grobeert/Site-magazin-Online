from flask import Blueprint, request, jsonify
from app.model.sensors import fetch_iot_data, set_iot_data, reset_iot_data
 
# Cream Blueprint-ul pentru /api/iot
iot_api = Blueprint('iot_api', __name__)
 
 
@iot_api.route('/api/iot', methods=['GET'])
def get_iot():
    """Returnează datele curente ale senzorilor în format JSON."""
    return jsonify(fetch_iot_data())
 
 
@iot_api.route('/api/iot', methods=['POST'])
def post_iot():
    """Actualizează parțial sau total datele senzorilor."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON invalid sau lipsă"}), 400
    set_iot_data(data)
    return jsonify(fetch_iot_data())
 
 
@iot_api.route('/api/iot', methods=['DELETE'])
def delete_iot():
    """Resetează toți sensorii la 0."""
    reset_iot_data()
    return jsonify(fetch_iot_data())