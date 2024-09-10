a = float(input("Valor A: "))

if a == 0:
    print("Não é equação do segundo grau")

else:
    b = float(input("Valor B: "))
    c = float(input("Valor C: "))
    
    delta = (b**2) - (4*a*c)

    if delta < 0:
        print("A equação não possui raizes reais")


    elif delta == 0:
        print("A sua equação vai ter uma raiz")
        x1 = -b / (2*a)
        print(f"A raiz é {x1}")
    else: 
        print("A equação tem duas raizes")
        x1 = (-b + delta ** 0.5) / (2*a)
        x2 = (-b - delta ** 0.5) / (2*a)
        print(x1,x2)