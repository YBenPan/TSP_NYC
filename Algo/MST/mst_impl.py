# Implementation of Prim's algorithm for minimum spanning tree

import networkx as nx


# Find the minimum edge in the graph
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
    mst.add_nodes_from(graph.nodes)

    # Add the first edge
    min_edge = find_min_edge(graph)
    mst.add_edge(min_edge[0], min_edge[1], weight=graph.edges[min_edge]["weight"])

    # Add the remaining edges
    while len(mst.edges) < len(graph.nodes) - 1:
        min_edge = find_min_edge(mst)
        mst.add_edge(min_edge[0], min_edge[1], weight=graph.edges[min_edge]["weight"])

    return mst