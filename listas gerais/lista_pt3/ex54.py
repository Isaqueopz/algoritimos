somaTotal = 0
for i in range(1, 51):
    numerador = 1000 - (3 * (i - 1))
    denominador = i
    termo = numerador / denominador
    somaTotal += termo
print(f"A soma total é {somaTotal:.2f}")
