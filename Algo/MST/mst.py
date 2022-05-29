# See README.md for description
import os
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Import our mst implementation
from mst_impl import find_min_edge, mst

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


# Check triangle inequality
def check_triangle_inequality(tri_inequality_graph):
    for edge in tri_inequality_graph.edges:
        if tri_inequality_graph.edges[edge]["weight"] < 0:
            return False
    return True


# Check if graph is connected
def check_connected(connected_graph):
    return nx.is_connected(connected_graph)


# Check if graph is a tree
def check_tree(tree_graph):
    return nx.is_tree(tree_graph)


check_triangle_inequality(graph)
check_connected(graph)
check_tree(graph)


# Run our implementation
mst_graph = mst(graph)

# Plot our results
pos = nx.spring_layout(mst_graph)
labels = nx.get_edge_attributes(mst_graph, "weight")
nx.draw(mst_graph)
nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)
plt.show()



