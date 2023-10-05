from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = lista_bots
        if not all(isinstance(bot, Bot) for bot in self.__lista_bots):
            raise ValueError("A lista deve conter apenas Bots.")
        self.__bot = None
        
    @property
    def lista_bots(self):
        return self.__lista_bots
    