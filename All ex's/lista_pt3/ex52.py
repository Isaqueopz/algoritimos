numeroN = int(input("Digite um número para o denominador da fração: "))
valorSoma = 0
for i in range(1, numeroN + 1):
    h = 1 / i
    valorSoma += h
print(f"O valor de h é igual a {valorSoma:.2f}")
