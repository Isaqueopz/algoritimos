from time import sleep

print("=" * 50)
print("Bem vindo ao aplicativo de cadastro de informações")
print("=" * 50)
print("Vamos começar...")
sleep(0.5)

listSalario = []
listFilhos = []
somaSalario = 0 
somaFilhos = 0
pessoasAte250 = 0
while True:
    perguntaSalario = float(input("Qual é o seu salário em [R$]: "))
    if perguntaSalario < 0:
        break
    somaSalario += perguntaSalario
    if perguntaSalario <= 250:
        pessoasAte250 += 1 
    perguntaFilhos = int(input("Quantos filhos você tem:  "))
    somaFilhos += perguntaFilhos
    listSalario.append(perguntaSalario)
    listFilhos.append(perguntaFilhos)

mediaSalarial = somaSalario / len(listSalario)
mediaFilhos = somaFilhos / len(listFilhos)
maiorSalario = max(listSalario)
percentualSalario250 = (pessoasAte250 / len(listSalario)) * 100 


print(f"A média salarial da população foi R${mediaSalarial} ")
print(f"A média do número de filhos da população é de {mediaFilhos} filhos ")
print(f"O maior salário da população foi de: R${maiorSalario} ")
print(f"O percentual de pessoas com salário até 250 reais é de: {percentualSalario250}% das pessoas")
