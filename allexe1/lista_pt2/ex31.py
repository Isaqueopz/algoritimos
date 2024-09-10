diaEscolhido = int(input("Digite um número que representa o dia da semana: [1-Domingo...2-Segunda...]? "))

if diaEscolhido == 1:
    print("O dia escolhido foi Domingo")
else:
    if diaEscolhido == 2:
        print("O dia escolhido foi Segunda")
    else:
        if diaEscolhido == 3:
            print("O dia escolhido foi Terça")
        else:
            if diaEscolhido == 4:
                print("O dia escolhido foi Quarta")
            else:                
                if diaEscolhido == 5:
                    print("O dia escolhido foi Quinta")
                else:
                    if diaEscolhido == 6:
                        print("O dia escolhido foi Sexta")
                    else:
                        if diaEscolhido == 7:
                            print("O dia escolhido foi Sábado")
                        else:
                            print("Valor inválido!")
