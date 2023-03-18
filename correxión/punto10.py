puntuacion = float(input("Ingrese la puntuación entre 0.0 y 5.0: "))

if puntuacion < 0.0 or puntuacion > 5.0:
    print("Error: la puntuación debe estar entre 0.0 y 5.0.")
else:
    if puntuacion >= 4.5:
        calificacion = "Sobresaliente"
    elif puntuacion >= 4.0:
        calificacion = "Notable"
    elif puntuacion >= 3.0:
        calificacion = "Bien"
    elif puntuacion >= 2.0:
        calificacion = "Suficiente"
    else:
        calificacion = "Insuficiente"

    print("La calificación correspondiente a la puntuación {} es: {}".format(puntuacion, calificacion))