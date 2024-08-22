import math

# isso caso a senhora queira com a bliblioteca
valor = int(input("Digite um valor para saber o fatorial: "))
valorFatorado = math.factorial(valor)
print(f"O valor fatorado fica de {valorFatorado}")

# com while

c = int(input("Digite um valor para saber o fatorial: "))
valorFatorial = 1
for c in range(c, 0, -1):
    valorFatorial *= c
print(f"O valor de C fatorial é {valorFatorial}")
