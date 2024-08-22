primeiroValor = float(input("Qual o primeiro valor: "))
segundoValor = float(input("Qual o segundo valor: "))

maiorValor = 0

if primeiroValor == segundoValor:
    print("Os valores são iguais")

else:
    if primeiroValor > segundoValor:
        maiorValor = primeiroValor
        print(f"O número {maiorValor} é maior que {segundoValor}")
    else:
        maiorValor = segundoValor
        print(f"O número {maiorValor} é maior que {primeiroValor}")