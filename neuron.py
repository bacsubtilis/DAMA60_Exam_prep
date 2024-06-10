# (251) neural neuron Calculate MSE with sigmoid/ tanh / ReLU / identity activation function for one output
# if we had two outputs then 1/2 * (((yactual_before1 - ypred_after1) ** 2) + ((yactual_before2 - ypred_after2) ** 2))

import math

h11 = 0.5
w11 = 1
h21 = 0.5
w21 = 0.2
h31 = 0.5
w31 = 1
b = 0.5
ypred_after = 1

z1 = h11 * w11 + h21 * w21 + h31 * w31 + b

# tanh
yactual_before = (math.exp(z1) - math.exp(-z1)) / (math.exp(z1) + math.exp(-z1))


# ReLU
#yactual_before = max(0, z1)

# Leaky Relu
#def leaky_relu(x, alpha=0.01):
#    return max(alpha * x, x)
#y_actual_before = leaky_relu(z1)

# identity
#yactual_before = z1

# sigmoid
#yactual_before = 1 / (1 + math.exp(-z1))

MSE = (1/1) * ((yactual_before - ypred_after) ** 2)
print(MSE)