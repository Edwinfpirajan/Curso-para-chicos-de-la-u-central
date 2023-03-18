import numpy as np

A = np.random.rand(2, 2)

det_A = np.linalg.det(A)

if det_A == 0:
    print("La matriz es singular y no tiene inversa")
else:
    A_inv = (1/det_A) * np.array([[A[1,1], -A[0,1]], [-A[1,0], A[0,0]]])
    print("La matriz generada es:")
    print(A)
    print("El determinante de la matriz es:", det_A)
    print("La matriz es invertible y su inversa es:")
    print(A_inv)