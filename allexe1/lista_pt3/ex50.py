resposta = 'S'
while resposta in "Ss":
    valorLado = int(input("Qual o valor do lado do quadrilátero: "))
    area = valorLado * valorLado 
    print(f"O valor da área do quadrilátero é {area}")
    resposta = str(input("Quer continuar: [S/N] ")).strip()

