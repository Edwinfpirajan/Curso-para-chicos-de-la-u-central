sum_10 = sum([1/(k**2) for k in range(1, 11)])
print("Suma hasta k=10:", sum_10)

sum_100 = sum([1/(k**2) for k in range(1, 101)])
print("Suma hasta k=100:", sum_100)

sum_500 = sum([1/(k**2) for k in range(1, 501)])
print("Suma hasta k=500:", sum_500)

if sum_500 < float('inf'):
    print("La serie es convergente")
else:
    print("La serie es divergente")