valorBase = int(input("Qual é o valor da base do seu número: "))
valorExpoente = int(input("Qual é o valor do seu expoente: "))
x = 0
valorFinal = 1
while valorExpoente > x:
    valorFinal *= valorBase
    x += 1
print(f"O valor final é de {valorFinal}")
