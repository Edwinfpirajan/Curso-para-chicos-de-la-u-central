tarifa_horaria = 10

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

if horas_trabajadas <= 40:
    salario = horas_trabajadas * tarifa_horaria
else:
    salario_base = 40 * tarifa_horaria
    horas_extra = horas_trabajadas - 40
    salario_extra = horas_extra * tarifa_horaria * 1.5
    salario = salario_base + salario_extra

print("El salario del empleado es de ${} dólares.".format(salario))