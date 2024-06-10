#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:16:00 2024

@author: vassilis
"""

import math  
import sklearn.metrics  
actual = [5, 4, 4, 5, 
          4.5, 4, 3, 4.5, 
          5, 3, 4, 3]  
predicted = [4, 3, 3, 1, 
             3, 3.5, 2, 2, 
             5, 5, 2, 3]  

mae = sklearn.metrics.mean_absolute_error(actual, predicted)

mse = sklearn.metrics.mean_squared_error(actual, predicted)  
  
rmse = math.sqrt(mse)  
  
print("The MAE is: ", mae)
print("The RMSE is: ", rmse)
print("The MSE is: ", mse)