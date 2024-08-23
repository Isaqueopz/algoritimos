primeiraNota = float(input("Digite a sua primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

if media == 10:
    print("Aprovado com Distinção, a sua média foi 10!")
else:
    if media >= 7:
        print(f"Você foi aprovado! Teve média de {media:.1f} pontos")

    else: 
        print(f"Você foi reprovado com média de {media:.1f} pontos! ")

