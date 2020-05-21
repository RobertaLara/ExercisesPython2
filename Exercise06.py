# Exercício 06 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

ladoQuadrado = input("\n\nPara calcular a área de um quadrado, digite a medida do lado: ")

areaQuadrado = round(pow(float(ladoQuadrado),2),2)     # pow é usado para elevar número à potência que eu desejar
                                                        # round mostra quantidade de casas decimais que eu desejar
print("\n\n\tA área do quadrado é:",areaQuadrado,"\n\n")     
print("\tO dobro da área do quadrado é:",areaQuadrado * 2,"\n\n\n")
