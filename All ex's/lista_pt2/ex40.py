pergunta1 = int(input("Telefonou para vítima [0 - NÃO] [1- SIM] ? "))
pergunta2 = int(input("Esteve no local do crime [0 - NÃO] [1- SIM] ? "))
pergunta3 = int(input("Mora perto da vítima [0 - NÃO] [1- SIM] ? "))
pergunta4 = int(input("Devia para a vítima [0 - NÃO] [1- SIM] ? "))
pergunta5 = int(input("Já trabalhou com a vítima [0 - NÃO] [1- SIM] ? "))

perguntasGeral = 0
if pergunta1 == 1 or pergunta2 == 1 or pergunta3 == 1 or pergunta4 == 1 or pergunta5 == 1:
    perguntasGeral += pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5

if perguntasGeral == 0 or perguntasGeral == 1:
    print("Você é Inocente!")

else: 
    if perguntasGeral == 5:
        print('Você foi classificada como Assasino(a)!')
    if perguntasGeral == 3 or perguntasGeral == 4:
        print('Você foi classificada como Cúmplice!')
    if perguntasGeral == 2:
        print('Você foi classificado como Suspeito(a)! ')