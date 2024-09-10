numero1 = float(input("Digite um valor qualquer: "))
numero2 = float(input("Digite outro valor qualquer: "))
operacao = float(input(""" 
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
elif operacao == 2:
    valorResultadoConta = subtracao
elif operacao == 3:
    valorResultadoConta = multiplicacao
elif operacao == 4:
    valorResultadoConta = divisao
else:
    print("Operação Inválida")
    exit()

if valorResultadoConta % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

if valorResultadoConta > 0:
    sinal = "Positivo"
if valorResultadoConta < 0:
    sinal = "Negativo"
else:
    sinal = "Zero"

if valorResultadoConta % 1 == 0:
    tipo = "Inteiro"
else:
    tipo = "Decimal"

print(f"""O valor obtido após a conta é {paridade}, {sinal} e {tipo}
 valor obtido é {valorResultadoConta:.2f}""")
