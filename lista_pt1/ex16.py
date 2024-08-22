nomeVendendor = str(input("Digite o seu nome: ")).strip()
valorSalarialFixo = int(input("Qual o valor salarial mensal: "))
quantidadeVendas = int(input("Quantas vendas você realizou nesse mês? [EM R$]  "))
comissao = quantidadeVendas * 15/100
salarioTotal = valorSalarialFixo + comissao
print(f"""{nomeVendendor} este mês ganhou R${valorSalarialFixo}reais de salário fixo
e mais R${comissao}reais de comissao totalizando, R${salarioTotal}reais """)