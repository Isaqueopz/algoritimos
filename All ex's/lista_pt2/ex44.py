alturaDoUsuario = float(input("Qual é a sua altura:  "))
sexoDoUsuario = str(input("Qual é o seu sexo? [M/F] "))

pesoIdealHomens = (72.7*alturaDoUsuario) - 58
pesoIdealMulheres = (62.1*alturaDoUsuario) - 44.7

if sexoDoUsuario in "Mm":
    print(f"Você é um homem e com base na sua altura o seu peso ideial é de {pesoIdealHomens}KG's ")
if sexoDoUsuario in "Ff":
    print(f"Você é uma mulher e com base na sua altura o seu peso ideial é de {pesoIdealMulheres}KG's ")