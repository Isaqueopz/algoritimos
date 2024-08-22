primeiroProduto = float(input("Qual o valor do produto? R$[ ] "))
segundoProduto = float(input("Qual o valor do produto? R$[ ] "))
terceiroProduto = float(input("Qual o valor do produto? R$[ ] "))

maisBarato = 0
infProduto = ''

if primeiroProduto == segundoProduto == terceiroProduto:
    print("Todos os valores são iguais!")

else:  
    if primeiroProduto < segundoProduto and primeiroProduto < terceiroProduto:
        maisBarato = primeiroProduto
        infProduto = "primeiro Produto"

    elif segundoProduto < primeiroProduto and segundoProduto < terceiroProduto:
        maisBarato = segundoProduto
        infProduto = "segundo Produto"
    else:
        maisBarato = terceiroProduto
        infProduto = "terceiro Produto"
    print(f"""O valor mais barato foi o de R${maisBarato:.2f}reais, ou seja, você deve comprar o
{infProduto}""")