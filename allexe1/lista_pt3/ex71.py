numero = int(input("Digite um número para verificar se é triangular: "))
n = 1
numeroTriangular = True
numeroNãoTriangular = True
while numeroTriangular and numeroNãoTriangular:
    produto = n * (n + 1) * (n + 2)
    if produto == numero:
        print(f"O número {numero} é triangular.")
        numeroTriangular = False
    if produto > numero:
        print(f"O número {numero} não é triangular.")
        numeroNãoTriangular = False
    else:
        n += 1

