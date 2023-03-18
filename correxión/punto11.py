def maximo_y_minimo(lista):
    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return (maximo, minimo)

lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximo, minimo = maximo_y_minimo(lista_numeros)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)