#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:53:36 2023

@author: vassilis
"""

# Calculates Jaccard binary and normal similarity

import numpy as np

def jaccard_binary(x,y):
    """A function for finding the similarity between two binary vectors"""
    intersection = np.logical_and(x, y)
    union = np.logical_or(x, y)
    #similarity = intersection.sum() / union.sum()
    #return similarity
    return f"{intersection.sum()}/{union.sum()}"

def jaccard_similarity(x, y):
    #Find intersection of two sets
    nominator = x.intersection(y)

    #Find union of two sets
    denominator = x.union(y)

    #Take the ratio of sizes
    #similarity = len(nominator)/len(denominator)
    
    return f"{len(nominator)}/{len(denominator)}"

# Define some binary vectors
S1 = [0,1,0,0,0,1,1,0,0,0]
S2 = [1,0,0,1,1,0,0,1,1,1]
S3 = [1,0,1,0,1,0,1,0,1,0]
S4 = [0,0,0,0,0,1,1,1,1,1]

# Find similarity among the vectors
simS1S2 = jaccard_binary(S1,S2)
simS1S3 = jaccard_binary(S1,S3)
simS1S4 = jaccard_binary(S1,S4)
simS2S3 = jaccard_binary(S2,S3)
simS2S4 = jaccard_binary(S2,S4)
simS3S4 = jaccard_binary(S3,S4)

print("S1S2: ",simS1S2)
print("S1S3: ",simS1S3)
print("S1S4: ",simS1S4)
print("S2S3: ",simS2S3)
print("S2S4: ",simS2S4)
print("S3S4: ",simS3S4)

# Signatures

S1s = {2,3,5}
S2s = {1,1,1}
S3s = {4,1,2}
S4s = {3,4,1}

print("Signatures similarity:")
print("S1S2 sig: ", jaccard_similarity(S1s, S2s))
print("S1S3 sig: ", jaccard_similarity(S1s, S3s))
print("S1S4 sig: ", jaccard_similarity(S1s, S4s))
print("S2S3 sig: ", jaccard_similarity(S2s, S3s))
print("S2S4 sig: ", jaccard_similarity(S2s, S4s))
print("S3S4 sig: ", jaccard_similarity(S3s, S4s))

# For the quiz question 2
Q1 = [0,1,1,0,0,0,1]
Q2 = [1,0,1,0,1,0,0]

# For the quiz question 9

D1 = [1,0,1,0]
D2 = [0,1,1,1]

P1 = {4,3,1,2}
P2 = {1,3,2,4}

print("Quiz, Question 2")
print("Q1,Q2: ", jaccard_binary(Q1, Q2))

print("Quiz Question 9")
print("D1,D2: ",jaccard_binary(D1, D2))
print("P1,P2: ",jaccard_similarity(P1, P2))
