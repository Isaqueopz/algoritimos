temperaturaFahrenheit = float(input("Qual a temperatura em Fahrenheit atualmente: "))
conversao = (5*(temperaturaFahrenheit-32)/9)
print(f"""A temperatura em Fahrenheit é de {temperaturaFahrenheit}°F, porém em Celsius fica de 
{conversao:.2f}°C """)