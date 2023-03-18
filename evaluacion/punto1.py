import numpy as np

A = np.array([[1, 1, 1, 2],[-1, 2, -1, 1],[2, 3, 4, -3],[1, 0, 1 , 1]])
B = np.array([[0, 1, 1, 1],[-0.4, 0.3, -0.2, 0.1],[-1, 2, 9, -3], [1, -1, 0, 1]])

AB = np.dot(A, B)
AB_inv = np.linalg.inv(AB)

result = 3 * AB - 6 * np.linalg.matrix_power(A - AB_inv, 4)

print(result)