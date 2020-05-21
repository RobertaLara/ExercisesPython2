# Exercício 07 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

valorHoras = input("\n\nDigite quanto você ganha por hora: ")
horasMes = input("\n\nAgora, digite quantas horas trabalhou no mês: ")

salario = round((float(valorHoras) * float(horasMes)),2)

print("\n\n\tO salário total referente ao mês é: ",salario,"\n\n")
