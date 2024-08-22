salarioBruto = float(input("Diga o seu salário atual: [ R$ ] "))
porcentagem1 = 1.2
porcentagem2 = 1.15
porcentagem3 = 1.1
porcentagem4 = 1.05
porcentagemAplicada = ""

if salarioBruto <= 280:
    novoSalario = salarioBruto * porcentagem1
    porcentagemAplicada = "20%"
    valorAjuste = novoSalario - salarioBruto

if salarioBruto > 280 and salarioBruto <= 700:
    novoSalario = salarioBruto * porcentagem2
    porcentagemAplicada = "15%"
    valorAjuste = novoSalario - salarioBruto

if  salarioBruto > 700 and salarioBruto <= 1500:
    novoSalario = salarioBruto * porcentagem3
    porcentagemAplicada = "10%"
    valorAjuste = novoSalario - salarioBruto

if salarioBruto > 1500:
    novoSalario = salarioBruto * porcentagem4
    porcentagemAplicada = "5%"
    valorAjuste = novoSalario - salarioBruto

print(f"""O salário antes do reajuste era de R${salarioBruto:.2f}reais, a porcentagem de aumento aplicado foi de {porcentagemAplicada} 
o valor do ajuste foi de R${valorAjuste:.2f}reais após passar pelo reajuste ficou de R${novoSalario:.2f}reais""")