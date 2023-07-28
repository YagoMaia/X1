from random import randint
from colors import *
from math import ceil


#Classe Base
class Player:
    vida = 500
    nome = "Player"
    status = "Normal"
    habilidades_clase = []
    classe = "Sem Classe"

    def status_vida(self):
        if 550 >= self.vida > 250:
            return verde
        elif 250 >= self.vida > 135:
            return amarelo
        return vermelho

    def mostrar_status(self):
        match self.status:
            case 'Envenenado':
                print(f"Status: {verde}{self.status}{nada}")
            case 'Mirando':
                print(f"Status: {vermelho}{self.status}{nada}")
            case 'Normal':
                print(f"Status: {ciano}{self.status}{nada}")
            case 'Protegido':
                print(f"Status: {azul}{self.status}{nada}")
            case 'Ira':
                print(f"Status: {vermelho}{self.status}{nada}")
            case 'Queimando':
                 print(f"Status: {vermelho}{self.status}{nada}")
            case 'Molhado':
                 print(f"Status: {ciano}{self.status}{nada}")
            case 'Congelado':
                 print(f"Status: {azul}{self.status}{nada}")
    
    def atualizar_vida(self, dano : int):
        if self.status == 'Protegido':
            self.vida -= ceil(dano/2)
        elif self.status == 'Envenenado':
            self.vida -= dano
            self.vida -= ceil((1/100)*self.vida)
        else: 
            self.vida -= dano
        return self.vida

    def atualizar_status(self, new_stat : str | None = None):
        if(new_stat != None):
            self.status = new_stat
        return self.status
    
    def atualizar(self, dict : dict):
        for stat, dano in dict.items():
            self.atualizar_vida(dano)
            self.atualizar_status(stat)


    def mostrar_vida(self):
        print(f"{self.status_vida()}{self.vida}{nada}")

    def mostrar_atributos(self):
        print('-=' * 20)
        print(f"{self.nome}: {self.status_vida()}{self.vida}{nada} Pontos de Vida")
        self.mostrar_status()
        print('-=' * 20)

    def usar_pocao(self):
        self.vida += 100
        self.status = 'Normal'
        print("Vida Recuperada em 100")
        return {None:0}

    def mostrar_ataque(self):
        print("="*40)
        print(f"Habilidades disponíveis para {self.nome}:")
        for a in range(0, len(self.habilidades_clase)):
            for k, v in self.habilidades_clase[a].items():
                print(f"[ {a} ] - {k}")

#Classes do PVP
class Arqueiro(Player):

    def __init__(self):
        self.classe = "Arqueiro"
        self.habilidades_clase = [{'Flecha Perfurante': 10}, {'Flecha Envenenada': 20}, {
            'Mira Certeira': 0}, {'Chuva de Flechas': 45}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()

    def critico(self, dano: int):
        if self.status == 'Mirando':
            chance_crit = randint(10, 20)
        else:
            chance_crit = randint(0, 20)
        if self.status == 'Mirando':
            self.status = 'Normal'
        if (chance_crit == 20):
            print(f"{vermelho}CRÍTICO{nada}")
            print(f"Dano Causado: {dano*2}")
            return {None:dano*2}
        return {None:dano}

    def envenenar(self, dano : int):
        chance_veneno = randint(0,20)
        new_status = None
        if(chance_veneno == 20):
            new_status = 'Envenenado'
            print("Você conseguiu envenenar seu inimigo")
        print(f"Dano Causado: {dano}")
        return {new_status:dano}

    def ataque(self, escolha: int, stat_adv : str | None = None):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return {None:0}
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            print(f"Habilidade usada : {key}")
            match key:
                case 'Poção':
                    return self.usar_pocao()
                case 'Mira Certeira':
                    self.status = 'Mirando'
                    return {None:0}
                case 'Flecha Envenenada':
                    return self.envenenar(value)
                case other:
                    return self.critico(value)


class Paladino(Player):
    def __init__(self):
        self.classe = "Paladino"
        self.habilidades_clase = [{'Investida': 10}, {'Escudo Divino': 0}, {
            'Ira': 0}, {'Machadada': 45}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()
        self.cont_1 = 0

    def atacar(self, dano: int):
        if (self.cont_1 == 3):
            self.status = 'Normal'
        self.cont_1 += 1
        if self.status == 'Ira':
            print(f"Dano Causado: {dano*2}")
            return {None:dano*2}
        print(f"Dano Causado: {dano}")
        return {None:dano}

    def ataque(self, escolha: int, stat_adv : str | None = None):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return {None:0}
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            print(f"Habilidade usada : {key}")
            match key:
                case 'Poção':
                    return self.usar_pocao()
                case 'Ira':
                    self.status = 'Ira'
                    self.cont_1 = 0
                    return {None:0}
                case 'Escudo Divino':
                    self.status = 'Protegido'
                    self.cont_1 = 0
                    return {None:0}
                case other:
                    return self.atacar(value)


class Assasino(Player):
    def __init__(self):
        self.classe = "Assasino"
        self.habilidades_clase = [{'Ataque Furtivo': 10}, {'Golpe Venenoso': 20}, {
            'Apunhalada': 40}, {'Lançamento de Adaga': 10}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()

    def envenenar(self, dano : int):
        chance_veneno = randint(0,20)
        new_status = None
        if(chance_veneno == 20):
            new_status = 'Envenenado'
            print("Você conseguiu envenenar seu inimigo")
            print(f"Dano Causado: {dano*2}")
            return {new_status:dano * 2}
        print(f"Dano Causado: {dano}")
        return {new_status:dano}

    def apunhalada(self, dano : int, stat_adv):
        if(stat_adv == 'Envenenado'):
            print(f"Dano Causado: {dano*2}")
            return {None:dano*2}
        print(f"Dano Causado: {dano}")
        return {None:dano}


    def ataque(self, escolha: int, stat_adv : str | None = None):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return {None:0}
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            print(f"Habilidade Usada: {key}")
            match key:
                case 'Poção':
                    return self.usar_pocao()
                case 'Apunhalada':
                    return self.apunhalada(value, stat_adv)
                case other:
                    return self.envenenar(value)


class Mago(Player):
    def __init__(self):
        self.classe = "Mago"
        self.habilidades_clase = [{'Bola de Fogo': 10}, {'Raio de Gelo': 30}, {
            'Trovão': 40}, {'Jato de Água': 20}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()

    def fogo(self, dano : int, stat_adv : str):
        chance_fogo = randint(20,20)
        print(f"Dano Causado: {dano}")
        if(chance_fogo == 20):
            if(stat_adv == 'Molhado'):
                print("Você evaporou a água do seu adversário")
                return {'Normal':dano}
            elif(stat_adv == 'Congelado'):
                print("Você derretou o gelo que adversário estava")
                return {"Molhado":dano}
            else:
                print("Você conseguiu queimar seu inimigo")
                return {"Queimando":dano}
        return {None:dano}
            
    def gelo(self, dano : int, stat_adv : str):
        chance_congelador = randint(20, 20)
        print(f"Dano Causado: {dano}")
        if(chance_congelador == 20):
            if(stat_adv == 'Queimando'):
                print("Misturando seu gelo com o fogo já existente, você deixa o inimigo molhado")
                return {'Molhado':dano}
            else:
                print("Você conseguiu congelar seu inimigo")
                return {"Congelado":dano}
        return {None:dano}

    def raio(self, dano : int, stat_adv : str):
        print("Você invoca o nome da Raio para te ajudar")
        if(stat_adv == 'Molhado'):
            print("O inimigo sofre um enorme descarga elétrica por estar molhado")
            print(f"Dano Causado: {dano*2}")
            return {'Normal':dano*2}
        print(f"Dano Causado: {dano}")
        return {None:dano}

    def agua(self, dano : int, stat_adv : str):
        print(f"Dano causado: {dano}")
        if(stat_adv == 'Queimando'):
            print("Você apaga o fogo do seu adversário")
            return {"Normal":dano}
        elif(stat_adv == 'Congelado'):
            return {None:dano}
        else:
            return {"Molhado":dano}

    def ataque(self, escolha: int, stat_adv : str | None = None):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return {None:0}
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            print(f"Habilidade usada : {key}")
            match key:
                case 'Poção':
                    self.usar_pocao()
                case 'Bola de Fogo':
                    return self.fogo(value, stat_adv)
                case 'Raio de Gelo':
                    return self.gelo(value, stat_adv)
                case 'Trovão':
                    return self.raio(value, stat_adv)
                case 'Jato de Água':
                    return self.agua(value, stat_adv)

def criando_jogador(jogador: int):
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

def Players(p1 : Player, p2 : Player):
    p1.mostrar_atributos()
    p2.mostrar_atributos()