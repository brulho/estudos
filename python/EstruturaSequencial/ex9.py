# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
# F = (9*C/5)+32
fahnren = float(input("Informe a temperatura em graus Fahrenheit e converteremos a graus Celsius: \r\n R:"))
celsius = (9*fahnren/5)+32
print(f'A conversão é: {celsius} celsius')
