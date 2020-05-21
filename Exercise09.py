# Exercício 09 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

celsius = input("\n\nDigite a temperatura em graus Celsius: ")

farenheit = round((float(celsius) * 9 / 5 + 32),2)

print("\n\n\tA temperatura convertida em Farenheit é: ",farenheit,"\n\n")
