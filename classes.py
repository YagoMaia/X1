from random import randint

nada = "\033[m"
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'


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
    
    def atualizar_vida(self, dano : int):
        if self.status == 'Protegido':
            self.vida -= dano/2
        else: 
            self.vida -= dano
        return self.vida
        
    def atualizar_vida_status(self, ret : dict):
        for stat, dano in ret.items():
            if self.status == 'Protegido':
                self.vida -= dano/2
            else: 
                self.vida -= dano
            if stat:
                self.status = stat
            return {self.status : self.vida}

    def atualizar(self, dict : dict):
        for stat, dano in dict.items():
            self.atualizar_vida(dano)
            self.atualizar_status(stat)

    def atualizar_status(self, new_stat : str | None = None):
        if(new_stat != None):
            self.status = new_stat
        return self.status

    def mostrar_vida(self):
        print(f"{self.status_vida()}{self.vida}{nada}")

    def mostrar_atributos(self):
        #print(f'Vida: {self.status_vida()}{self.vida}{nada}')
        #print(f'Nome: {self.nome}')
        #print(f'Classe: {self.classe}')
        #print(f'Habilidades: {self.habilidades_clase}')
        print('-=' * 20)
        print(f"{self.nome}: {self.status_vida()}{self.vida}{nada} Pontos de Vida")
        self.mostrar_status()
        print('-=' * 20)
        #self.mostrar_status()

    def usar_pocao(self):
        self.vida += 50
        return self.vida

    def mostrar_ataque(self):
        print("="*45)
        print(f"Habilidades disponíveis para {self.nome}:")
        for a in range(0, len(self.habilidades_clase)):
            for k, v in self.habilidades_clase[a].items():
                print(f"[ {a} ] - {k}")


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
            return {None:dano*2}
        return {None:dano}

    def ataque(self, escolha: int):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return 0
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            match key:
                case 'Poção':
                    self.usar_pocao()
                    return {None:0}
                case 'Mira Certeira':
                    self.status = 'Mirando'
                    return {None:0}
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
            return dano*2
        return dano

    def ataque(self, escolha: int):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return 0
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            match key:
                case 'Poção':
                    self.usar_pocao()
                    return 0
                case 'Ira':
                    self.status = 'Ira'
                    self.cont_1 = 0
                    return 0
                case 'Escudo Divino':
                    self.status = 'Protegido'
                    self.cont_1 = 0
                    return 0
                case other:
                    return self.atacar(value)


class Assasino(Player):
    def __init__(self):
        self.classe = "Assasino"
        self.habilidades_clase = [{'Ataque Furtivo': 10}, {'Golpe Venenoso': 20}, {
            'Apunhalada': 40}, {'Lançamento de Adaga': 10}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()

    def envenenar(self, dano : int):
        chance_veneno = randint(20,20)
        new_status = None
        if(chance_veneno == 20):
            new_status = 'Envenenado'
            return {new_status:dano * 2}
        return {new_status:dano}


    def ataque(self, escolha: int):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return 0
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            match key:
                case 'Poção':
                    self.usar_pocao()
                    return 0
                case 'Mira Certeira':
                    self.status = 'Mirando'
                    return 0
                case other:
                    return self.envenenar(value)


class Mago(Player):
    def __init__(self):
        self.classe = "Mago"
        self.habilidades_clase = [{'Bola de Fogo': 10}, {'Raio de Gelo': 30}, {
            'Trovão': 40}, {'Jato de Água': 20}, {'Poção': 50}]
        self.nome = input("Qual seu nome? ").title()

    def ataque(self, escolha: int):
        if (escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return 0
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            match key:
                case 'Poção':
                    self.usar_pocao()
                    return 0
                case 'Mira Certeira':
                    self.status = 'Mirando'
                    return 0
                case other:
                    return self.critico(value)


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