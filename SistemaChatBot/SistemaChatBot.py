from Bots.Bot import Bot
import pickle

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots, arquivo):
        self.__empresa = nomeEmpresa
        self.__arquivo = arquivo
        self.__lista_bots = lista_bots
        if not all(isinstance(bot, Bot) for bot in self.__lista_bots):
            raise ValueError("A lista deve conter apenas Bots.")
        self.__bot = None
        
    @property
    def lista_bots(self):
        return self.__lista_bots
    
    def __dump(self):
        f = open(self.__arquivo, 'wb')
        pickle.dump(self.__listabots, f)
        f.close()
        
    def __load(self):
        f = open(self.__arquivo, 'rb')
        self.__listabots = pickle.load(f)
        f.close()
    
    def addbot(self, bot):                              
        if not bot in self.lista_bots:
            self.lista_bots.append(bot)
            self.__dump()
        else:
            raise ValueError("Bot já está na lista de bots")
    
    def removebot(self, bot):
        if bot in self.lista_bots:
            self.lista_bots.remove(bot)
            self.__dump()
        else:
            raise ValueError("Não é um bot válido ou não está na lista de bots")