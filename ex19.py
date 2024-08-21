tamanhoDownload = float(
    input("Qual o tamanho do arquivo que você vai instalar? [em MB] ")
)
velocidadeInternet = float(
    input("Qual é a velocidade do link de Internet utilizado ? [em MBps] ")
)
tempoSegundos = tamanhoDownload / velocidadeInternet
tempoMinutos = tempoSegundos / 60
print(f"O tempo aproximado de download é de {tempoMinutos:.2f} minutos.")

