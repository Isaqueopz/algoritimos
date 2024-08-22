altura = float(input("Altura: "))
sexo = input("Sexo [M/F]: ")
formula_m = (72.7 * altura) - 58
formula_f = (62.1 * altura) - 44.7
if sexo in "Mm":
    print(f"Peso ideal: {formula_m:.1f}")
else:
    if sexo in "Ff":
        print(f"Peso ideal: {formula_f:.1f}")
    else:
        print("Valor inválido")
