from random import randint

class Player():

    def __init__(self):
        self.vida = 50
        self.dano = randint(2,9)
        self.prot = 5
        self.capacete = {None:0}
        self.peitoral = {None:0}
        self.calça = {None:0}
        self.bota = {None:0}
        self.luva = {None:0}

class Esqueleto():

    def __init__(self):
        self.vida = 20
        self.dano = randint(2,9)
        self.prot = 5
        self.drops_armas = [{"Espada Velha" : 10}, {"Bastão" : 5}]
        self.drop_armaduras = [{"Armadura Velha":3}, {"Bota de Malha" : 2}, {"Luva Velha" : 1}]