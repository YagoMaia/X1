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
    
    def atualizar_vida(self, dano : int):
        self.vida -= dano
        return self.vida

    def mostrar_vida(self):
        print(f"{self.status_vida()}{self.vida}{nada}")

    
    def mostrar_atributos(self):
        print(f'Vida: {self.vida}')
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'Habilidades: {self.habilidades_clase}')
        self.mostrar_status()
    
    def usar_pocao(self):
        self.vida += 50
        return self.vida

class Arqueiro(Player):

    def __init__(self):
        self.classe = "Arqueiro"
        self.habilidades_clase = [{'Flecha Perfurante': '10'}, {'Flecha Envenenada': '20'}, {'Mira Certeira': '0'}, {'Chuva de Flechas': '45'}, {'Poção': '50'}]


    def critico(self, dano : int):
        if self.status == 'Mirando':
            chance_crit = randint(10, 20)
        else:
            chance_crit = randint(0, 20)
        self.status = 'Normal'
        if(chance_crit == 20): 
            print(f"{vermelho}CRÍTICO{nada}")
            return dano * 2 
        return dano

    def ataque(self, escolha : int):
        if(escolha > len(self.habilidades_clase)):
            print("Escolha Indisponível")
            return 0
        habilidade_usada = self.habilidades_clase[escolha]
        for key, value in habilidade_usada.items():
            match key:
                case 'Poção':
                    return self.usar_pocao()
                case 'Mira Certeira':
                    self.status = 'Mirando'
                    return self.status
                case other:
                    return self.critico(value)

 
class Paladino(Player):
    def __init__(self):
        self.classe = "Paladino"
        self.habilidades_clase = [{'Investida' : 10}, {'Escudo Divino': 0}, {'Ira' : 0}, {'Machadada' : 45}, {'Poção' : 50}]

class Assasino(Player):
    def __init__(self):
        self.classe = "Assasino"
        self.habilidades_clase = [{'Ataque Furtivo': '10'}, {'Golpe Venenoso': '20'}, {'Apunhalada': '40'}, {'Lançamento de Adaga': '10'}, {'Poção': '50'}]

class Mago(Player):
    def __init__(self):
        self.classe = "Mago"
        self.habilidades_clase = [{'Bola de Fogo' : 10}, {'Raio de Gelo': 30}, {'Trovão' : 40}, {'Jato de Água' : 20}, {'Poção' : 50}]

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