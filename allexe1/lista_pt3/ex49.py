numero = 0
somapar = 0
while numero < 1000:
    if numero % 2 == 0:
        somapar += numero
    numero += 1
print(f"A soma dos números pares deu {somapar}")
