quantidadeMorangos = int(input("Qual a quantidade de morangos você irá comprar, em [KG'S]: "))
quantidadeMacas = int(input("Qual a quantidade de maçãs você irá comprar, em [KG'S]: "))

precoMorangoAte5 = 2.5
precoMorangoMaisDe5 = 2.2
precoMacaAte5= 1.8
precoMacaMaisDe5 = 1.5
valorTotal = 0


if quantidadeMorangos <= 5:
    precoBrutoMorango = precoMorangoAte5 * quantidadeMorangos

if quantidadeMorangos > 5:
    precoBrutoMorango = precoMorangoMaisDe5 * quantidadeMorangos

if quantidadeMacas <= 5:
    precoBrutoMaca = precoMacaAte5 * quantidadeMacas

if quantidadeMacas > 5:
    precoBrutoMaca = precoMacaMaisDe5 * quantidadeMacas

quantidadeTotal = quantidadeMorangos + quantidadeMacas
valorTotal = precoBrutoMorango + precoBrutoMaca

if quantidadeTotal > 8 and valorTotal > 25:
    valorComDesconto = valorTotal * 0.9
    print(f"O valor com desconto de 10% ficou de R${valorComDesconto:.2f}reais")
else:
    print(f"O valor ficou de R${valorTotal}reais, somando R${precoBrutoMorango}reais do morango com R${precoBrutoMaca}reais da maça")
