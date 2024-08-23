valorDolar = float(input("Qual o valor do dólar atualmente (em real): "))
quantidadeDeDolar = int(input("Quantos dólares você quer trocar em real? "))
conversao = quantidadeDeDolar * valorDolar
print(f"Feita a troca, agora você tem R${conversao:.2f} reais")