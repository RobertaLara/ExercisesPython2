# Exercício 04 - Faça um Programa que converta metros para centímetros
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

valorMetro = input("\n\nDigite o valor em metros que deseja converter para centímetros: ")

valorCentimetro = float(valorMetro)*100

print("\n\n\tValor convertido:",valorCentimetro,"cm\n\n")
