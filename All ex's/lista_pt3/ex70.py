# Solicita a quantidade de partidas
quantidadeDePartidas = int(input("Qual a quantidade de partidas do campeonato: "))

# Inicializa a soma total de pontos
somaTotal = 0

# Loop para processar cada partida
for _ in range(quantidadeDePartidas):
    # Solicita o placar do jogo
    placar = input("Qual foi o placar do jogo [no formato gols da casa - gols de fora]: ")

    # Divide o placar em duas partes usando o hífen como delimitador
    placarPartes = placar.split('-')
    
    # Converte as partes para inteiros
    placarTime1 = int(placarPartes[0])
    placarTime2 = int(placarPartes[1])
    
    # Verifica se os gols são negativos
    if placarTime1 < 0 or placarTime2 < 0:
        print("O número de gols está inválido!")
        break  # Encerra o loop se algum dos valores de gols for negativo

    # Lógica para calcular os pontos
    if placarTime1 > placarTime2:
        print("O seu time ganhou, você fez 3 pontos.")
        somaTotal += 3
    elif placarTime1 == placarTime2:
        print("O jogo deu empate! Você fez 1 ponto.")
        somaTotal += 1
    else:
        print("O seu time perdeu o jogo, você não pontuou nada.")

# Exibe a pontuação total
print(f"A pontuação total foi de {somaTotal}")

