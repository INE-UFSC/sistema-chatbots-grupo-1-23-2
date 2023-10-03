from Bot import Bot
from SistemaChatBot import SistemaChatBot as scb

class BotMaker:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
    
    @property
    def sistema(self):
        return self.__sistema
        
    def addbot(self, nome, apresentacao, boas_vindas, despedida):
        self.sistema.lista_bots.append(Bot(nome, apresentacao, boas_vindas, despedida))
    
    def removebot(self, bot: Bot):
        if bot in self.sistema.lista_bots:
            self.sistema.lista_bots.remove(bot)
        else:
            raise ValueError("Não é um bot válido ou não está na lista de bots")