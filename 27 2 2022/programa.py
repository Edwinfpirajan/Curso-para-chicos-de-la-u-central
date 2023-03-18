import numpy as np

# Ejercicio 1
def calcular_nota(promedio_corte_1, promedio_corte_2, promedio_corte_3):
    nota_final = promedio_corte_1 * 0.3 + promedio_corte_2 * 0.3 + promedio_corte_3 * 0.4
    return nota_final

# Ejercicio 2
def calcular_media_y_desviacion_estandar(datos):
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    return media, desviacion_estandar

# Ejercicio 3
def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

# Ejercicio 4
def es_invertible(matriz):
    determinante = np.linalg.det(matriz)
    if determinante != 0:
        return True
    else:
        return False

# Ejercicio 5
def encontrar_cortes(coeficientes):
    a, b, c = coeficientes
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("La función no corta los ejes coordenados.")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La función corta el eje x en {x} y el eje y en {c}.")
    else:
        x1 = (-b + np.sqrt(discriminante)) / (2*a)
        x2 = (-b - np.sqrt(discriminante)) / (2*a)
        print(f"La función corta el eje x en {x1} y {x2} y el eje y en {c}.")

# Ejercicio 6
def resolver_sistema_ecuaciones(A, b):
    det_A = np.linalg.det(A)
    if det_A == 0:
        print("La matriz A no es invertible, el sistema no tiene solución única.")
    else:
        n = A.shape[0]
        soluciones = []
        for i in range(n):
            A_i = A.copy()
            A_i[:, i] = b
            det_A_i = np.linalg.det(A_i)
            solucion_i = det_A_i / det_A
            soluciones.append(solucion_i)
        return np.array(soluciones)

# Ejecutar el programa
if __name__ == '__main__':
    # Ejercicio 1
    promedio_corte_1 = 4.5
    promedio_corte_2 = 3.8
    promedio_corte_3 = 4.2
    nota_final = calcular_nota(promedio_corte_1, promedio_corte_2, promedio_corte_3)
    print(f"La nota final del curso es: {nota_final}")
    
    # Ejercicio 2
    datos = [5, 3, 7, 2, 9, 10]
    media, desviacion_estandar = calcular_media_y_desviacion_estandar(datos)
    print(f"La media de los datos es: {media}")
    print(f"La desviación estándar de los datos es: {desviacion_estandar}")
    
    # Ejercicio 3
    peso = 75
    estatura = 1.8
    imc = calcular_imc(peso, estatura)
    print(f"El índice de masa muscular es: {imc}")
    
    # Ejercicio 4
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if es_invertible(matriz):
        print("La matriz es invertible.")
    else:
        print("La matriz es singular.")
    
    # Ejercicio 5
    coeficientes = [2, -3, 1]
    encontrar_cortes(coeficientes)
    
    # Ejercicio 6
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([4, 5, 6])
    soluciones = resolver_sistema_ecuaciones(A, b)
    if soluciones is not None:
        print(f"La solución del sistema es: {soluciones}")