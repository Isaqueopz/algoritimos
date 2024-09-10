login_invalido = True
senha_invalida = True
numeroDeTentativasMenor3 = True
numeroTentativas = 0
while login_invalido and senha_invalida and numeroDeTentativasMenor3:
    login = str(input("Digite o seu login: "))
    senha = int(input("Digite a sua senha: "))
    if login in ["Kezia", "kezia"] and senha == 123:
        print("Acesso atorizado!")
        login_invalido = False
        senha_invalida = False
    else:
        if login == login_invalido or senha_invalida:
            print("ACESSO NEGADO!")
            numeroTentativas += 1
        if numeroTentativas >= 3:
            numeroDeTentativasMenor3 = False
