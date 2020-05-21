# Exercício 17 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link 
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

import math         # Importar funçoes matemáticas do Python

tamanhoArquivo = input("\nDigite o tamanho do arquivo para download (em MB): ")
velocidadeLink = input("\nAgora, digite a velocidade do link de Internet (em Mbps): ")

tempoDownload = round((((float(tamanhoArquivo) * 8 )/ float(velocidadeLink)) / 60),2)

print("\n\n\tO tempo de download do arquivo usando esse link é:",tempoDownload,"\n\n\n")
