from app.services.grid_service import create_grid, create_fake_ocean_data
from datetime import date


latitudes, longitudes = create_grid()

ocean_data = create_fake_ocean_data(latitudes, longitudes)


def get_ocean_data(date: date, lat: float, lon: float):

    # Find nearest grid point
    lat_index = min(
        range(len(latitudes)),
        key=lambda i: abs(latitudes[i] - lat)
    )

    lon_index = min(
        range(len(longitudes)),
        key=lambda j: abs(longitudes[j] - lon)
    )

    return {
        "date": date,
        "lat": float(latitudes[lat_index]),
        "lon": float(longitudes[lon_index]),

        "sst": float(ocean_data["sst"][lat_index, lon_index]),
        "sss": float(ocean_data["sss"][lat_index, lon_index]),
        "ssh": float(ocean_data["ssh"][lat_index, lon_index]),

        "current_u": float(
            ocean_data["current_u"][lat_index, lon_index]
        ),
        "current_v": float(
            ocean_data["current_v"][lat_index, lon_index]
        ),

        "wind_u": float(
            ocean_data["wind_u"][lat_index, lon_index]
        ),
        "wind_v": float(
            ocean_data["wind_v"][lat_index, lon_index]
        )
    }