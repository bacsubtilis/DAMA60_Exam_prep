# import required libraries
import numpy as np
from numpy.linalg import norm
 
# define two lists or array
A = np.array([2,4,5,5,5])
B = np.array([4,3,4,2,3 ])
 
print("A:", A)
print("B:", B)
 
# compute cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity:", cosine)