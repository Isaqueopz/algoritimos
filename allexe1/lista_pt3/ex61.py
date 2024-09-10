numeroDePessoasAtualizado = 0
numeroDePessoas = int(input("Digite a quantidade de pessoas que vão participar do progama: "))
somaIdade = 0
idadeMaiorQueZero = True
for i in range(1, numeroDePessoas + 1):
    idade = int(input(f"Qual a idade da {i} pessoa: "))
    if idade == 0:
        print("Vocẽ digitou uma idade inválida! ")
        numeroDePessoasAtualizado = numeroDePessoas - 1 
        idadeMaiorQueZero = False
    else:
        somaIdade += idade
media = somaIdade / numeroDePessoasAtualizado

if media > 0 and media <= 25:
    print("A classificação média das idades é: JOVEM")
if media > 25 and media <= 60:
    print("A classificação média das idades é: ADULTA")
if media > 60:
    print("A classificação média das idades é: IDOSA")
