idade = int(input("Qual é a sua idade: "))
if idade in [5,6,7]:
    print("Você está na categoria infantil A ")
if idade in [8,9,10]:
    print("Você está na categoria infantil B ")
if idade in [11,12,13]:
    print("Você está na categoria juvenil A ")
if idade in [14,15,17]:
    print("Você está na categoria juvenil B ")
if idade >= 18:
    print("Você está na categoria Adulto ")