# Exercício 12 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        # Para homens: (72.7*h) - 58
        # Para mulheres: (62.1*h) - 44.7
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

altura = input("\n\nDigite a sua altura: ")
sexo = input("\nQual o seu sexo?"
            "\n\tPara homem, digite 1"
            "\n\tPara mulher, digite qualquer outro valor\n")

if (sexo == '1'):               # Se for homem, o calculo realizado será um. Se for mulher, o cálculo será outro
    pesoIdeal = round(((float(altura) * 72.7) - 58),3)      # round mostra a quantidade de casas decimais que eu desejar
elif (sexo != '1'):
    pesoIdeal = round(((float(altura) * 62.1) - 44.7),3)

print("\n\n\tCom base na sua altura e sexo, seu peso ideal é: ",pesoIdeal,"\n\n\n")
