turno = str(input("""Em que turno você estuda,tendo em vista que 
M é MATUTINO, V é VESPERTINO e N é NOTURNO!?  """)).strip()

if turno not in ["M","m","V","v","N","n"]:
    print("Valor Inválido!")

else:
    if turno in ["M","m"]:
        print("Bom dia meu parceiro!")
    if turno in ["V","v"]:
        print("Boa tarde amigão!")
    if turno in ["N","n"]:
        print("Boa noite abençoado!")