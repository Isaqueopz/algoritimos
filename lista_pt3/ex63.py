primeiroTermo = int(input("Qual será o primeiro termo da série: "))
razao = int(input("Qual será a razão: "))
quantidadeTermo = int(input("Qual vai ser a quantidade de termos: "))
for i in range(1, quantidadeTermo+1):
    formula = primeiroTermo + ((i-1) * razao)
    print(f"{formula}", end=" ")
   
