temperaturaCelsius = float(input("Qual a temperatura em Celsius atualmente: "))
conversao = (temperaturaCelsius * 1.8) + 32
print(f"""A temperatura em Celsius é de {temperaturaCelsius}°C, porém em Fahrenheit fica de 
{conversao:.2f}°F """)