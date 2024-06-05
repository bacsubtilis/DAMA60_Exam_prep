#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HITS Algorithm
"""

import numpy as np

def create_adjacency_matrix(links, nodes):
    # Initialize a square adjacency matrix with zeros
    size = len(nodes)
    matrix = np.zeros((size, size))
    # Create a node index mapping to map node names to indices
    node_index = {node: i for i, node in enumerate(nodes)}
    # Fill the adjacency matrix based on the outgoing links
    for node, outlinks in links.items():
        for outlink in outlinks:
            if outlink in node_index:
                # Set 1 for an outgoing link from node to outlink
                matrix[node_index[node], node_index[outlink]] = 1
    return matrix

def hits_algorithm(adj_matrix, iterations=5):
    # Initialize hub and authority scores to 1
    nodes_count = adj_matrix.shape[0]
    hub_scores = np.ones(nodes_count)
    auth_scores = np.ones(nodes_count)
    
    for i in range(iterations):
        # Update authority scores by multiplying with the transpose of the adjacency matrix
        new_auth_scores = np.dot(adj_matrix.T, hub_scores)
        # Normalize authority scores by the maximum value
        auth_scores = new_auth_scores / new_auth_scores.max() if new_auth_scores.max() != 0 else new_auth_scores
        
        # Update hub scores by multiplying with the adjacency matrix using normalized authority scores
        new_hub_scores = np.dot(adj_matrix, auth_scores)
        # Normalize hub scores by the maximum value
        hub_scores = new_hub_scores / new_hub_scores.max() if new_hub_scores.max() != 0 else new_hub_scores
        
        # Print the results for the current iteration
        print(f"Iteration {i+1}:")
        print("Adjacency Matrix (Link Matrix):\n", adj_matrix)
        print("Transpose of the Link Matrix (Adjacency Matrix):\n", adj_matrix.T)
        print("Non-normalized Authority Scores (a):", new_auth_scores)
        print("Normalized Authority Scores (a):", auth_scores)
        print("Non-normalized Hub Scores (h):", new_hub_scores)
        print("Normalized Hub Scores (h):", hub_scores)
        print()  # Blank line for readability

    # Return the final hub and authority scores
    return hub_scores, auth_scores

########################################
# Calculations depending on the exercise
########################################

# Outgoing links and nodes
# SOS HERE WE HAVE ΤΟ NOTE ALL CONNECTIONS E.G.  '1': ['2','3'] DOES NOT EXCLUDE '2': ['1'...ETC.]
# Outgoing links and nodes
outgoing_links = {
    '1': ['2','3'],
    '2': ['1', '3'],
    '3': ['4'],
}

nodes = ['1', '2', '3', '4']
# Create the adjacency matrix from the outgoing links
adj_matrix = create_adjacency_matrix(outgoing_links, nodes)

#NUMBER OF ITERATIONS !!!!!!!!!
iterations = 1

# Run the HITS algorithm for a specified number of iterations
hub_scores, auth_scores = hits_algorithm(adj_matrix, iterations)