letraPedida = str(input("Digite o seu sexo: [M/F] ")).strip()

if letraPedida not in ["M","m","F","f"]:
    print("""SEXO INVÁLIDO!!! 
Digite novamente o sexo escolhido! """)

else: 
    print("Obrigado, o sexo está registrado! ")

