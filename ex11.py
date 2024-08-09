valorDepositado = float(input("Digite o valor depositado: "))
valorComJuros = valorDepositado * (0.7/100)
valorFinal = valorComJuros + valorDepositado
print(f"O valor inicial era de R${valorDepositado:.2f}reais e o valor final após o seu investimento foi de R${valorFinal:.2f}reais")