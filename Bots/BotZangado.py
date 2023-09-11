from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)
    
    def apresentacao(self):
        return f"Grrrrrr. Meu nome é {self.__nome} e eu te odeio!"
    
    def executa_comando(self,cmd):
        if cmd == "1":
            nome_variavel = self.__comandos[cmd][1]
        elif cmd==2:
            self.apresentacao()
        elif cmd==3:
            self.quero_um_conselho()
        elif cmd==-1:
            self.despedida()
            exit()
    
    def quero_um_conselho(self):
        pass
    
    def boas_vindas(self):
        
    
    def despedida(self):
        #msg despedida 
        pass