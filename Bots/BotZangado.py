from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {"1": ["1 - Bom dia", self.boas_vindas()]}
    
    def apresentacao(self):
        pass
 
    def mostra_comandos(self):
        string = ""
        for i in dic:
            string += f"{i[0]}\n"
        return "1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho"
        
    
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