from Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome)
    
    def apresentacao(self):
        return f'Olá! Meu nomé é {self.__nome}, como você está?'
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return self.__comandos[cmd][1]
        elif cmd==2:
            self.apresentacao()
        elif cmd==3:
            self.quero_um_conselho()
        elif cmd==-1:
            self.despedida()
            exit()
    
    def quero_um_conselho(self):
        return 'Veja a vida de forma mais positiva!'
    
    def boas_vindas(self):
        return 'Bem-vindo ao chat! Espero que esteja bem'
    
    def despedida(self):
        return 'Até outra hora! Espero te ver mais uma vez!'