numero = int(input("Digite um número para verificar se é triangular: "))
n = 1
while True:
    produto = n * (n + 1) * (n + 2)
    if produto == numero:
        print(f"O número {numero} é triangular.")
        break
    if produto > numero:
        print(f"O número {numero} não é triangular.")
        break
    else:
        n += 1

