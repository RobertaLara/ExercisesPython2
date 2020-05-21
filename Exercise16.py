# Exercício 16 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        # - comprar apenas latas de 18 litros;
        # - comprar apenas galões de 3,6 litros;
        # - misturar latas e galões, de forma que o preço seja o menor. 
        # Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# Programadora Roberta Lara

import os          
def clear():            # Função para limpar console
    os.system('clear')
clear()

import math         # Importar funçoes matemáticas do Python

area = input("\nDigite o tamanho da área a ser pintada em metros quadrados: ")

coberturaTinta = (float(area) / 6) * 1.10           # Acrescentei 10% de folga na nessecidade de tinta
quantidadeGalao = math.ceil(coberturaTinta / 18)         # math.ceil é uma fórmula para arredondar valor para cima
quantidadeLata = math.ceil(coberturaTinta / 3.6)
custoGalao = quantidadeGalao * 80
custoLata = quantidadeLata * 25

print("\n\n\nCOMPRANDO APENAS GALÕES DE 18 LITROS\n\n"
    "   Quantidade de galões de tinta necessária:",quantidadeGalao,"\n"
    "   O preço total será: R$",custoGalao)

print("\n\n\nCOMPRANDO APENAS LATAS DE 3.6 LITROS\n\n"
    "   Quantidade de latas de tinta necessária:",quantidadeLata,"\n"
    "   O preço total será: R$",custoLata)

quantidadeMixGalao = 0          # Considerei quantidade inicial de galões e latas como zero
quantidadeMixLata = 0           # Assim, através do while, vou avaliar todas as possibilidades de combinações possíveis
custoMixMinimo = custoGalao + custoLata       # Considerar o maior custo para substituir por valores menores depois

while (quantidadeMixGalao <= quantidadeGalao):
    while (quantidadeMixLata <= quantidadeLata):
        somaCobertura = (quantidadeMixGalao * 18) + (quantidadeMixLata * 3.6)  # Soma para reduzir as repetições do if
        if ( somaCobertura >= coberturaTinta):
            custoMixGalao = quantidadeMixGalao * 80
            custoMixLata= quantidadeMixLata * 25
            custoMix = custoMixGalao + custoMixLata
            if (custoMixMinimo > custoMix):         # if para substituir o custo pelo menor valor encontrado
                custoMixMinimo = custoMix           # Salva na variável o menor custo
                custoMixGalaoMinimo = custoMixGalao     # Salva na variável o custo do galão e lata correspondente
                custoMixLataMinimo = custoMixLata
        quantidadeMixLata = quantidadeMixLata + 1       # Soma 1 para dar continuidade ao while
    quantidadeMixGalao = quantidadeMixGalao + 1
    quantidadeMixLata = 0                           # Considera zero para reiniciar o segundo while e fazer novas combinações

quantidadeMixGalao = math.ceil(custoMixGalaoMinimo / 80)    # Substitui pela quantidade correspondente ao menor custo
quantidadeMixLata = math.ceil(custoMixLataMinimo/25)

print("\n\n\nMINIMIZANDO OS CUSTO MISTURANDO GALÕES E LATAS\n\n"
    "   Quantidade de tinta necessária\n"
    "     - Galões:",quantidadeMixGalao,"\n"
    "     - Latas:",quantidadeMixLata,"\n"
    "\n   Preço total da tinta: R$",custoMixMinimo,"\n"
    "     - Galões: R$",custoMixGalaoMinimo,"\n"
    "     - Latas: R$",custoMixLataMinimo,"\n\n\n")
