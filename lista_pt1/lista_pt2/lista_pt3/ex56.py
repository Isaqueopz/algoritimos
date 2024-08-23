n = int(input("Digite o número de termos que você quer: "))
soma = 0
denominador = 1
for i in range(1, n + 1):
    termo = i / denominador
    soma += termo
    print(f"{i}/{denominador} = {termo:.4f}")
    denominador += 2
print(f"Soma total da série: {soma:.4f}")
