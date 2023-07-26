from time import sleep
from random import randint
from math import ceil
from funções import *
print(f'{"Bem Vindo ao X1":=^30}')
classes = ['Arqueiro', 'Paladino', 'Mago', 'Assassino']
classes_jogadores = []
nomes = []
ações = []
rod = poção1 = poção2 = 1
cont1_gelo = cont2_gelo = cont1_queim = cont2_queim = cont1_mira = cont2_mira = cont1_puto = cont2_puto = cont1_prot = cont2_prot = 0
status1 = f'{ciano}Normal{nada}'
status2 = f'{ciano}Normal{nada}'
hp1 = hp2 = 500
estado1 = estado2 = "inválido"
crit = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
ven = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
fogo = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
gelo = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
for j in range(1, 3):
    nome = str(input(f'Digite o nome do jogador {j}: ')).strip().title()
    esc = int(input(f'''[ 1 ] - Arqueiro
[ 2 ] - Paladino
[ 3 ] - Mago
[ 4 ] - Assasino
Escolha a classe do jogador {j}: '''))
    print(f'A classe escolhida foi {classes[esc - 1]}')
    print('-=' * 18)
    classes_jogadores += [classes[esc - 1]]
    nomes += [nome]

Arqueiro = ['Flecha Perfurante', 'Flecha Envenenada',
            'Mira Certeira', 'Chuva de Flechas',
            'Poção']
dano_arqueiro = [10, 20, 0, 45, 50]

Paladino = ['Investida', 'Escudo Divino',
            'Ira', 'Machadada', 'Poção']
dano_paladino = [10, 0, 0, 45, 50]

Mago = ['Bola de Fogo', 'Raio de Gelo',
        'Trovão', 'Jato de Água', 'Poção']
dano_mago = [10, 30, 40, 20, 50]

Assassino = ['Ataque Furtivo', 'Golpe Venenoso',
             'Apunhalada', 'Lançamento de Adaga',
             'Poção']
dano_assassino = [10, 20, 40, 10, 50]


for c in range(0, 2):
    if classes_jogadores[c] == 'Arqueiro':
        ação = (f'''[ 1 ] - {Arqueiro[0]}
[ 2 ] - {Arqueiro[1]}
[ 3 ] - {Arqueiro[2]}
[ 4 ] - {Arqueiro[3]}
[ 5 ] - {Arqueiro[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Paladino':
        ação = (f'''[ 1 ] - {Paladino[0]}
[ 2 ] - {Paladino[1]}
[ 3 ] - {Paladino[2]}
[ 4 ] - {Paladino[3]}
[ 5 ] - {Paladino[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Mago':
        ação = (f'''[ 1 ] - {Mago[0]}
[ 2 ] - {Mago[1]}
[ 3 ] - {Mago[2]}
[ 4 ] - {Mago[3]}
[ 5 ] - {Mago[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Assassino':
        ação = (f'''[ 1 ] - {Assassino[0]}
[ 2 ] - {Assassino[1]}
[ 3 ] - {Assassino[2]}
[ 4 ] - {Assassino[3]}
[ 5 ] - {Assassino[4]}''')
        ações += [ação]



#Bloco Principal
while True:
    print('-=' * 20)
    print(f'{"Rodada":>20} {rod:<20}')
    print('-=' * 20)
    sleep(1)
    #Bloco 1
    while estado1 != "válido":
       
        #Bloco 1.1
        if status1 != f'{amarelo}Congelado{nada}':
            #Bloco 1.2
            mostrar_vida(hp1, hp2, nomes[0], nomes[1], status1, status2)
            print('=' * 37)
            print(f'Ataques disponiveis para o {nomes[0]}:')
            print(ações[0])
            ato1 = int(input('Qual será sua ação? ')) - 1
            sorte1 = randint(0, 9)

            #Caso o jogador 1 tenha escolhido a classe arqueira   
            if classes_jogadores[0] == 'Arqueiro':
                if status1 == f"{vermelho}Mirando{nada}":
                    crit = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
                if ato1 != 2 and ato1 != 4: 
                    crit1 = crit[sorte1]
                    if crit1 == 1:
                        dano1 = dano_arqueiro[ato1] * 2
                        print(f'{vermelho}CRITICO{nada}')
                    else:
                        dano1 = dano_arqueiro[ato1]
                sleep(1)

                if ato1 != 1 and ato1 != 2 and ato1 != 4:
                    print(f'Habilidade usada: {Arqueiro[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                elif ato1 == 1:
                    print(f'Habilidade usada: {Arqueiro[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                    chance_ven1 = randint(0, 9)
                    if ven[chance_ven1] == 1:
                        sleep(1)
                        print(f'{verde}O inimigo ficou ENVENENADO{nada}')
                        sleep(1)
                        print('Causará um dano igual a 1% do Hp')
                        status2 = f'{verde}Envenenado{nada}'
                elif ato1 == 2:
                    print(f'Habilidade usada: {Arqueiro[ato1]}')
                    sleep(1)
                    print('Agora você possui mais chance de acerto crítico...')
                    sleep(1)
                    dano1 = 0
                    status1 = f"{vermelho}Mirando{nada}"
                    estado1 = 'válido'

                elif ato1 == 4:
                    if poção1 == 1:
                        print(f'Habilidade usada: {Arqueiro[ato1]}')
                        sleep(1)
                        print('Vida Recupurada: +150')
                        poção1 = 0
                        sleep(1)
                        print('Suas poções acabaram...')
                        sleep(1)
                        estado1 = 'válido'
                        hp1 += 150
                        if status1 == f'{verde}Envenenado{nada}':
                            status1 = f"{ciano}Normal{nada}"
                        if hp1 >= 500:
                            hp1 = 500
                        
                    else:
                        print('As poções acabaram...')
                        estado1 = 'inválido'

            
            #Caso o jogador 1 tenha escolhido a classe paladina        
            elif classes_jogadores[0] == 'Paladino':
                dano1 = dano_paladino[ato1]
                sleep(1)
                if ato1 != 1 and ato1 != 2 and ato1 != 4:
                    print(f'Habilidade usada: {Paladino[ato1]}')
                    sleep(1)
                    if status1 == f'{vermelho}Puto{nada}':
                        print(f'Dano causado: {dano1*2}')
                    else:
                        print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                elif ato1 == 1:
                    print(f'Habilidade usada: {Paladino[ato1]}')
                    sleep(1)
                    print(f'Dano Reduzido em 50%')
                    status1 = f'{roxo}Protegido{nada}'
                    estado1 = 'válido'
                elif ato1 == 2:
                    print(f'Habilidade usada: {Paladino[ato1]}')
                    sleep(1)
                    print(f'Ataque aumenta em 50%')
                    status1 = f'{vermelho}Puto{nada}'
                    estado1 = 'válido'
                elif ato1 == 4:
                    if poção1 == 1:
                        print(f'Habilidade usada: {Paladino[ato1]}')
                        sleep(1)
                        print(f'Vida Recupurada: +150')
                        poção1 = 0
                        sleep(1)
                        print('Suas poções acabaram...')
                        sleep(1)
                        estado1 = 'válido'
                        hp1 += 150
                        if status1 == f'{verde}Envenenado{nada}':
                            status1 = f"{ciano}Normal{nada}"
                        if hp1 >= 500:
                            hp1 = 500
                        
                    else:
                        print('As poções acabaram...')
                        estado1 = 'inválido'
            
            #Caso o jogador 1 tenha escolhido a classe mago
            elif classes_jogadores[0] == 'Mago':
                dano1 = dano_mago[ato1]
                sleep(1)
                if ato1 == 0:
                    print(f'Habilidade usada: {Mago[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    chance_fogo1 = randint(0, 9)
                    estado1 = 'válido'
                    if fogo[chance_fogo1] == 1:
                        if status2 != f'{azul}Molhado{nada}' and status2 != f'{amarelo}Congelado{nada}':
                            sleep(1)
                            print(f'{vermelho}O inimigo está QUEIMANDO{nada}')
                            sleep(1)
                            print('Causará um dano redução de 30% do dano')
                            status2 = f'{vermelho}Queimando{nada}'
                        elif status2 == f'{azul}mMolhado{nada}':
                            sleep(1)
                            print('O inimigo acabou de tomar uma sauna...')
                            status2 = f'{ciano}Normal{nada}'
                        elif status2 == f'{amarelo}Congelado{nada}':
                            sleep(1)
                            print('O inimigo foi descongelado...')
                            status2 = f'{ciano}Normal{nada}'
                elif ato1 == 1:
                    print(f'Habilidade usada: {Mago[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                    chance_gelo1 = randint(0, 9)
                    if gelo[chance_gelo1] == 1:
                        if status2 == f'{vermelho}Queimando{nada}':
                            sleep(1)
                            print('O inimigo sentiu uma leve brisa resfriante')
                            status2 = f'{ciano}Normal{nada}'
                        else:
                            sleep(1)
                            print(f'{amarelo}Inimigo CONGELADO{nada}')
                            status2 = f'{amarelo}Congelado{nada}'
                            sleep(1)
                            if status2 != f'{azul}Molhado{nada}':
                                cont2_gelo = 1
                            else:
                                cont2_gelo = 0
                elif ato1 == 2:
                    if status2 != f'{azul}Molhado{nada}':
                        print(f'Habilidade usada: {Mago[ato1]}')
                        sleep(1)
                        print(f'Dano causado: {dano1}')
                        estado1 = 'válido'
                    elif status2 == f'{azul}Molhado{nada}':
                        sleep(1)
                        print(f'{cinza}Foi realizado um ataque ELEMENTAL{nada}')
                        dano1 = dano1 * 2
                        sleep(1)
                        print(f'Habilidade usada: {Mago[ato1]}')
                        sleep(1)
                        print(f'Dano causado: {dano1}')
                        status2 = f'{ciano}Normal{nada}'
                        estado1 = 'válido'
                elif ato1 == 3:
                    print(f'Habilidade usada: {Mago[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    sleep(1)
                    estado1 = 'válido'
                    if status2 != f'{vermelho}Queimando{nada}':
                        print('O inimigo está MOLHADO')
                        status2 = f'{azul}Molhado{nada}'
                    else:
                        print('O inimigo acabou de tomar banho...')
                        status2 = f'{ciano}Normal{nada}'
                elif ato1 == 4:
                    if poção1 == 1:
                        print(f'Habilidade usada: {Mago[ato1]}')
                        sleep(1)
                        print('Vida Recupurada: +150')
                        poção1 = 0
                        sleep(1)
                        print('Suas poções acabaram...')
                        sleep(1)
                        estado1 = 'válido'
                        hp1 += 150
                        if status1 == f'{verde}Envenenado{nada}':
                            status1 = f"{ciano}Normal{nada}"
                        if hp1 >= 500:
                            hp1 = 500
                        
                    else:
                        print('As poções acabaram...')
                        estado1 = 'inválido'

            #Caso o jogador 1 tenha escolhido a classe assasina
            elif classes_jogadores[0] == 'Assassino':
                dano1 = dano_assassino[ato1]
                sleep(1)
                if ato1 != 1 and ato1 != 3 and ato1 != 4:
                    print(f'Habilidade usada: {Assassino[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                elif ato1 == 1:
                    print(f'Habilidade usada: {Assassino[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    estado1 = 'válido'
                    chance_ven1 = randint(0, 9)
                    if ven[chance_ven1] == 1:
                        sleep(1)
                        print(f'{verde}O inimigo ficou ENVENENADO{nada}')
                        sleep(1)
                        print('Causará um dano igual a 1% do Hp')
                        status2 = f'{verde}Envenenado{nada}'
                elif ato1 == 3:
                    sleep(1)
                    print('Primeira adaga lançada...')
                    adaga1 = randint(20, 40)
                    sleep(1)
                    print(f'Dano: {adaga1}')
                    sleep(1)
                    print('Segunda adaga lançada...')
                    sleep(1)
                    adaga2 = randint(20, 40)
                    print(f'Dano: {adaga2}')
                    sleep(1)
                    dano1 = adaga1 + adaga2
                    print(f'Dano total: {dano1}')
                    sleep(1)
                    estado1 = 'válido'
                elif ato1 == 4:
                    if poção1 == 1 :
                        print(f'Habilidade usada: {Assassino[ato1]}')
                        sleep(1)
                        print('Vida Recupurada: +150')
                        poção1 = 0
                        sleep(1)
                        print('Suas poções acabaram...')
                        sleep(1)
                        estado1 = 'válido'
                        hp1 += 150
                        if status1 == f'{verde}Envenenado{nada}':
                            status1 = f"{ciano}Normal{nada}"
                        if hp1 >= 500:
                            hp1 = 500
                        
                    else:
                        print('As poções acabaram...')
                        estado1 = 'inválido'
        
        
            #Fim ação jogador 1
            print('=' * 37)
        else:
            print(f'{amarelo}{nomes[0]} está CONGELADO{nada}')
            cont1_gelo += 1
            sleep(1)
            print(f'Faltam {4 - cont1_gelo} rodadas para acabar...')
            if cont1_gelo == 3:
                status1 = f'{ciano}Normal{nada}'
                cont1_gelo = 0
            sleep(1)
            print('=' * 37)
            sleep(1)
            estado1 = "válido"

        #Bloco 1.3
        #Condições para tirar vida do jogador2
        if status2 == f'{roxo}Protegido{nada}':
            hp2 -= ceil((dano1/2))
        else:
            if status1 != f'{vermelho}Puto{nada}' and status1 != f'{vermelho}Queimando{nada}':
                hp2 -= dano1
            elif status1 == f'{vermelho}Puto{nada}':
                hp2 -= dano1 * 2
            elif status1 == f'{vermelho}Queimando{nada}':
                hp2 -= dano1 * 0.7
            if status2 == f'{verde}Envenenado{nada}':
                hp2 -= ceil(0.01*hp2)
    estado1 = 'inválido'
    if hp2 <= 0:
        break
    else:
        while estado2 != "válido":
            mostrar_vida(hp1, hp2, nomes[0], nomes[1], status1, status2)
            print('=' * 37)

            if status2 != f'{amarelo}Congelado{nada}':
                print(f'Ataques disponiveis para o {nomes[1]}:')
                print(ações[1])
                ato2 = int(input('Qual será sua ação? ')) - 1
                sorte2 = randint(0, 9)
                
                #Caso o jogador 2 tenha escolhido a classe arqueira
                if classes_jogadores[1] == 'Arqueiro':
                    if status2 == f"{vermelho}Mirando{nada}":
                        crit = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
                    if ato2 != 2 and ato2 != 4:
                        crit2 = crit[sorte2]
                        if crit2 == 1:
                            dano2 = dano_arqueiro[ato2] * 2
                            print(f'{vermelho}CRITICO{nada}')
                        else:
                            dano2 = dano_arqueiro[ato2]
                    sleep(1)
                    if ato2 != 1 and ato2 != 2 and ato2 != 4:
                        print(f'Habilidade usada: {Arqueiro[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                    elif ato2 == 1:
                        print(f'Habilidade usada: {Arqueiro[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                        chance_ven2 = randint(0, 9)
                        if ven[chance_ven2] == 1:
                            sleep(1)
                            print(f'{verde}O inimigo ficou ENVENENADO{nada}')
                            sleep(1)
                            print('Causará um dano igual a 1% do Hp')
                            status1 = f'{verde}Envenenado{nada}'
                    elif ato2 == 2:
                        print(f'Habilidade usada: {Arqueiro[ato2]}')
                        sleep(1)
                        print('Agora você possui mais chance de acerto crítico...')
                        sleep(1)
                        status2 = f"{vermelho}Mirando{nada}"
                    elif ato2 == 4:
                        if poção2 == 1:
                            print(f'Habilidade usada: {Arqueiro[ato2]}')
                            sleep(1)
                            print('Vida Recupurada: +150')
                            poção2 = 0
                            sleep(1)
                            print('Suas poções acabaram...')
                            sleep(1)
                            estado2 = 'válido'
                            hp2 += 150
                            if status2 == f"{verde}Envenenado{nada}":
                                status2 = f"{ciano}Normal{nada}"
                            if hp2 >= 500:
                                hp2 = 500
            
                        else:
                            print('As poções acabaram...')
                            estado2 = 'inválido'
                
                #Caso o jogador 2 tenha escolhido a classe paladina
                elif classes_jogadores[1] == 'Paladino':
                    dano2 = dano_paladino[ato2]
                    sleep(1)
                    if ato2 != 1 and ato2 != 2 and ato2 != 4:
                        print(f'Habilidade usada: {Paladino[ato2]}')
                        sleep(1)
                        if status2 == f'{vermelho}Puto{nada}':
                            print(f'Dano causado: {dano2*2}')
                        else:
                            print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                    elif ato2 == 1:
                        print(f'Habilidade usada: {Paladino[ato2]}')
                        sleep(1)
                        print(f'Dano Reduzido em 50%')
                        status2 = f'{roxo}Protegido{nada}'
                        estado2 = 'válido'
                    elif ato2 == 2:
                        print(f'Habilidade usada: {Paladino[ato2]}')
                        sleep(1)
                        print(f'Ataque aumenta em 50%')
                        status2 = f'{vermelho}Puto{nada}'
                        estado2 = 'válido'
                    elif ato2 == 4:
                        if poção2 == 1:
                            print(f'Habilidade usada: {Paladino[ato2]}')
                            sleep(1)
                            print('Vida Recupurada: +150')
                            poção2 = 0
                            sleep(1)
                            print('Suas poções acabaram...')
                            sleep(1)
                            estado2 = 'válido'
                            hp2 += 150
                            if status2 == f"{verde}Envenenado{nada}":
                                status2 = f"{ciano}Normal{nada}"
                            if hp2 >= 500:
                                hp2 = 500
                    
                        else:
                            print('As poções acabaram...')
                            estado2 = 'inválido'
                
                #Caso o jogador 2 tenha escolhido a classe mago
                elif classes_jogadores[1] == 'Mago':
                    dano2 = dano_mago[ato2]
                    sleep(1)
                    if ato2 == 0:
                        print(f'Habilidade usada: {Mago[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                        chance_fogo2 = randint(0, 9)
                        if fogo[chance_fogo2] == 1:
                            if status1 != f'{azul}Molhado{nada}' and status1 != f'{amarelo}Congelado{nada}':
                                sleep(1)
                                print(f'{vermelho}O inimigo está QUEIMANDO{nada}')
                                sleep(1)
                                print('Causará um dano redução de 30% do dano')
                                status1 = f'{vermelho}Queimando{nada}'
                            elif status1 == f'{amarelo}Congelado{nada}':
                                sleep(1)
                                print('O inimigo foi descongelado...')
                                status1 = f'{ciano}Normal{nada}'
                            elif status1 == f'{azul}Molhado{nada}':
                                sleep(1)
                                print('O inimigo acabou de tomar uma sauna...')
                                sleep(1)
                                status1 = f'{ciano}Normal{nada}'
                    elif ato2 == 1:
                        print(f'Habilidade usada: {Mago[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                        chance_gelo2 = randint(0, 9)
                        if gelo[chance_gelo2] == 1:
                            if status1 == f'{vermelho}Queimando{nada}':
                                sleep(1)
                                print('O inimigo sentiu uma leve brisa resfriante')
                                status1 = f'{ciano}Normal{nada}'
                            else:
                                sleep(1)
                                print('Inimigo CONGELADO')
                                status1 = f'{amarelo}Congelado{nada}'
                                sleep(1)
                                if status1 != f'{azul}Molhado{nada}':
                                    cont1_gelo = 1
                                else:
                                    cont1_gelo = 0
                    elif ato2 == 2:
                        if status1 != f'{azul}Molhado{nada}':
                            print(f'Habilidade usada: {Mago[ato2]}')
                            sleep(1)
                            print(f'Dano causado: {dano2}')
                            estado2 = 'válido'
                        else:
                            sleep(1)
                            print(f'{cinza}Foi realizado um ataque ELEMENTAL{nada}')
                            dano2 = dano2 * 2
                            sleep(1)
                            print(f'Habilidade usada: {Mago[ato2]}')
                            sleep(1)
                            print(f'Dano causado: {dano2}')
                            status1 = f'{ciano}Normal{nada}'
                            estado2 = 'válido'
                    elif ato2 == 3:
                        print(f'Habilidade usada: {Mago[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        sleep(1)
                        estado2 = 'válido'
                        if status1 != f'{vermelho}Queimando{nada}':
                            print('O inimigo está MOLHADO')
                            status1 = f'{azul}Molhado{nada}'
                        else:
                            print('O inimigo acabou de tomar banho...')
                            status1 = f'{ciano}Normal{nada}'
                    elif ato2 == 4:
                        if poção2 == 1:
                            print(f'Habilidade usada: {Mago[ato2]}')
                            sleep(1)
                            print('Vida Recupurada: +150')
                            poção2 = 0
                            sleep(1)
                            print('Suas poções acabaram...')
                            sleep(1)
                            estado2 = 'válido'
                            hp2 += 150
                            if status2 == f"{verde}Envenenado{nada}":
                                status2 = f"{ciano}Normal{nada}"
                            if hp2 >= 500:
                                hp2  = 500
                        else:
                            print('As poções acabaram...')
                            estado2 = 'inválido'

                #Caso o jogador 2 tenha escolhido a classe assasina
                elif classes_jogadores[1] == 'Assassino':
                    dano2 = dano_assassino[ato2]
                    sleep(1)
                    if ato2 != 1 and ato2 != 3 and ato2 != 4:
                        print(f'Habilidade usada: {Assassino[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                    elif ato2 == 1:
                        print(f'Habilidade usada: {Assassino[ato2]}')
                        sleep(1)
                        print(f'Dano causado: {dano2}')
                        estado2 = 'válido'
                        chance_ven2 = randint(0, 9)
                        if ven[chance_ven2] == 1:
                            sleep(1)
                            print(f'{verde}O inimigo ficou ENVENENADO{nada}')
                            sleep(1)
                            print('Causará um dano igual a 1% do Hp')
                            status1 = f'{verde}Envenenado{nada}'
                    elif ato2 == 3:
                        sleep(1)
                        print('Primeira adaga lançada...')
                        adaga1 = randint(20, 40)
                        sleep(1)
                        print(f'Dano: {adaga1}')
                        sleep(1)
                        print('Segunda adaga lançada...')
                        sleep(1)
                        adaga2 = randint(20, 40)
                        print(f'Dano: {adaga2}')
                        sleep(1)
                        dano2 = adaga1 + adaga2
                        print(f'Dano total: {dano2}')
                        sleep(1)
                        estado2 = 'válido'
                    elif ato2 == 4:
                        if poção2 == 1:
                            print(f'Habilidade usada: {Assassino[ato2]}')
                            sleep(1)
                            print('Vida Recupurada: +150')
                            poção2 = 0
                            sleep(1)
                            print('Suas poções acabaram...')
                            sleep(1)
                            estado2 = 'válido'
                            hp2 += 150
                            if status2 == f"{verde}Envenenado{nada}":
                                status2 = f"{ciano}Normal{nada}"
                            if hp2 >= 500:
                                hp2= 500
                        else:
                            print('As poções acabaram...')
                            estado2 = 'inválido'  
            else:
                print(f'{amarelo}{nomes[1]} está CONGELADO{nada}')
                cont2_gelo += 1
                sleep(1)
                rod += 1
                print(f'Faltam {4 - cont2_gelo} rodadas para acabar...')
                if cont2_gelo == 3:
                    status2 = f'{ciano}Normal{nada}'
                    cont2_gelo = 0
                estado2 = "válido"

        
            #Condições para tirar vida do jogador 1
            if status1 == f'{azul}mProtegido{nada}':
                hp1 -= ceil((dano2/2))
            else:
                if status2 != f'{vermelho}Puto{nada}' and status2 != f'{vermelho}Queimando{nada}':
                    hp1 -= dano2
                elif status2 == f'{vermelho}Puto{nada}':
                    hp1 -= dano2 * 2
                elif status2 == f'{vermelho}Queimando{nada}':
                    hp1 -= dano2 * 0.7
                if status1 == f'{verde}Envenenado{nada}':
                    hp1 -= ceil(0.01*hp2)
        estado2 = "inválido"
        #Finalizando a rodada
        rod += 1
        if status1 == f"{vermelho}Queimando{nada}":
            cont1_queim += 1
            if cont1_queim == 3:
                print('=' * 37)
                print(f'{verde}{nomes[0]} não está mais queimando...{nada}')
                print('=' * 37)
                sleep(1)
                status1 = f'{ciano}Normal{nada}'
                cont1_queim = 0
        if status1 == f'{roxo}Protegido{nada}':
            cont1_prot += 1
            if cont1_prot == 3:
                print('=' * 37)
                print(f'{verde}BUFF de defesa de {nomes[0]} acabou{nada}...')
                print('=' * 37)
                sleep(1)
                status1 = f'{ciano}Normal{nada}'
                cont1_prot = 0
        if status1 == f'{vermelho}Puto{nada}':
            cont1_puto += 1
            if cont1_puto == 3:
                print('=' * 37)
                print(f'{verde}Você não está mais PUTO{nada}')
                print('=' * 37)
                sleep(1)
                status1 = f'{ciano}Normal{nada}'
                cont1_puto = 0
        if status1 == f"{vermelho}Mirando{nada}":
            cont1_mira += 1
            if cont1_mira == 3:
                print('=' * 37)
                print(f'{verde}{nomes[0]} não está mais Mirando{nada}')
                print('=' * 37)
                sleep(1)
                status1 = f'{ciano}Normal{nada}'
                cont1_mira = 0
        if status2 == f"{vermelho}Queimando{nada}":
            cont2_queim += 1
            if cont2_queim == 3:
                print('=' * 37)
                print(f'{vermelho}{nomes[1]} não está mais queimando...{nada}')
                print('=' * 37)
                sleep(1)
                status2 = f'{ciano}Normal{nada}'
                cont2_queim = 0
        if status2 ==f'{roxo}Protegido{nada}':
            cont2_prot += 1
            if cont2_prot == 3:
                print('=' * 37)
                print(f'{vermelho}BUFF de defesa de {nomes[1]} acabou...{nada}')
                print('=' * 37)
                sleep(1)
                status2 = f'{ciano}Normal{nada}'
                cont2_prot = 0
        if status2 == f'{vermelho}Puto{nada}':
            cont2_puto += 1
            if cont2_puto == 3:
                print('=' * 37)
                print(f'{vermelho}Você não está mais PUTO{nada}')
                print('=' * 37)
                sleep(1)
                status2 = f'{ciano}Normal{nada}'
                cont2_puto = 0
        if status2 == f"{vermelho}Mirando{nada}":
            cont2_mira += 1
            if cont2_mira == 3:
                print('=' * 37)
                print(f'{vermelho}{nomes[1]} não está mais Mirando{nada}')
                sleep(1)
                print('=' * 37)
                status2 = f'{ciano}Normal{nada}'
                cont2_mira = 0
        if hp1 <= 0:
            break
            
print('Fim da batalha')
sleep(1)
if hp1 > 0:
    print(f'O vencedor foi {nomes[0]}')
else:
    print(f'O vencedor foi {nomes[1]}')
