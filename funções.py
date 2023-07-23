from classes import *

#Definindo cores
nada = "\033[m"
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'



def mostrar_vida(vida1, vida2, nome1, nome2, situação1, situação2):
    if 550 >= vida1 > 250:
        print(f'{nome1}: {verde}{vida1:.0f}{nada} pontos de vida Status:{situação1}')
    elif 250 >= vida1 > 135:
        print(f'{nome1}: {amarelo}{vida1:.0f}{nada} pontos de vida Status:{situação1}')
    elif 135 >= vida1 > 0:  
        print(f'{nome1}: {vermelho}{vida1:.0f}{nada} pontos de vida Status:{situação1}')
    #Mostrando a vida do jogador 2
    if 550 >= vida2 > 250:
        print(f'{nome2}: {verde}{vida2:.0f}{nada} pontos de vida Status:{situação2}')
    elif 250 >= vida2 > 135:
        print(f'{nome2}: {amarelo}{vida2:.0f}{nada} pontos de vida Status:{situação2}')
    elif 135 >= vida2 > 0:
        print(f'{nome2}: {vermelho}{vida2:.0f}{nada} pontos de vida Status:{situação2}')
