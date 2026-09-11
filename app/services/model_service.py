from app.config import DEPTHS

def predict_temperature(ocean_data):

    # Get the surface variables
    sst = ocean_data["sst"]
    sss = ocean_data["sss"]
    ssh = ocean_data["ssh"]

    current_u = ocean_data["current_u"]
    current_v = ocean_data["current_v"]

    wind_u = ocean_data["wind_u"]
    wind_v = ocean_data["wind_v"]

    # Fake model:
    # We are using the surface variables to create
    # a simple temperature profile.
    surface_temperature = (
        sst
        - (sss - 35) * 0.1
        + ssh * 0.2
        + (current_u + current_v) * 0.1
        + (wind_u + wind_v) * 0.01
    )

    depths = [
        0, 5, 10, 20, 30,
        50, 75, 100, 125, 150,
        200, 300, 500, 700, 1000
    ]

    temperature = [
        round(surface_temperature - depth * 0.012, 2)
        for depth in DEPTHS
    ]

    return temperature