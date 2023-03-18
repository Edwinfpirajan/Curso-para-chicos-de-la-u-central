n = 100 
x_n = 0 

print("Los primeros 10 términos de la sucesión son:")
for i in range(1, 11):
    x_n = ((i+1)/i)**i
    print(f"X{i} = {x_n}")

print("\nLos primeros 50 términos de la sucesión son:")
for i in range(1, 51):
    x_n = ((i+1)/i)**i
    print(f"X{i} = {x_n}")

x_n = ((100+1)/100)**100
print(f"\nEl término 100 de la sucesión es X100 = {x_n}")

n = int(input("\nIngresa el número de términos que deseas mostrar: "))
print(f"\nLos primeros {n} términos de la sucesión son:")
for i in range(1, n+1):
    x_n = ((i+1)/i)**i
    print(f"X{i} = {x_n}")
    
x_n = ((n+1)/n)**n
print(f"\nLa sucesión se está aproximando al número {x_n}")