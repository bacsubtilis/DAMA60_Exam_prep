import networkx as nx
import numpy as np


# Calculate the centrality between all edges. 
# Useful in questions that ask you to find the highest betweenness centrality in 
# the whole graph (Like in Question 10 from final)
# Similar to the Girvan-Newman algorithm

def betweenness_edge(G):
    centrality = nx.edge_betweenness_centrality(G, normalized=False)
    print("Edge betweenness centrality \n")
    for key, value in centrality.items():
        print(f"Edge {key}: {value:.1f}")

# Calculate the centrality w.r.t. a node.

def betweenness_node(G, start_node, V):
    centrality = nx.edge_betweenness_centrality_subset(G, start_node, V)
    print("Node betweenness centrality w.r.t. node", start_node,"\n")
    for key, value in centrality.items():
        centrality[key] = value * 2
    for key, value in centrality.items():
        print(f"Edge {key}: {value:.1f}")

### Example 1: Edge betweenness - Question 10 from final ###

# Create the graph

#List of nodes
V1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of edges
E1 = [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('8', '9')]


G1 = nx.Graph()

G1.add_nodes_from(V1)
G1.add_edges_from(E1)

# Draw the graph to check if it is correct
nx.draw(G1, with_labels=True, node_color='red', node_size=1000)


betweenness_edge(G1)

### Example 2: Node betweenness - HW4 Topic-4(b) ###

V2 = ['1', '2', '3', '4', '5', '6']

E2 = [('1', '5'), ('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '6'), ('6', '3')]

G2 = nx.Graph()
G2.add_nodes_from(V2)
G2.add_edges_from(E2)
nx.draw(G2, with_labels=True, node_color='green', node_size=1000)

betweenness_node(G2, '5', V2)
