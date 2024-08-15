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

valorTotal = precoBrutoMorango + precoBrutoMaca


if quantidadeMorangos + quantidadeMacas >= 8 or valorTotal > 25:
    valorComDesconto = valorTotal * 0.9
    valorDescontado = valorTotal - valorComDesconto
    print(f"O valor total pago pelo cliente foi de R${valorTotal}reais, uma vez que somou o R${precoBrutoMorango}reais + R${precoBrutoMaca}reais e foi descontado R${valorDescontado:.2F}reais ")
    print(f"O valor total pago pelo cliente foi de {valorTotal}, uma vez que somou o R${precoBrutoMorango}reais + R${precoBrutoMaca}reais")
else:
    print(f"O valor total pago pelo cliente foi de {valorTotal}, uma vez que somou o R${precoBrutoMorango}reais + R${precoBrutoMaca}reais")