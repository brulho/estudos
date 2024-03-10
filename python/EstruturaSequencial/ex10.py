# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
celsius = float(input("Informe a temperatura em graus Celsius e converteremos a graus Fahrenheit: \r\n R:"))
fahren = 5*((celsius-32)/9)
print(f'A conversão é: {fahren} Fahrenheit')
