nota = 0
quantidadeDeAlunos = 0
while (
    quantidadeDeAlunos <= 4
):  # aqui eu iria trocar o 4 por 29 para ter 30 médias mas só para a senhora testar o progama coloquei 4
    nota1 = float(input("Qual é sua primeira nota: "))
    nota2 = float(input("Qual é sua segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"Sua média foi de {media} pontos")
    quantidadeDeAlunos += 1
