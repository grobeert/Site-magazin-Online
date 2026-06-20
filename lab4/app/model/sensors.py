"""
Data model for IoT sensors.
"""
import json
import os

DATA_FILE = "sensors_data.json"

iot_data = {
    "ext_temp": 0,
    "int_temp": 0,
    "ext_hum": 0,
    "int_hum": 0,
    "rain": 0,
}


def load_iot_data():
    """Încarcă datele din fișierul JSON dacă există."""
    global iot_data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            iot_data.update(json.load(f))


def save_iot_data():
    """Salvează datele curente în fișierul JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(iot_data, f, indent=2)


def fetch_iot_data():
    return iot_data


def set_iot_data(data):
    for key in data:
        if key in iot_data:
            iot_data[key] = data[key]
    save_iot_data()


def reset_iot_data():
    for key in iot_data:
        iot_data[key] = 0
    save_iot_data()


# Încarcă datele la pornirea serverului
load_iot_data()