# Exercício 02 - Faça um Programa que peça dois números e imprima a soma
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

numero1 = input("\n\nPara somar dois valores, digite o primeiro valor: ")
numero2 = input("\nAgora, digite o segundo valor: ")
soma = float(numero1) + float(numero2)

print("\n\n\tA soma dos valores é: ",soma,"\n\n")
