primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
if primeiroNumero == segundoNumero:
    print("Os valores são iguais")
if primeiroNumero < segundoNumero:
    for i in range(primeiroNumero, segundoNumero + 1):
        print(f"{i}", end=" ")
else:
    for i in range(primeiroNumero, segundoNumero - 1, -1):
        print(f"{i}", end=" ")
