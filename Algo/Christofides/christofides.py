# See README.md for description
import os
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Import data
data_path = os.path.abspath("../data")
data_file = "/test1.csv"
adj = pd.read_csv(data_path + data_file, header=None)
adj = adj.to_numpy()


def cost(adj, cycle):
    cost = 0
    for node, i in enumerate(cycle[:-1]):
        next_node = cycle[i + 1]
        cost += adj[node][next_node]
    return cost


def main():

    G = nx.from_numpy_array(adj)
    pos = nx.spring_layout(G, scale=2)

    pos[0] = (0.5, 0.5)

    cycle = nx.approximation.christofides(G, weight="weight")
    edge_list = list(nx.utils.pairwise(cycle))

    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        edgelist=edge_list,
        edge_color="red",
        node_size=200,
        width=1,
    )
    print(f"The order of traversal is: {cycle}")
    print(f"The cost of the traversal is: {cost(adj, cycle)}")
    plt.show()


if __name__ == "__main__":
    main()
