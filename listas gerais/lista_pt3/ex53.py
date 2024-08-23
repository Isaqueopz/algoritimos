valorX = int(input("Diga um valor x qualquer: "))
valorFinal = 0
for i in range(1, 101):
    y = valorX + i
    valorFinal += y
print(f"O valor final da soma é {valorFinal}")
