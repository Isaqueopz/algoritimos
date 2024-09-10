anosTrabalhadorMaisVelho = 0
anosTrabalhadorMaisNovo = 999 # ou 0 
numeroDoEmpregadoMaisNovo = 0
numeroDoEmpregadoMaisVelho = 0

pergunta = ['N','n']

while pergunta not in ['S','s']:
    numeroDoEmpregado = int(input("Qual o número de registro do empregado: "))
    anosDeTrabalho = int(input("A quantos anos este empregado trabalha na empresa: "))
    if anosDeTrabalho > anosTrabalhadorMaisVelho:
        numeroDoEmpregadoMaisVelho = numeroDoEmpregado
        anosTrabalhadorMaisVelho = anosDeTrabalho
    else:
        numeroDoEmpregadoMaisNovo = numeroDoEmpregado
        anosTrabalhadorMaisNovo = anosDeTrabalho
    pergunta = str(input("Quer sair do progama[S/N]: ")).strip().lower()


print(f"O trabalhador mais novo na empresa tem registro: {numeroDoEmpregadoMaisNovo} e trabalha aqui faz {anosTrabalhadorMaisNovo} ano(s) ")
print(f"O trabalhador mais antigo na empresa tem registro: {numeroDoEmpregadoMaisVelho} e trabalha aqui faz {anosTrabalhadorMaisVelho} ano(s) ")


