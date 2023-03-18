TARIFA_MINIMA = 5200

distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))

valor_carrera = TARIFA_MINIMA + (distancia * 2500)

print("El valor de la carrera de taxi es de {} pesos colombianos.".format(valor_carrera))