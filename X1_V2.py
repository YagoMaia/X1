from classes import *


p1 = criando_jogador(1)
p2 = criando_jogador(2)

while(p1.vida and p2.vida > 0):
    #p1.mostrar_atributos()
    #p2.mostrar_atributos()
    Players(p1,p2)
    p1.mostrar_ataque()
    escolha_1 = int(input("Escolha o ataque: "))
    ataque_1 = p1.ataque(escolha_1, p2.status)
    p2.atualizar(ataque_1)
    Players(p1,p2)
    p2.mostrar_ataque()
    escolha_2 = int(input("Escolha o ataque: "))
    ataque_2 = p2.ataque(escolha_2, p1.status)
    p1.atualizar(ataque_2)
