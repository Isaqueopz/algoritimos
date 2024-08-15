diasDaSemana = [
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado"
]

diaEscolhido = int(input("Digite um número que representa o dia da semana: [1-Domingo...2-Segunda...]? "))

if 0 <= diaEscolhido <= 6:
    print(f"O dia escolhido foi {diasDaSemana[diaEscolhido-1]}")
else:
    print("Valor inválido")












'''if diaEscolhido == 1:
    print("O dia escolhido foi Domingo")
if diaEscolhido == 2:
    print("O dia escolhido foi Segunda")
if diaEscolhido == 3:
    print("O dia escolhido foi Terça")
if diaEscolhido == 4:
    print("O dia escolhido foi Quarta")
if diaEscolhido == 5:
    print("O dia escolhido foi Quinta")
if diaEscolhido == 6:
    print("O dia escolhido foi Sexta")
if diaEscolhido == 7:
    print("O dia escolhido foi Sábado")
else:
    print("Valor inválido")'''


