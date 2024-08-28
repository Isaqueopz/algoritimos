quantidadeNumerosTot = 0 
quantidadePar = 0
quantidadeImpar = 0
somapar = 0
somaimpar = 0
somaTotal = 0
pergunta = 1

while pergunta != 2:
    numeroRequisitado = int(input("Digite um número: "))
    
    if numeroRequisitado <= 0:
        print("Esse número não é positivo! ")
    else:
        somaTotal += numeroRequisitado
        quantidadeNumerosTot += 1
        
        if numeroRequisitado % 2 == 0:
            quantidadePar += 1
            somapar += numeroRequisitado
        else:
            quantidadeImpar += 1
            somaimpar += numeroRequisitado
    
    pergunta = int(input("Quer continuar? [1 - SIM ] [2 - NÃO ] "))

if quantidadeNumerosTot > 0:
    print(f"A quantidade de números pares é: {quantidadePar} números")
    print(f"A quantidade de números ímpares é: {quantidadeImpar} números")
    if quantidadePar > 0:
        print(f"A média de valores pares é de: {somapar / quantidadePar:.2f}")
    print(f"A média geral é de: {somaTotal / quantidadeNumerosTot:.2f}")
else:
    print("Nenhum número positivo foi inserido.")

