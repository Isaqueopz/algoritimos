matriz = [[], [], [], [], []]
valido = False
condicaoAtingida = False
lista = []
print('''
Marcas    Tamanhos
------    --------
Marca A      35
             36
Marca B      37
             38
Marca C      39
             40
''')
while not valido:
  while not condicaoAtingida:
    try:
      marcas = str(input('informe qual marca você quer?[A/B/C] '))
      numero = int(input('Qual número do sapato você deseja? '))
      while numero < 35 or numero > 40:
        print('Valor inválido! Só aceitamos valores de 35 a 40. ')
        numero = int(input('Qual número do sapato você deseja? '))
      if marcas in 'Aa':
        matriz[0].append(numero)
      elif marcas in 'Bb':
        matriz[1].append(numero)
      elif marcas in 'Cc':
        matriz[2].append(numero)
      matriz[3].append(numero)
      pergunta = input('Acabar atendimento? [S/N] ').upper()
      if pergunta in ['S']:
        valido = True
        condicaoAtingida = True
      condicaoAtingida = True  
    except ValueError:
      print("Entrada inválida! Por favor, insira um número válido.")
print('''
            Tamanhos:
        35 36 37 38 39 40
Marca A: ''', end='')
for i in range(6):
  quant = matriz[0].count(35 + i)
  print(f'{quant}', end='  ')
print('\nMarca B:', end=' ')
for i in range(6):
  quant = matriz[1].count(35 + i)
  print(f'{quant}', end='  ')
print('\nMarca C:', end=' ')
for i in range(6):
  quant = matriz[2].count(35 + i)
  print(f'{quant}', end='  ')
for i in range(6):
  quant = matriz[3].count(35 + i)
  matriz[4].append(quant)
maiorQuantNumero = matriz[4].index(max(matriz[4]))
numeroComMaiorQuant = 35 + maiorQuantNumero
print(f'\nNumeração com maior quantidade em estoque: {numeroComMaiorQuant} ({max(matriz[4])} unidades)')
