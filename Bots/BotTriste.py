from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        
    def apresentacao(self):
        return f'Grrrrrr. Meu nome é {self.__nome} e eu te odeio!'    
    
    def executa_comando(self,cmd):
        if cmd == "1":
           return "Bom
        elif cmd=="2":
            self.apresentacao()
        elif cmd=="3":
            self.quero_um_conselho()
        elif cmd=="4" or cmd=="-1":
            self.despedida()
            exit()
    
    def boas_vindas(self):
        return 
        
    
    def despedida(self):
        pass