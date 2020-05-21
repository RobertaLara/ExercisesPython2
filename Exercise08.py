# Exercício 08 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

farenheit = input("\n\nDigite a temperatura em graus Farenheit: ")

celsius = round((5 * (float(farenheit)-32) / 9),2)

print("\n\n\tA temperatura convertida em Celsius é: ",celsius,"\n\n")
