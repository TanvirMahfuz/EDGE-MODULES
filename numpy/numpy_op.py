# Broadcasting `a` across rows of `b`
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
result = a + b  
print(result)

#vectorization
a = np.array([1, 2, 3, 4, 5])
result = a * 10  # Multiplies each element by 10
print(result) 

#masked array

data = np.array([1, 2, np.nan, 4, 5])
masked_data = np.ma.masked_invalid(data)
print(masked_data.mean())  # Ignores `np.nan` and calculates the mean

#liniear algebra operation
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # Matrix multiplication
print(np.linalg.inv(A))  # Inverse of A
