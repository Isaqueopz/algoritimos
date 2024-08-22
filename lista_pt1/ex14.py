quilometragemPercorrida = float(input("Quantos KM'S você percorre em um mês ? "))
consumoMédio = float(input("Qual o consumo médio de combustível do seu automóvel [LITROS] ? "))
operacao = quilometragemPercorrida / consumoMédio
print(f"O consumo médio do seu veículo é de {operacao}Km/L")