ganhorPorHora = float(input("Quanto você ganha por hora? [R$] "))
horasTrabalhadas = int(input("Qual a quantidade de horas trabalhadas no mês? "))
salarioBruto = ganhorPorHora * horasTrabalhadas
descontoINSS = salarioBruto - (salarioBruto * 0.92)
descontoSindicato = salarioBruto - (salarioBruto * 0.95)
descontoImpostoRenda = salarioBruto - (salarioBruto * 0.89)
salarioLiquido = salarioBruto - descontoINSS - descontoSindicato - descontoImpostoRenda
print(f"{'Descrição':<30} {'Valor (R$)':>15}")
print(f"{'-'*45}")
print(f"{'Salário Bruto:':<30} {salarioBruto:>15.2f}")
print(f"{'Desconto Imposto de Renda:':<30} {-descontoImpostoRenda:>15.2f}")
print(f"{'Desconto INSS:':<30} {-descontoINSS:>15.2f}")
print(f"{'Desconto Sindicato:':<30} {-descontoSindicato:>15.2f}")
print(f"{'Salário Líquido:':<30} {salarioLiquido:>15.2f}")
