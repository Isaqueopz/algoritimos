#não sabia se poderia usar while, pelo fato de a senhora não ter passado ainda, porém, acho mais organizado fazer esse ex assim.

valorSaque = float(input("Qual o valor do saque levando em considerão o mín de 10 reais e o máx de 600? [ R$ ] "))

quantidadenota1 = 0
quantidadenota5 = 0
quantidadenota10 = 0
quantidadenota50 = 0
quantidadenota100 = 0

if valorSaque < 10 or valorSaque > 600:
    print("Valor inválido, o valor deve estar entre 10 e 600")

else:
    while valorSaque >= 100:
        valorSaque -= 100
        quantidadenota100 += 1

    while valorSaque >= 50:
        valorSaque -= 50
        quantidadenota50 += 1

    while valorSaque >= 10:
        valorSaque -= 10
        quantidadenota10 += 1

    while valorSaque >= 5:
        valorSaque -= 5
        quantidadenota5 += 1

    while valorSaque >= 1:
        valorSaque -= 1
        quantidadenota1 += 1

    print(f"Quantidade de notas de 100: {quantidadenota100}")
    print(f"Quantidade de notas de 50: {quantidadenota50}")
    print(f"Quantidade de notas de 10: {quantidadenota10}")
    print(f"Quantidade de notas de 5: {quantidadenota5}")
    print(f"Quantidade de notas de 1: {quantidadenota1}")