numero = int(input("qual o número desejado? "))
print(f"Tabuada do número: {numero}")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}*{i} = {resultado}")
