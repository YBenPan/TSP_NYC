# MST heuristic
Steps:
1. Read from a csv file with adjacency matrix
2. Run MST heuristic on the graph 
    1. Check for triangle inequality
    2. Compute MST using Prim's (better than Kruskal's in a complete/dense graph)
    3. Traverse the vertices using DFS, while shortcutting
    4. Run comparison with optimal solution?
3. Save path in a csv file to be outputted by another script (WIP)
