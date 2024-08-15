nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1+nota2+nota3) / 3

if media == 10:
    print(f"Você foi aprovado com {media:.1f} pontos de média, com uma grande DISTINÇÃO ")
else:
    if media >= 7:
        print(f"Você alcançou {media:.1f} pontos de média, sendo assim está APROVADO!")
    else:
        print(f"Você alcançou {media:.1f} pontos de média, sendo assim está REPROVADO!")
