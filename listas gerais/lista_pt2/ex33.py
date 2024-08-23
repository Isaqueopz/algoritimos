ladoA = int(input("Digite o primeiro lado do triângulo: "))
ladoB = int(input("Digite o segundo lado do triângulo: "))
ladoC = int(input("Digite o terceiro lado do triângulo: "))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print("Você consegue montar um triângulo")

    if ladoA == ladoB and ladoA != ladoC:
        print("Você tem um triângulo isósceles, possuindo dois lados iguais")

    if ladoA != ladoB != ladoC:
        print("Você tem um triângulo Escaleno, possuindo três lados diferentes")

    if ladoA == ladoB == ladoC:
        print("Você tem um triângulo equilátero, com todos os lados iguais!")
else:
    print("Você não consegue montar o triângulo com esses lados! ")
