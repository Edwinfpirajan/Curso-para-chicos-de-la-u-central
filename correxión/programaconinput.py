import numpy as np
from math import sqrt

# Ejercicio 1
def nota_curso(notas):
    nota = notas[0]*0.3 + notas[1]*0.3 + notas[2]*0.4
    return nota

# Ejercicio 2
def media_desviacion(datos):
    media = np.mean(datos)
    desviacion = np.std(datos)
    return media, desviacion

# Ejercicio 3
def calcular_imc(peso, estructura):
    imc = peso / (estructura ** 2)
    return imc

# Ejercicio 4
def es_invertible(matriz):
    if np.linalg.det(matriz) == 0:
        return False
    else:
        return True

# Ejercicio 5
def encontrar_cortes(coeficientes):
    a, b, c = coeficientes
    delta = b**2 - 4*a*c
    if delta < 0:
        print("La función no corta con los ejes coordenados.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"La función corta con el eje x en x={x} y con el eje y en y=0.")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"La función corta con el eje x en x1={x1} y x2={x2} y con el eje y en y=0.")
        coeficientes = []
        for i in range(3):
            coeficiente = float(input(f"Ingrese el coeficiente {i+1}: "))
            coeficientes.append(coeficiente)
        encontrar_cortes(coeficientes)

# Ejercicio 6
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


#=================

if __name__ == '__main__':
    print("Ejercicios disponibles:")
    print("1. Nota del curso")
    print("2. Media y desviación estándar")
    print("3. Índice de masa muscular")
    print("4. Matriz invertible o singular")
    print("5. Cortes con los ejes coordenados")
    print("6. Resolver sistema de ecuaciones lineales con la regla de Cramer")
    ejercicio = int(input("Elija un ejercicio (1-6): "))

    if ejercicio == 1:
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota del corte {i+1}: "))
            notas.append(nota)
        nota_final = nota_curso(notas)
        print(f"La nota del curso es: {nota_final}")

    elif ejercicio == 2:
        datos = input("Ingrese los datos separados por comas: ")
        datos = [float(dato.strip()) for dato in datos.split(",")]
        media, desviacion = media_desviacion(datos)
        print(f"La media es: {media}")
        print(f"La desviación estándar es: {desviacion}")

    elif ejercicio == 3:
        peso = float(input("Ingrese su peso en kg, separada por punto: "))
        estructura = float(input("Ingrese su estructura en m, separada por punto: "))
        imc = calcular_imc(peso, estructura)
        print(f"Su índice de masa muscular es: {imc}")

    elif ejercicio == 4:
        n = int(input("Ingrese la dimensión de la matriz cuadrada: "))
        matriz = []
        for i in range(n):
            fila = input(f"Ingrese la fila {i+1} separada por comas: ")
            fila = [float(numero.strip()) for numero in fila.split(",")]
            matriz.append(fila)
        matriz = np.array(matriz)
        if es_invertible(matriz):
            print("La matriz es invertible.")
        else:
            print("La matriz es singular.")

    elif ejercicio == 5:
        coeficientes = []
        for i in range(3):
            coeficiente = float(input(f"Ingrese el coeficiente {i+1}: "))
            coeficientes.append(coeficiente)
        encontrar_cortes(coeficientes)

    elif ejercicio == 6:
        n = int(input("Ingrese el tamaño de la matriz A (n x n): "))
        A = []
        for i in range(n):
            fila = input(f"Ingrese la fila {i+1} de la matriz A separada por comas: ")
            fila = [float(numero.strip()) for numero in fila.split(",")]
            A.append(fila)
        A = np.array(A)
        b = input(f"Ingrese el vector b separado por comas: ")
        b = [float(numero.strip()) for numero in b.split(",")]
        b = np.array(b)
        x = resolver_sistema_ecuaciones(A, b)
        if x is None:
            print("El sistema no tiene solución única.")
        else:
            print("La solución del sistema es:")
            for i, x_i in enumerate(x):
                print(f"x{i+1} = {x_i}")