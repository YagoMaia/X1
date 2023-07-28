from classes import *




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
