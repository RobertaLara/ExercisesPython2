# Exercício 01 - Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]""
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

numero = input("\n\nDigite um número: ")

while not numero.isdigit():        # Enquanto o valor não for um número inteiro, o while continua solicitando um número válido
    numero = input("\n\nApenas números inteiros são válidos! Digite novamente: ")

print("\n\n\tO número informado foi: ",numero,"\n\n")
