# Receber entrada do usuário
valorInicial = float(input("Qual o valor da dívida em [R$]: "))
jurosParcela3 = 1.1
jurosParcela6 = 1.15

# Calcular valores com juros e valores das parcelas
valorComJuros3 = valorInicial * jurosParcela3
valorComJuros6 = valorInicial * jurosParcela6
valorDescontado3 = valorComJuros3 - valorInicial
valorDescontado6 = valorComJuros6 - valorInicial
valorParcelas3 = valorComJuros3 / 3
valorParcelas6 = valorComJuros6 / 6

# Define largura das colunas
largura_coluna_1 = 30
largura_coluna_2 = 30
largura_coluna_3 = 30
largura_coluna_4 = 30

# Cabeçalhos
print(
    f"{'Valor da Dívida':<{largura_coluna_1}} {'Valor dos Juros':<{largura_coluna_2}} {'Quantidade de Parcelas':<{largura_coluna_3}} {'Valor da Parcela':<{largura_coluna_4}}"
)

# Imprimir dados formatados diretamente
print(
    f"R${valorInicial:,.2f}".ljust(largura_coluna_1)
    + f"{'0':<{largura_coluna_2}} {'1':<{largura_coluna_3}} R${valorInicial:,.2f}".rjust(
        largura_coluna_4
    )
)
print(
    f"R${valorComJuros3:,.2f}".ljust(largura_coluna_1)
    + f"R${valorDescontado3:,.2f}".ljust(largura_coluna_2)
    + f"{'3':<{largura_coluna_3}} R${valorParcelas3:,.2f}".rjust(largura_coluna_4)
)
print(
    f"R${valorComJuros6:,.2f}".ljust(largura_coluna_1)
    + f"R${valorDescontado6:,.2f}".ljust(largura_coluna_2)
    + f"{'6':<{largura_coluna_3}} R${valorParcelas6:,.2f}".rjust(largura_coluna_4)
)
