somaTemp = 0
maiorTemp  = contagemTemperaturas =  0
menorTemp = 9999 
pergunta = ['S','s']
while pergunta not in ['N','n']: 
    valorTemperatura = int(input("Qual o valor da temperatura: "))
    if valorTemperatura > maiorTemp:
        maiorTemp = valorTemperatura
    if valorTemperatura > 0 and valorTemperatura < menorTemp:
        menorTemp = valorTemperatura
    contagemTemperaturas += 1
    somaTemp += valorTemperatura
    pergunta = str(input("Quer continuar [S/N]: ")).strip()

media = somaTemp / contagemTemperaturas 

print(f"O valor da maior temperatura é de {maiorTemp} e o valor da menor temperatura é de {menorTemp}!! ")
print(f"A média das temperaturas é de {media:.2f} graus! ")
