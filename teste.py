from classes import *

#Arqueiro = ['Flecha Perfurante', 'Flecha Envenenada',
#            'Mira Certeira', 'Chuva de Flechas',
#            'Poção']
#dano_arqueiro = [10, 20, 0, 45, 50]
#
#Habilidades_Arqueiro = {'Flecha Perfurante' : 10, 'Flecha Envenenada': 20, 'Mira Certeira' : 0, 'Chuva de Flechas' : 45, #'Poção' : 50}
#
#Paladino = ['Investida', 'Escudo Divino',
#            'Ira', 'Machadada', 'Poção']
#dano_paladino = [10, 0, 0, 45, 50]
#
#Habilidades_Paladino = {'Investida' : 10, 'Escudo Divino': 0, 'Ira' : 0, 'Machadada' : 45, 'Poção' : 50}
#
#Mago = ['Bola de Fogo', 'Raio de Gelo',
#        'Trovão', 'Jato de Água', 'Poção']
#dano_mago = [10, 30, 40, 20, 50]
#
#Habilidades_Mago = {'Bola de Fogo' : 10, 'Raio de Gelo': 30, 'Trovão' : 40, 'Jato de Água' : 20, 'Poção' : 50}
#
#Assassino = ['Ataque Furtivo', 'Golpe Venenoso',
#             'Apunhalada', 'Lançamento de Adaga',
#             'Poção']
#dano_assassino = [10, 20, 40, 10, 50]
#
#Habilidades_Assasino = {'Ataque Furtivo' : 10, 'Golpe Venenoso': 20, 'Apunhalada' : 40, 'Lançamento de Adaga' : 10, 'Poção' : 50}

yago = Player()

yago.mostrar_vida()
yago.classe = "Arqueiro"
#yago.nome_personagem("Yago")
yago.nome = "Yago"
yago.mostrar_atributos()

douglas = Arqueiro()
douglas.mostrar_atributos()
douglas.ataque(1)
douglas.mostrar_atributos()

#for j in range(1, 3):
    #nome = str(input(f'Digite o nome do jogador {j}: ')).strip().title()
    #esc = int(input(f'''[ 1 ] - Arqueiro
#[ 2 ] - Paladino
#[ 3 ] - Mago
#[ 4 ] - Assasino
#Escolha a classe do jogador {j}: '''))

def criando_jogador(jogador : int):
        esc = int(input(f'''[ 1 ] - Arqueiro
[ 2 ] - Paladino
[ 3 ] - Mago
[ 4 ] - Assasino
Escolha a classe do jogador {jogador}: '''))
        match esc:
                case 1:
                        return Arqueiro()
                case 2:
                        return Paladino()
                case 3:
                        return Mago()
                case 4:
                        return Assasino()
                case other:
                        return None

lucas = criando_jogador(1)
lucas.nome = str(input("Qual o seu nome? "))
lucas.mostrar_atributos()