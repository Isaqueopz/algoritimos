lista = ["isaque", "rafael", "marcos", "pedro", "raiff"]
#for nome in lista:
#    if nome[0] == "r":
#        print(nome)


#def encontrarLetra(letraPedida):
#    for nome in lista:
#        if nome[0] == letraPedida :
#            print(nome)
#
#encontrarLetra("i")


from random import randint 

numeroEscolhido = int(input("Digite um valor numerico de três digitos: "))

def bruteForce():
    global numeroEscolhido

    numeroSorteado = randint(0,10)

    if numeroEscolhido == numeroSorteado:
        print("Você acertou!")
        
        return True

    print(numeroSorteado)

    return bruteForce()

bruteForce()

