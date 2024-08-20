expoente = 1
sinal = 1
arctan = 0
x = float(input("Valor x:"))
for i in range(50):
    arctan += sinal * ((x**expoente) / expoente)
    expoente += 2
    sinal *= -1
print(arctan)
