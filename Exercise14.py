# Exercício 14 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
        # 1 - salário bruto.
        # 2 - quanto pagou ao INSS.
        # 3 - quanto pagou ao sindicato.
        # 4 - o salário líquido.
            # calcule os descontos e o salário líquido, conforme a tabela abaixo:
                # + Salário Bruto : R$
                # - IR (11%) : R$
                # - INSS (8%) : R$
                # - Sindicato ( 5%) : R$
        # 5 - = Salário Liquido : R$
            # Obs.: Salário Bruto - Descontos = Salário Líquido
#Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

valorHoras = input("\nDigite quanto você ganha por hora: ")
horasMes = input("\nAgora, digite quantas horas trabalhou no mês: ")

salarioBruto = round((float(valorHoras) * float(horasMes)),2)       # Cálculo do Salário Bruto
impostoRenda = round((salarioBruto * 0.11),2)                       # Cálculo do desconto de IR
inss = round((salarioBruto * 0.08),2)                               # Cálculo do desconto de INSS
sindicato = round((salarioBruto * 0.05),2)                          # Cálculo do desconto do Sindicato
descontoTotal = impostoRenda + inss + sindicato                     # Cálculo do Desconto total
salarioLiquido = salarioBruto - descontoTotal                       # Cálculo do Salário Líquido

print("\n\n\t\tHOLERITE\n\n\n"
    "SALÁRIO BRUTO .............................. R$",salarioBruto,"\n\n\n"
    "Descontos aplicados\n\n"
    "   Imposto de renda (11%) .................. R$",impostoRenda,"\n"
    "   INSS (8%) ............................... R$",inss,"\n"
    "   Sindicato (5%) .......................... R$",sindicato,"\n"
    "   TOTAL DE DESCONTOS ...................... R$",descontoTotal,"\n\n\n"
    "SALÁRIO LÍQUIDO ............................ R$",salarioLiquido,"\n\n\n")
