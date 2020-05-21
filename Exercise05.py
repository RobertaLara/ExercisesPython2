# Exercício 05 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

import math         # Importando funções matemáticas

raioCirculo = input("\n\nPara calcular a área de um círculo, digite seu raio: ")

areaCirculo = pow(float(raioCirculo),2) * math.pi       # pow é usado para elevar número à potência que eu desejar
                                                        # math.pi é função matemática para o valor de pi
print("\n\n\tA área do círculo é:",round(areaCirculo,2),"\n\n")     # round mostra quantidade de casas decimais que eu desejar
