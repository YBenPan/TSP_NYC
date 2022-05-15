# See README.md for description
import os
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Import data
data_path = os.path.abspath("../data")
data_file = "/test1.csv"
data = pd.read_csv(data_path + data_file, header=None)
data = data.to_numpy()

graph = nx.from_numpy_array(data)
pos = nx.spring_layout(graph)
labels = nx.get_edge_attributes(graph, "weight")
nx.draw(graph)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()



