import numpy as np

def cramer_solver(a, b):
    n = len(a)
    det_a = determinant(a)
    if det_a == 0:
        return "El determinante de la matriz de coeficientes es cero, no se puede resolver el sistema"
    x = []
    for i in range(n):
        a_i = a.copy()
        for j in range(n):
            a_i[j][i] = b[j]
        det_a_i = determinant(a_i)
        x_i = det_a_i / det_a
        x.append(x_i)
    return x

def determinant(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    det = 0
    for i in range(n):
        a_minor = [[a[j][k] for k in range(n) if k != i] for j in range(1,n)]
        det_i = a[0][i] * ((-1) ** i) * determinant(a_minor)
        det += det_i
    return det

a = np.array([[2, 1, -1], [3, 2, 1], [1, 1, 2]]) # matriz de coeficientes
b = np.array([8, 13, 5]) # vector de términos independientes
x = cramer_solver(a, b)
print("La solución del sistema de ecuaciones es:", x)