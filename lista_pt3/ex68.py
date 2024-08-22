listNumeros = []
quantidadePar = 0
quantidadeImpar = 0
somapar = 0
somaimpar = 0
somaTotal = 0
while True:
    numeroRequisitado = int(input("Digite um número: "))
    somaTotal += numeroRequisitado
    listNumeros.append(numeroRequisitado)
    if numeroRequisitado % 2 == 0:
        quantidadePar += 1
        somapar += numeroRequisitado
    else:
        quantidadeImpar += 1
        somaimpar += numeroRequisitado
    pergunta = int(input("Quer continuar? [1 - SIM ] [0 - NÃO ] "))
    if pergunta == 0:
        break

if numeroRequisitado < 0:
    print("Esse numero não é positivo! ")

print(f"A quantidade de números pares é: {quantidadePar} números ")
print(f"A quantidade de números impares é: {quantidadeImpar} números ")
print(f"A média de valores pares é de: {somapar / quantidadePar:.2f} ")
print(f"A média geral é de: {somaTotal / len(listNumeros)} ")
