edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingresos >= 2000000:
    print("Debe tributar el impuesto")
else:
    print("No debe tributar el impuesto")