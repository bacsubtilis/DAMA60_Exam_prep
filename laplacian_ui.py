import numpy as np

def get_nodes():
    nodes = input("Enter the nodes separated by spaces: ").split()
    return nodes

def get_connections(nodes):
    connections = {node: [] for node in nodes}
    for node in nodes:
        conns = input(f"Connections for {node}: ").split()
        connections[node] = conns
    return connections

def create_adjacency_matrix(nodes, connections):
    n = len(nodes)
    adj_matrix = np.zeros((n, n), dtype=int)
    node_index = {node: idx for idx, node in enumerate(nodes)}
    
    for node, conns in connections.items():
        for conn in conns:
            i, j = node_index[node], node_index[conn]
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1  # because the graph is undirected
    
    return adj_matrix

def calculate_laplacian_matrix(adj_matrix):
    degree_matrix = np.diag(adj_matrix.sum(axis=1))
    laplacian_matrix = degree_matrix - adj_matrix
    return laplacian_matrix

# Main script
nodes = get_nodes()
connections = get_connections(nodes)
adj_matrix = create_adjacency_matrix(nodes, connections)
laplacian_matrix = calculate_laplacian_matrix(adj_matrix)

print("Adjacency Matrix:")
print(adj_matrix)
print("\nLaplacian Matrix:")
print(laplacian_matrix)
