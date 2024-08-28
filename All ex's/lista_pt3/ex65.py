valorInicial = float(input("Qual o valor da dívida em [R$]: "))

jurosParcela3 = 1.1
jurosParcela6 = 1.15

valorComJuros3 = valorInicial * jurosParcela3
valorComJuros6 = valorInicial * jurosParcela6

valorParcelas3 = valorComJuros3 / 3
valorParcelas6 = valorComJuros6 / 6

valorDescontado3 = valorComJuros3 - valorInicial
valorDescontado6 = valorComJuros6 - valorInicial
#cabeçalho
print(f"{'Valor da Dívida':<18} {'Valor dos Juros':<17} {'Parcelas':<10} {'Valor da Parcela':<20}")
#pagamento a vista
print(f"R${valorInicial:,.2f}".ljust(20) + "R$0,00".ljust(20) + "1".ljust(10) + f"R${valorInicial:,.2f}".rjust(10))
# pagamento 3 parcelas
print(f"R${valorComJuros3:,.2f}".ljust(20) + f"R${valorDescontado3:,.2f}".ljust(20) + "3".ljust(10) + f"R${valorParcelas3:,.2f}".rjust(10))
# pagamaento 6 parcelas
print(f"R${valorComJuros6:,.2f}".ljust(20) + f"R${valorDescontado6:,.2f}".ljust(20) + "6".ljust(10) + f"R${valorParcelas6:,.2f}".rjust(10))

