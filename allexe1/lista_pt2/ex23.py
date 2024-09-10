valorPedido = int(input("Digite um valor: "))

if valorPedido == 0:
    print("O valor é nulo")

else:
    if valorPedido > 0:
        print(f"O {valorPedido} é positivo")
    else:
        print(f"O {valorPedido} é negativo")