primeiroValor = float(input("Digite um valor: "))
segundoValor = float(input("Digite outro valor: "))
terceiroValor = float(input("Digite mais um valor: "))

maiorValor = 0

if primeiroValor == segundoValor == terceiroValor:
    print("Todos os valores são iguais!")

else: 
    if primeiroValor > segundoValor and primeiroValor > terceiroValor:
        maiorValor = primeiroValor
    elif segundoValor > primeiroValor and segundoValor > terceiroValor:
        maiorValor = segundoValor
    else:
        maiorValor = terceiroValor
    print(f"O maior valor é {maiorValor}")
