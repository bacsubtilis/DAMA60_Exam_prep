import networkx as nx
import numpy as np

# HW4 - Topic4

# Create the graph
# I could not implement it with strings as nodes. networkx can create such graphs but numpy below doesn't like them

# User1 = U1
# User2 = U2
# User3 = U3
# Item1 = I1
# Item2 = I2
# Item3 = I3

#List of nodes
V = ['U1', 'U2', 'U3', 'I1', 'I2', 'I3']

# List of edges
E = [('U1', 'I1'), ('U1', 'I3'), ('U2', 'I2'), ('U3', 'I2')]

G = nx.Graph()

G.add_nodes_from(V)
G.add_edges_from(E)

# Draw the graph to check if it is correct
nx.draw(G, with_labels=True, node_color='red', node_size=1000)

seed = 5
alpha = 0.9

# CHANGE THIS TO SEE EACH STEP e.g. 0 gives the initial one - hot encoded vector, 1 the first step, 2 the second etc.
step = 4

# get the adjacency matrix
A = nx.to_numpy_array(G)

# normalize the rows of thematrix
A = A / A.sum(axis=1, keepdims=True)

print(A.T)

# create the pesonalization vector (the one-hot encoded thingy)
p =  np.zeros(G.number_of_nodes())
p[seed - 1] = 1

# Initialize the score vector with the personalization vector
r = p.copy()

# Print the initial r
print(r)

# Iterate for the given number of steps and give the score vector
for i in range(step):
    r = alpha * A.T @ r + (1 - alpha) * p
    print(r)
