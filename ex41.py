quantidadeCombustível = float(input('Qual a quantidade de combustível você irá colocar em litros [L/l]: '))
tipoDeCombustível = str(input("Qual será o tipo de combustível Alcóol[A] ou Gasolina[G]? ")).strip()

valorLitroAlcool = 1.9
valorLitroGasolina = 2.5

if tipoDeCombustível not in "Aa" or "Gg":
    print("Valor inválido, esse combustível não consta em nosso sistema!")

else:
    if quantidadeCombustível <= 20 and tipoDeCombustível in 'Aa':
        valorBruto= (quantidadeCombustível * valorLitroAlcool)
        valorComDesconto = valorBruto - (quantidadeCombustível*0.97)

    if quantidadeCombustível > 20 and tipoDeCombustível in 'Aa':    
        valorBruto= (quantidadeCombustível * valorLitroAlcool)
        valorComDesconto = valorBruto - (quantidadeCombustível* 0.95)

    if quantidadeCombustível <= 20 and tipoDeCombustível in 'Gg':
        valorBruto= (quantidadeCombustível * valorLitroGasolina)
        valorComDesconto = valorBruto - (quantidadeCombustível*0.96)

    if quantidadeCombustível > 20 and tipoDeCombustível in 'Gg':    
        valorBruto= (quantidadeCombustível * valorLitroGasolina)
        valorComDesconto = valorBruto - (quantidadeCombustível* 0.94)

    if tipoDeCombustível in "Aa":
        tipoDeCombustível = "Álcool"

    if tipoDeCombustível in "Gg":
        tipoDeCombustível = "Gasolina" 

    print(f"O cliente escolheu a opção {tipoDeCombustível} e a sua conta deu R${valorComDesconto}reais")