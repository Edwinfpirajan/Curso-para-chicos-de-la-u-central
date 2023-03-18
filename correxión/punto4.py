import numpy as np

A = np.array([[2, 5, 4, 6], [-1, 7, 6, 6], [4, 5, 9, -9], [7, 3, 4, 6]])
B = np.array([5, 4, 7, 13])

X = np.linalg.solve(A, B)

print("La solución del sistema de ecuaciones es:")
print("r =", X[0])
print("s =", X[1])
print("t =", X[2])
print("u =", X[3])