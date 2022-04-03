# See README.md for description
import os
import numpy as np
import pandas as pd

# Import data
data_path = os.path.abspath("../data")
data_file = "/test1.csv"
data = pd.read_csv(data_path + data_file, header=None)
data = data.to_numpy()
print(data)



