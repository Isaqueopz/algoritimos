listTemperaturas = []
somaTemp = 0
while True:
    valorTemperatura = int(input("Qual o valor da temperatura: "))
    somaTemp += valorTemperatura
    listTemperaturas.append(valorTemperatura)
    pergunta = str(input("Quer continuar [S/N]: ")).strip()
    if pergunta not in ["S", "s"]:
        break
media = somaTemp / len(listTemperaturas)
print(f"A maior temperatura foi: {max(listTemperaturas)}")
print(f"A menor temperatura foi: {min(listTemperaturas)}")
print(f"A média das temperaturas foi de {media:.3f} ")
