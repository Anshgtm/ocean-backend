import numpy as np


def create_grid():

    latitudes = np.arange(5, 30.01, 0.25)
    longitudes = np.arange(45, 105.01, 0.25)

    return latitudes, longitudes


def create_fake_ocean_data(latitudes, longitudes):

    shape = (len(latitudes), len(longitudes))

    sst = np.zeros(shape)
    sss = np.zeros(shape)
    ssh = np.zeros(shape)
    current_u = np.zeros(shape)
    current_v = np.zeros(shape)
    wind_u = np.zeros(shape)
    wind_v = np.zeros(shape)

    for i, lat in enumerate(latitudes):
        for j, lon in enumerate(longitudes):

            sst[i, j] = 29 - (lat - 5) * 0.05
            sss[i, j] = 35.0
            ssh[i, j] = 0.4
            current_u[i, j] = 0.18
            current_v[i, j] = -0.07
            wind_u[i, j] = 4.2
            wind_v[i, j] = -1.5

    return {
        "sst": sst,
        "sss": sss,
        "ssh": ssh,
        "current_u": current_u,
        "current_v": current_v,
        "wind_u": wind_u,
        "wind_v": wind_v
    }


latitudes, longitudes = create_grid()

print("Number of latitude points:", len(latitudes))
print("Number of longitude points:", len(longitudes))

ocean_data = create_fake_ocean_data(latitudes, longitudes)

for variable, data in ocean_data.items():
    print(variable, "shape:", data.shape)