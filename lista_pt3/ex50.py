resposta = True
while resposta == True:
    valorLado = int(input("Qual o valor do lado do quadrilátero: "))
    area = valorLado * valorLado 
    print(f"O valor da área do quadrilátero é {area}")
    pergunta = str(input("Quer continuar: [S/N] ")).strip()
    if pergunta in "Nn":
        break
