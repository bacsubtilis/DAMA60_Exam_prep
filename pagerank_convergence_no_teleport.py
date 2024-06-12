# Solution for HW3 - Quiz - Question 3

import networkx as nx

# Define the graph
G = nx.DiGraph()
G.add_nodes_from(['0', '1', '2', '3'])
G.add_edges_from([('0', '1'), ('1', '2'), ('2', '3')])

# Set the dangling node penalty to 0
G.nodes['0']['pagerank'] = 0
G.nodes['3']['pagerank'] = 0

# Set the initial pagerank scores
G.nodes['0']['pagerank'] = 1
G.nodes['1']['pagerank'] = 1
G.nodes['2']['pagerank'] = 1

# Iterate until convergence
iter = 0
while True:
    # Calculate the new pagerank scores
    for node in G.nodes():
        G.nodes[node]['pagerank'] = (1 - G.nodes[node]['pagerank']) * G.degree(node) / (G.degree(node) + 1)
        iter = iter+1
        print(iter)

    # Check for convergence
    if all(G.nodes[node]['pagerank'] == round(G.nodes[node]['pagerank'], 5) for node in G.nodes()):
        break

# Print the final pagerank scores
for node in G.nodes():
    print(f"PageRank of node {node}: {G.nodes[node]['pagerank']}")