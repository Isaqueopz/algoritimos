somaIdade = 0
contagemRegular = 0
contagemBom = 0
contagemOtimo = 0
media = 0
continuar = True
while continuar:
        idade = int(input("Qual é a sua idade: "))
        opniao = int(
        input("Qual a sua opnião em relação ao filme [3 -> ÓTIMO, 2 -> BOM, 1 -> REGULAR] ->  ")) 

        if opniao not in [3,2,1]:
            continuar = False
        else:
            if opniao == 3:
                somaIdade += idade
                contagemOtimo += 1
                media = somaIdade / contagemOtimo
            if opniao == 1:
                contagemRegular += 1
            if opniao == 2:
                contagemBom += 1
        

porcentagemBom = (contagemBom / 15) * 100

print(f"A média das idades das pessoas que respoderam ótimo foi {media:.2f} ")
print(f"A quantidade de pessoas que responderam regular: {contagemRegular} pessoas ")
print(
    f"A porcentagem de pessoas que responderam bom entre todos os espectadores analisados foi de {porcentagemBom:.2f}% "
)
