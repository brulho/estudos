# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
# Formulas
# R=RAIO C=COMPRIMENTO A=AREA
# C = 2*pi* R Formula do perímetro
# A = piR*R (R ao quadrado) Formula do área
PI = math.pi
raio = float(input("Informe o raio e mostraremos qual é a área:"))
print("A área do raio informado é:",PI*raio*raio)
