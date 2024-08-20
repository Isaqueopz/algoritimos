quantidadeNum = 0
maiornum = 0
menornum = 0
while quantidadeNum <= 9:
    pedindoNumero = float(input("Qual o número escolhido: "))
    if pedindoNumero > maiornum:
        maiornum = pedindoNumero
    if pedindoNumero < menornum:
        menornum = pedindoNumero
    quantidadeNum += 1
print(f"O maior número foi {maiornum} e o menor número foi {menornum}...")
