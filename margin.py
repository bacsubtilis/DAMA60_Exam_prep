import numpy as np

def calculate_margin(w):
    # Calculate the Euclidean norm of the weight vector w
    norm_w = np.linalg.norm(w)
    
    # The margin is given by 2 / norm_w
    margin = 1 / norm_w
    
    return margin

#Solve the 3 line equations(wx+b=0, wx+b=1, wx+b=-1, using w=[w1,w2] and x=[x,y]^T
#w1*x+w2*y+b=0, w1*x+w2*y+b=1, w1*x+w2*y+b=1 
#Put values (x=0,y=?)(y=0,x=?) for all 3 equations


# Define the coefficients and constants from the given equations
A = np.array([
    [0, 2, 1],  # from 0*w1 + 2*w2 + b = 0
    [2, 0, 1],  # from 2*w1 + 0*w2 + b = 0
    [0, 3, 1],  # from 0*w1 + 3*w2 + b = 1
    [3, 0, 1],  # from 3*w1 + 0*w2 + b = 1
    [0, 1, 1],  # from 0*w1 + 1*w2 + b = -1
    [1, 0, 1],  # from 1*w1 + 0*w2 + b = -1
])

B = np.array([0, 0, 1, 1, -1, -1])

# Solve the linear system
solution = np.linalg.lstsq(A, B, rcond=None)[0]

# Extract solutions
w1, w2, b = solution

# Print the results
print(f"w1 = {w1}")
print(f"w2 = {w2}")
print(f"b = {b}")







# Set the corresponding x and y when x=0, y=2 and when y = 0 then x=2
w = np.array([w1, w2])  # weight vector
margin = calculate_margin(w)
print(f"The margin of the classifier is: {margin}")
