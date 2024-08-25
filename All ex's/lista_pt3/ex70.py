
somaPontosVitoria = 0
somaPontosEmpate = 0
quantidadeDePartidas = int(input("Qual foi a quantidade de partidas jogadas: "))
quantidadeTotalDeGols = int(input("A quantidade total de gols foi de: "))

print('-='*30)
tabelaDeDados = print("""TABELA DE PONTUAÇÕES:
VITÓRIA [1]
EMPATE  [2]
DERROTA [3]""")
print('-='*30)

for i in range (quantidadeDePartidas):
            quantidadeDeGols = int(input(f" Mediante a tabela passada, qual o resultado da {i+1}º partida ? "))
            if quantidadeDeGols not in [1,2,3]:
                print("Número Inválido")
                break
            if quantidadeDeGols == 1:
                somaPontosVitoria += 3
            if quantidadeDeGols == 2:
                somaPontosEmpate += 1
            if quantidadeDeGols < 0:
                break

somaTot = somaPontosVitoria + somaPontosEmpate

print(f"Você jogou {quantidadeDePartidas} partidas, fazendo no total {quantidadeTotalDeGols} gols, sendo assim sua pontuação geral é de {somaTot} pontos! ")
