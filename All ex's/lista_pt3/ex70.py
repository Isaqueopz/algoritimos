timeDaCasa = 0
timeDeFora = 0

while timeDaCasa >= 0 and timeDeFora >= 0:
    resultado = input("Resultado da partida: ").split()
    timeDaCasa = int(resultado[0])
    timeDeFora = int(resultado[1])
    if timeDaCasa < 0 or timeDeFora < 0: 
        print("Fim de progama.")
    else:
        if timeDaCasa > timeDeFora:
            print("VITÓRIA, O seu time fez 3 pontos! ")
        else:
            if timeDaCasa == timeDeFora:
                print("EMPATE, O seu time fez 1 ponto! ")
            else:
                if timeDaCasa < timeDeFora:
                    print("DERROTA, o seu time não pontuou! ")

