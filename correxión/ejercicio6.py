import numpy as np

def resolver_sistema_ecuaciones(A, b):
    if np.linalg.det(A) == 0:
        return None
    else:
        x = []
        for i in range(A.shape[0]):
            matriz = A.copy()
            matriz[:, i] = b
            x_i = np.linalg.det(matriz) / np.linalg.det(A)
            x.append(x_i)
        return x

n = int(input("Ingrese el tamaño de la matriz A (n x n): "))
A = []
for i in range(n):
    fila = input(f"Ingrese la fila {i+1} de la matriz A separada por comas: ")
    fila = [float(numero.strip()) for numero in fila.split(",")]
    if len(fila) != n:
        print("Error: la fila no tiene la cantidad correcta de elementos.")
        exit()
    A.append(fila)
A = np.array(A)
b = input(f"Ingrese el vector b separado por comas: ")
b = [float(numero.strip()) for numero in b.split(",")]
if len(b) != n:
    print("Error: el vector b no tiene la cantidad correcta de elementos.")
    exit()
b = np.array(b)
x = resolver_sistema_ecuaciones(A, b)
if x is None:
    print("El sistema no tiene solución única.")
else:
    print("La solución del sistema es:")
    for i, x_i in enumerate(x):
        print(f"x{i+1} = {x_i}")