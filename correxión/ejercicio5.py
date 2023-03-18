import numpy as np
from math import sqrt

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

def main():
    coeficientes = []
    for i in range(3):
        coeficiente = float(input(f"Ingrese el coeficiente {i+1}: "))
        coeficientes.append(coeficiente)
    encontrar_cortes(coeficientes)

if __name__ == "__main__":
    main()