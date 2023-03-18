import numpy as np

A = np.random.randint(10, size=(3, 3))
print("Matriz A:")
print(A)

if np.array_equal(A, A.T):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")