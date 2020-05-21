# Exercício 11 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

altura = input("\n\nDigite a sua altura: ")

pesoIdeal = round(((float(altura) * 72.7) - 58),3)      # round mostra a quantidade de casas decimais que eu desejar

print("\n\n\tCom base na sua altura, seu peso ideal é: ",pesoIdeal,"\n\n")
