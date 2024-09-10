print("BEM VINDO A LOJA NA MÃO COM AÇÚCAR!")
print("--------"*5)
quantidadeDeProduto = int(input("Quantos mamão com açucar você irá querer ? [R$5.00 A UNIDADE] "))
print("--------"*8)
valorBruto = quantidadeDeProduto * 5
quantidadeDeParcela = int(input(f"""Em quantas PARCELAS você quer dividir o valor de R${valorBruto}reais
tendo em vista que o máx de parcelas são 5 parcelas: """))
quantidadeDividida = valorBruto // quantidadeDeParcela
print(f"O valor final ficou de R${quantidadeDividida:.2f} reais, uma vez que foi dividido em {quantidadeDeParcela} parcelas. ")