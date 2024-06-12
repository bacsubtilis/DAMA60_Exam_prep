#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:47:45 2024

@author: vassilis
"""

import numpy as np

########### BANNER ###############

print('''
 ######                       ######                       
 #     #   ##    ####  ###### #     #   ##   #    # #    # 
 #     #  #  #  #    # #      #     #  #  #  ##   # #   #  
 ######  #    # #      #####  ######  #    # # #  # ####   
 #       ###### #  ### #      #   #   ###### #  # # #  #   
 #       #    # #    # #      #    #  #    # #   ## #   #  
 #       #    #  ####  ###### #     # #    # #    # #    # 
 
 DAMA Edition
 
''')

########### END BANNER ###########

########### USER INPUT AND SETUP #####################
nodes = input("Please enter the nodes of your graph separated by spaces: \n")

beta = float(input("Please enter the beta (1 for no teleportation): "))

iteration = int(input("Enter the number of iterations: "))

nodes_list = nodes.split()

# Get the relationships of the outgoing links
print("\nEnter the outgoing links of each node (separate by spaces)")

node_rel = []
for i in nodes_list:
    node_out = input("Outgoing links of " + i + ": ")
    node_out = node_out.split()
    node_rel.append(node_out)

# Ask the user if they want to keep the default initial probability
use_default_prob = input("Do you want to use the default initial probability of 1/n? (yes/no): ").strip().lower()

if use_default_prob == 'no':
    user_prob = float(input(f"Enter the probability to be used for the initial vector (length {len(nodes_list)}): "))
    initial_vector_prob = [user_prob] * len(nodes_list)
else:
    initial_vector_prob = [1/len(nodes_list)] * len(nodes_list)

# Create the adjacency matrix based on the node relationships
# Initialise a "flat" matrix (simple python list)
Mat_flat = []

for rel in node_rel:
    # For every relationship (rel) map the elements to the index on the nodes list
    indices = [nodes_list.index(x) for x in rel]
    
    # Depending on the number of outgoing rels, create the probability
    if indices:
        prob = 1/len(indices)
    else:
        prob = 0  # No outgoing links, so probability is 0
    
    # Create a zeros numpy array of size equal to the number of the nodes
    # Substitute the zeros at the indices positions with the probability
    # Append this to Mat_flat
    arr = np.zeros(len(nodes_list))
    for x in indices:
        arr.put(x, prob)
    Mat_flat.append(arr)
    
# Convert Mat_flat to np.matrix and transpose to be column stochastic
Mat = np.matrix(Mat_flat).T

######################### END SETUP #######################   

print("\nIs this matrix correct?\n")
print(Mat)


# The main PageRank function that calculates and returns the final vector
# according to the iterations set
# Notes: For NO TELEPORTATION SET beta to 1
#        For iteration just add the number of iterations
#        M is the adjacency matrix
def PageRank(M, beta, iteration, initial_vector_prob):
    # Get the size of the M matrix (only one side is enough. square)
    M_size = len(M)
    
    # Get the initial probability for each node from the user input
    init_prob = np.array(initial_vector_prob)
    
    # Construct the nxn matrix
    nxn = np.zeros((M_size, M_size))
    nxn[:] = init_prob.reshape(-1, 1)
    
    # Calculate the initial matrix A
    Al = (beta * M) + ((1 - beta) * nxn)
    
    # Construct the initial vector
    r = np.matrix(init_prob).reshape(-1, 1)
    
    # Calculate the iterations and return the results
    r_new = r
    for i in range(1, iteration + 1):
        r = Al * r_new
        print("\nIteration", i)
        print(np.transpose(r))
        r_new = r
    
    return r

# Run the PageRank def
test = PageRank(Mat, beta, iteration, initial_vector_prob)
print("\nFinal PageRank Vector:")
print(test)
