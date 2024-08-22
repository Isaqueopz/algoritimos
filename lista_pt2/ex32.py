nota1 = float(input("Qual a sua primeira nota: "))
nota2 = float(input("Qual a sua segunda nota: "))

media = (nota1+nota2) / 2
situacaoEscolar = ""

if media >= 0 and media <= 4:
    Aproveitamento = "O seu aproveitamento tem conceito E"
    situacaoEscolar = "REPROVADO"

if media > 4 and media <= 6:
    Aproveitamento = "O seu aproveitamento tem conceito D"
    situacaoEscolar = "REPROVADO"

if media > 6 and media <= 7.5:
    Aproveitamento = "O seu aproveitamento tem conceito C"
    situacaoEscolar = "APROVADO"

if media > 7.5 and media <= 9.0:
    Aproveitamento = "O seu aproveitamento tem conceito B"
    situacaoEscolar = "APROVADO"

if media > 9 and media <= 10:
    Aproveitamento = "O seu aproveitamento tem conceito A"
    situacaoEscolar = "APROVADO"

print(f"""As notas do aluno foram {nota1} e {nota2}, tendo assim uma média de {media} pontos.
{Aproveitamento}, e você foi {situacaoEscolar}""")