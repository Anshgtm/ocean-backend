from app.services.model_service import predict_temperature
from app.config import DEPTHS


def generate_prediction(ocean_data):
    temperature = predict_temperature(ocean_data)

    return DEPTHS, temperature