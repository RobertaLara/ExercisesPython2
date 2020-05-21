# Exercício 10 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
                    # 1. o produto do dobro do primeiro com metade do segundo .
                    # 2. a soma do triplo do primeiro com o terceiro.
                    # 3. o terceiro elevado ao cubo
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

numeroInteiro1 = input("\n\nDigite o primeiro número inteiro: ")
numeroInteiro2 = input("\n\nDigite o segundo número inteiro: ")
numeroReal = input("\n\nAgora digite um número real: ")

calculo1 = (float(numeroInteiro1) * 2) * (float(numeroInteiro2) / 2)
calculo2 = (float(numeroInteiro1) * 3) + float(numeroReal)
calculo3 = pow(float(numeroReal),3)              # pow é usado para elevar número à potência que eu desejar

print("\n\n\n\tO produto do dobro do primeiro com metade do segundo é: ",calculo1)
print("\n\n\tA soma do triplo do primeiro com o terceiro é: ",calculo2)
print("\n\n\tO terceiro elevado ao cubo é: ",calculo3,"\n\n\n")
