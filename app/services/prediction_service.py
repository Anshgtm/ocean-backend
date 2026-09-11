from datetime import date
from sqlalchemy.orm import Session

from app.models.ocean_data import OceanData
from app.services.model_service import predict_temperature

from app.config import DEPTHS


def generate_prediction(
    db: Session,
    date: date,
    lat: float,
    lon: float
):

    # Find the nearest 0.25° grid point
    grid_lat = round(lat * 4) / 4
    grid_lon = round(lon * 4) / 4

    row = (
        db.query(OceanData)
        .filter(
            OceanData.date == date,
            OceanData.lat == grid_lat,
            OceanData.lon == grid_lon
        )
        .first()
    )

    if row is None:
        return None

    ocean_data = {
        "date": row.date,
        "lat": row.lat,
        "lon": row.lon,
        "sst": row.sst,
        "sss": row.sss,
        "ssh": row.ssh,
        "current_u": row.current_u,
        "current_v": row.current_v,
        "wind_u": row.wind_u,
        "wind_v": row.wind_v
    }

    temperature = predict_temperature(ocean_data)

    return DEPTHS, temperature