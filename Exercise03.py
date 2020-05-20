# Exercício 03 - Faça um Programa que peça as 4 notas bimestrais e mostre a média
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

nota1 = input("\n\nPara calcular a média das 4 notas bimestrais, digite\n\n  Nota Prova 1: ")
nota2 = input("\n  Nota prova 2: ")
nota3 = input("\n  Nota prova 3: ")
nota4 = input("\n  Nota prova 4: ")

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4

print("\n\n\tA média das 4 notas bimestrais é: ",media,"\n\n")
