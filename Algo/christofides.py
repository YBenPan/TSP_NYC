# See README.md for description
import os
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Import data
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = os.path.join(ROOT_DIR, "Algo", "data", "test1.csv")
adj = pd.read_csv(data_file, header=None)
adj = adj.to_numpy()


def cost(adj, cycle):
    cost = 0
    for i, node in enumerate(cycle[:-1]):
        next_node = cycle[i + 1]
        cost += adj[node][next_node]
    return cost

def shortcutting(circuit):
    nodes = []
    for u, v in circuit:
        if not nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)
    nodes.append(nodes[0])
    return nodes

def christofides_impl(G, weight="weight"):
    loop_nodes = (n for n, neighbors in G.adj.items() if n in neighbors)
    try:
        node = next(loop_nodes)
    except StopIteration:
        pass
    else:
        G = G.copy()
        G.remove_edge(node, node)
        G.remove_edges_from((n, n) for n in loop_nodes)
    check = False
    for n,ndict in G.adj.items():
        if len(ndict)!=len(G)-1:
            check=True
            break
    if check:
        raise nx.NetworkXError("G must be a complete graph.")
    tree = nx.minimum_spanning_tree(G)
    L = G.copy()
    nodes = []
    for v,degree in (tree.degree):
        if degree%2==0: 
            nodes.append(v)
    L.remove_nodes_from(nodes)
    MG = nx.MultiGraph()
    MG.add_edges_from(tree.edges)
    edges = nx.min_weight_matching(L)
    MG.add_edges_from(edges)
    return shortcutting(nx.eulerian_circuit(MG))

def christofides(adj=adj):

    G = nx.from_numpy_array(adj)
    pos = nx.spring_layout(G, scale=2)

    pos[0] = (0.5, 0.5)

    cycle = christofides_impl(G)
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
    return cycle, cost(adj, cycle)
    # plt.show()


def main():
    christofides(adj)

if __name__ == "__main__":
    main()
