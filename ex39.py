numero1 = int(input("Digite um valor qualquer: "))
numero2 = int(input("Digite outro valor qualquer: "))
operacao = int(input(""" 
[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
Qual operação você quer realizar: """))

valorResultadoConta = 0
adicao = numero1 + numero2
subtracao = numero1 - numero2 
multiplicacao = numero1 * numero2
divisao = numero1 / numero2


if operacao == 1:
    valorResultadoConta = adicao
if operacao == 2:
    valorResultadoConta = subtracao
if operacao == 3:
    valorResultadoConta = multiplicacao
if operacao == 4 :
    valorResultadoConta = divisao


if valorResultadoConta % 2 == 0 and valorResultadoConta > 0 and valorResultadoConta % 1 == 0: 
    print(f"O número {valorResultadoConta} é par, positivo e inteiro! ")

elif valorResultadoConta % 2 == 0 and valorResultadoConta < 0 and valorResultadoConta % 1 == 0: 
    print(f"O número {valorResultadoConta} é par, negativo e inteiro! ")

if valorResultadoConta % 2 == 1:
    situacaonumero = ''
    if valorResultadoConta < 0:
        situacaonumero = "negativo"
    else:
        situacaonumero = "positivo"
        print(f"O número {valorResultadoConta} é impar, {situacaonumero} e decimal")    