import pickle
import os
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from lightgbm import LGBMRegressor
from christofides import christofides

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_time_info(str):
    dt = datetime.strptime(str, "%m-%d-%Y %H:%M:%S")
    month = dt.month
    day = dt.day
    weekday = dt.weekday()
    hour = dt.hour
    minute = dt.minute
    return month, day, weekday, hour, minute

# Load the first row of the input file
input_file = os.path.join(ROOT_DIR, "Algo", "data", "input1.csv")
with open(input_file) as f:
    reader = csv.reader(f)
    row1 = next(reader)

# Get pickup time
month, day, weekday, hour, minute = get_time_info(row1[0])

# Load the rest of the input file
df = pd.read_csv(input_file, skiprows=1)
latitudes = df["Latitude"].values
longitudes = df["Longitude"].values
coords = np.stack((longitudes, latitudes), axis=1)
locations = df["Location"].values

assert len(locations) == len(latitudes) == len(longitudes)

# Load the model that has already been trained with LightGBM
model_file = os.path.join(ROOT_DIR, "ML", "final_model.pickle")
model = pickle.load(open(model_file, "rb"))

# Form input arrays with the following features
# "pickup_longitude",
# "pickup_latitude",
# "dropoff_longitude",
# "dropoff_latitude", 
# "pickup_month",
# "pickup_day",
# "pickup_weekday",
# "pickup_hour",
# "pickup_minute"
adj_matrix = np.zeros((len(locations), len(locations)))
for i, (lat1, lon1) in enumerate(zip(latitudes, longitudes)):
    for j, (lat2, lon2) in enumerate(zip(latitudes, longitudes)):
        if i == j:
            adj_matrix[i][j] = 0
            continue
        if i > j:
            adj_matrix[i][j] = adj_matrix[j][i]
            continue
        X = [lon1, lat1, lon2, lat2, month, day, weekday, hour, minute]
        y = int(model.predict([X])[0])
        # print(f"{locations[i]} --> {locations[j]} takes {y} minutes")
        adj_matrix[i][j] = y
cycle, cost = christofides(adj=adj_matrix)
print(f"{locations[0]}", end="")
for i, node in enumerate(cycle[:-1]):
    next_node = cycle[i + 1]
    time = int(adj_matrix[node][next_node])
    print(f" --({time})--> {locations[next_node]}", end="")
