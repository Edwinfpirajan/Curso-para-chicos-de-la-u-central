def resolver_ecuacion_lineal(a, b, c):
    x = (c - b) / a
    return x

a = 2
b = 5
c = 11
solucion = resolver_ecuacion_lineal(a, b, c)
print("La solución de la ecuación {}x + {} = {} es x = {}".format(a, b, c, solucion))