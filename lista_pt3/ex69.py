listCodigos = []
listQuantidades = []
itens = {
        100 : "Cachorro Quente",
        101 : 'Bauru Simples',
        102 : 'Bauru com ovo',
        103 : 'Hambúrguer',
        104 : 'Cheeseburguer',
        105 : 'Refrigerante',
        }

while True:
    codigoDoProduto = int(
        input("""
Especificação    Código  

Cachorro Quente - 100 
Bauru Simples   - 101 
Bauru com ovo   - 102 
Hambúrguer      - 103 
Cheeseburguer   - 104 
Refrigerante    - 105 

Qual será o código do produto? """)
    )
    quantidade = int(input(f"Qual a quantidade que você quer de {itens[codigoDoProduto]}: "))


    listCodigos.append(codigoDoProduto)
    listQuantidades.append(quantidade)

    pergunta = str(input("Você quer encerrar a compra [S/N]:  "))
    if pergunta in ["S","s"]:
        break


