ganhorPorHora = float(input("Quanto você ganha por hora? [R$] "))
horasTrabalhadas = int(input("Qual a quantidade de horas trabalhadas no mês? "))

salarioBruto = ganhorPorHora * horasTrabalhadas

porcentagemIR1 = 0.95 
porcentagemIR2 = 0.90
porcentagemIR3 = 0.80

descontoINSS = salarioBruto - (salarioBruto * 0.90)
Fgts = (salarioBruto * 1.11) - salarioBruto

if salarioBruto <= 900:
    salarioBruto = salarioBruto
else: 
    if salarioBruto > 900 and salarioBruto <= 1500:
        novoSalario = salarioBruto*porcentagemIR1
    if salarioBruto > 1500 and salarioBruto <= 2500:
        novoSalario = salarioBruto*porcentagemIR2
    if salarioBruto >= 2500:
        novoSalario = salarioBruto*porcentagemIR3

descontoImpostoRenda = salarioBruto - novoSalario

descontosTotal = descontoINSS + descontoImpostoRenda
salarioLiquido = salarioBruto - descontosTotal

print(f"{'Descrição':<30} {'Valor (R$)':>15}")
print(f"{'-'*45}")
print(f"{'Salário Bruto:':<30}  {salarioBruto:>15.2f}")
print(f"{'Desconto Imposto de Renda:':<30} {-descontoImpostoRenda:>15.2f}")
print(f"{'Desconto INSS:(10%)':<30} {-descontoINSS:>15.2f}")
print(f"{'FGTS:(11%)':<30} {Fgts:>15.2f}")
print(f"{'Salário Líquido:':<30} {salarioLiquido:>15.2f}")
