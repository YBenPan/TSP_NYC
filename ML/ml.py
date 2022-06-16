import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.svm import SVR


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = f"{ROOT_DIR}/ML/data/nyc-taxi-trip-duration"
# test_df = pd.read_csv(f"{data_path}/test.csv", usecols=["pickup_datetime", "pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude"])
train_df = pd.read_csv(
    f"{data_path}/train.csv",
    usecols=[
        # "pickup_datetime",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "trip_duration",
    ],
)

train_data = train_df.values
X = train_data[:, :-1]
Y = train_data[:, -1]
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.20, random_state=1)

models = []
models.append(("Linear Regression", LinearRegression()))
# models.append(("Support Vector Regression", SVR(gamma="auto")))

results = []
model_names = [model[0] for model in models]
for model_name, model in models:
    kfold = KFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring="neg_mean_absolute_error")
    results.append(cv_results)
    print(model_name, cv_results.mean(), cv_results.std())
