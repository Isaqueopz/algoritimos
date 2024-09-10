numero = int(input("Digite um número para verificar se é primo: "))
if numero == 1:
    print(f"{numero} não é um número primo.")
else:
    eprimo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eprimo = False
    if eprimo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
