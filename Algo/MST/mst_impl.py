# Implementation of Prim's algorithm for minimum spanning tree
import os

import networkx as nx


# Find the minimum edge in the graph
import pandas as pd
from matplotlib import pyplot as plt


def find_min_edge(graph):
    # Find the minimum edge
    min_edge = None
    for edge in graph.edges:
        if min_edge is None:
            min_edge = edge
        elif graph.edges[edge]["weight"] < graph.edges[min_edge]["weight"]:
            min_edge = edge
    return min_edge


# Find the minimum spanning tree
def mst(graph):
    # Initialize the minimum spanning tree
    mst = nx.Graph()
    # Add the first edge
    min_edge = find_min_edge(graph)
    mst.add_edge(*min_edge)
    # Add the rest of the edges
    while len(mst.edges) < len(graph.edges):
        min_edge = find_min_edge(graph)
        mst.add_edge(*min_edge)
    return mst


# Test our implementation
if __name__ == "__main__":
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

    # Run our implementation
    mst_graph = mst(graph)

    # Plot our results
    pos = nx.spring_layout(mst_graph)
    labels = nx.get_edge_attributes(mst_graph, "weight")
    nx.draw(mst_graph)
    nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)
    plt.show()