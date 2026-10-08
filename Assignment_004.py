# Matrix addition using Python lists

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("First Matrix:")
for row in matrix1:
    print(row)

print("\nSecond Matrix:")
for row in matrix2:
    print(row)

print("\nAddition of Two Matrices:")
for row in result:
    print(row)

# Matrix addition using NumPy

import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("First Matrix:")
print(matrix1)

print("\nSecond Matrix:")
print(matrix2)

print("\nAddition of Two Matrices:")
print(result)
