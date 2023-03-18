import numpy as np

A = np.random.randint(10, size=(3, 3))
print("Matriz A:")
print(A)

cofactors = np.zeros_like(A)
for i in range(3):
    for j in range(3):
        submatrix = np.delete(np.delete(A, i, axis=0), j, axis=1)
        cofactor = (-1)**(i+j) * np.linalg.det(submatrix)
        cofactors[i, j] = cofactor

adj = cofactors.T
print("Matriz adjunta de A:")
print(adj)

det_A = np.linalg.det(A)
print("Determinante de A:")
print(det_A)

inv_A = np.linalg.inv(A)
print("A^-1:")
print(inv_A)

adj_div_det = adj / det_A
inv_A_diff = inv_A - adj_div_det
print("Diferencia entre A^-1 y (1/det(A)) * Adj(A):")
print(inv_A_diff)