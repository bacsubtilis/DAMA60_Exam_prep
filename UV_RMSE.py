import numpy as np

def calculate_rmse(matrix1, matrix2):
    # Ensure matrices are numpy arrays
    matrix1 = np.array(matrix1, dtype=np.float64)
    matrix2 = np.array(matrix2, dtype=np.float64)
    
    # Find indices where neither of the values is NaN
    valid_mask = ~np.isnan(matrix1) & ~np.isnan(matrix2)
    
    # Extract the valid values
    valid_values1 = matrix1[valid_mask]
    valid_values2 = matrix2[valid_mask]
    
    # Calculate RMSE only on valid values
    mse = np.mean((valid_values1 - valid_values2) ** 2)
    rmse = np.sqrt(mse)
    
    return rmse

########## User input #####################

# Example usage with sample matrices from Question 8 Final 2022-2023
matrix1 = [
    [2, None, 4, 1],
    [None, 1, 3, None],
    [2, 4, None, 3],
    [1, 5, None, None]
]

matrix2 = [
    [1, 4, 6, 2],
    [2, 5, 6, 1],
    [1, 3, 4, 1],
    [2, 4, 4, 0]
]

########## User input end ##################


# Replace None with np.nan for easier handling with numpy
matrix1 = np.array([[np.nan if val is None else val for val in row] for row in matrix1], dtype=np.float64)
matrix2 = np.array([[np.nan if val is None else val for val in row] for row in matrix2], dtype=np.float64)

rmse = calculate_rmse(matrix1, matrix2)
print(f"RMSE: {rmse:.4f}")
