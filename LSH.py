#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LSH
"""
# Use if given the hashed permutations (here H1, H2, H3)
# and the initial sets (here S1, S2, S3) and asked to find the signatures

hash_ex_dict = {"H1":(6,2,8,1,4,3,7,5,10,9), 
                "H2":(2,3,5,8,1,4,6,10,9,7), 
                "H3":(3,5,6,4,2,9,8,1,10,7)}

sets_dict = {"S1":(0,1,0,0,0,1,1,0,0,0), 
              "S2":(1,0,0,1,1,0,0,1,1,1), 
              "S3":(1,0,1,0,1,0,1,0,1,0), 
              "S4":(0,0,0,0,0,1,1,1,1,1)}

for kh, vh in hash_ex_dict.items():
    for ks, vs in sets_dict.items():
        for i in range(1, 11): # we could use the len() function here
            idx = vh.index(i)
            signature_val = vs[idx]
            if signature_val == 1:
                print(f"{kh}:{ks} -> {i}")
                break