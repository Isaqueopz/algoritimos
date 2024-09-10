from time import sleep

print("=" * 50)
print("Bem-vindo ao aplicativo de cadastro de informações")
print("=" * 50)
print("Vamos começar...")
sleep(0.5)

quantRespostasSalario = 0 
somaSalario = 0 
somaFilhos = 0
pessoasAte250 = 0
maiorSalario = 0

salarioMaiorQueZero = True

while salarioMaiorQueZero:
    perguntaSalario = float(input("Qual é o seu salário em [R$]: "))

    if perguntaSalario < 0:
        salarioMaiorQueZero = False
    else:
        if perguntaSalario <= 250:
            pessoasAte250 += 1 

        if perguntaSalario > maiorSalario:
            maiorSalario = perguntaSalario

        perguntaFilhos = int(input("Quantos filhos você tem: "))
        somaFilhos += perguntaFilhos
        somaSalario += perguntaSalario
        quantRespostasSalario += 1 

if quantRespostasSalario > 0:
    mediaSalarial = somaSalario / quantRespostasSalario
    mediaFilhos = somaFilhos / quantRespostasSalario  
    percentualSalario250 = (pessoasAte250 / quantRespostasSalario) * 100
else:
    mediaSalarial = 0
    mediaFilhos = 0
    percentualSalario250 = 0

print(f"A média salarial da população foi R${mediaSalarial:.2f}")
print(f"A média do número de filhos da população é de {mediaFilhos:.2f} filhos")
print(f"O maior salário da população foi de: R${maiorSalario:.2f}")
print(f"O percentual de pessoas com salário até R$250 é de: {percentualSalario250:.2f}% das pessoas")

