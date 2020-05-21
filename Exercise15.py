# Exercício 15 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
      # a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
      # vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
      # compradas e o preço total
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

import math

area = input("\nDigite o tamanho da área a ser pintada em metros quadrados: ")

coberturaTinta = float(area) / 3
latasTinta = math.ceil(coberturaTinta / 18)         # math.ceil é uma fórmula para arredondar valor para cima
custoTotal = latasTinta * 80

print("\n\n\tQuantidade de latas de tinta necessária:",latasTinta,"\n"
    "\tO preço total será: R$",custoTotal,"\n\n\n")
