# Exercício 13 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

pesoPeixes = input("\n\nDigite o peso de peixes pescado: ")

excesso = round((float(pesoPeixes) - 50),3)     # round mostra a quantidade de casas decimais que eu desejar

if (excesso > 0 ):      # Se o excesso for maior que 0, ele paga multa
    multa = round(excesso * 4,2)      
    print("\n\n\tO peso de peixes pescado está ultrapassando",excesso,"quilos do limite regulamentado.\n\t\tA multa será de",multa,"reais.\n\n\n")
elif (excesso <= 0):           # Se o excesso for menor ou igual a 0, a multa é 0
    multa = 0
    print("\n\n\tO peso de peixes pescado não ultrapassa o limite regulamentado.\n\t\tVocê não precisará pagar multa.\n\n\n")
