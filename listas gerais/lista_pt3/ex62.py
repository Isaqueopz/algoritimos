a = int(input("Qual o primeiro valor: "))
b = int(input("Qual o segundo valor: "))
nTermos = int(input("Qual o número de termos: [OBS:MÍNIMO DE TRÊS TERMOS] "))
serie = []
for i in range(nTermos):
    serie.append(a)
    a, b = b, a + b
print(serie)
