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

# Get the relationships of the outogoing links
print("\nEnter the outgoing links of each node (separate by spaces)")

node_rel = []
for i in nodes_list:
    node_out = input("Outgoing links of " + i + ": ")
    node_out = node_out.split()
    node_rel.append(node_out)

# Create the adjacency matrix based on the node relationships
# Initialise a "flat" matrix (simple python list)
Mat_flat = []

for rel in node_rel:
    # For every relationship (rel) map the elements to the index on the nodes list
    indices = [nodes_list.index(x) for x in rel]
    
    # Depending on the number of outgoing rels, create the probability
    prob = 1/len(indices)
    
    # Create a zeros numpy array of size equal to the number of the nodes
    # Substitute the zeros at the indices positions with the probability
    # Append this to Mat_flat
    arr = np.zeros(len(nodes_list))
    for x in indices:
        arr.put(x,prob)
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
def PageRank(M, beta, iteration):
    # Get the size of the M matrix (only one side is enough. square)
    M_size = len(M)
    
    # Get the initial probability for each node
    init_prob = 1/M_size
    
    # Construct the nxn matrix
    nxn = np.zeros((M_size, M_size))
    nxn[:]=init_prob
    
    # Calculate the initial matrix A
    Al = (beta * M) + ((1-beta) * nxn)
    
    # Construct the initial vector
    r = np.matrix([init_prob] * M_size)
    r = np.transpose(r)
    
    # Calculate the iterations and return the results
    r_new = r
    for i in range(1, iteration+1):
        r = Al*r_new
        print("\nIteration", i)
        print(np.transpose(r))
        r_new = r
    


# Run the PageRank def
test = PageRank(Mat, beta, iteration)
test

# Note that number 2 below is the number of steps i.e. the power that Mat will be raised
print(np.linalg.matrix_power(Mat, 2))