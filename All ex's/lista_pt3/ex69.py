print("""                 Código  Valor
Cachorro quente - 100 - R$1.20
Bauru simples   - 101 - R$1.30
Bauru com ovo   - 102 - R$1.50
Hambúrguer      - 103 - R$1.20
Cheeseburguer   - 104 - R$1.30
Refrigerante    - 105 - R$1.00
      """)

somaTotal = 0

while True:
    opcao = int(input("Escolha itens acima através do código para realizar sua compra: "))

    if opcao < 100 or opcao > 105:
        print("Opção inválida, selecione o código novamente.")
        continue

    quantidade = int(input('Qual será a quantidade que você irá querer: '))
    
    if opcao == 100 or opcao == 103:
        somaTotal += quantidade * 1.20
            
    if opcao == 101 or opcao == 104:
        somaTotal += quantidade * 1.30
            
    if opcao == 102:
        somaTotal += quantidade * 1.50

    if opcao == 105:
        somaTotal += quantidade * 1.00

    pergunta = input("Quer continuar [S/N]: ").strip().lower()
    if pergunta == 'n':
        break

print(f"A soma total foi de: R${somaTotal:.2f}")

