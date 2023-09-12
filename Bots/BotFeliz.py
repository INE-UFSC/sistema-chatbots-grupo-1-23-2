from Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)
    
    def apresentacao(self):
        return f'Olá! Meu nomé é {self.__nome}, como você está?'
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return 'Bem-vindo ao chat! Espero que esteja bem'
        elif cmd== "2":
            return f'Olá! Meu nomé é {self.__nome}, como você está?'
        elif cmd== "3":
            return 'Veja a vida de forma mais positiva!'        
        elif cmd=="-1" or cmd == "4":
            self.despedida()

    def despedida(self):
        self.sair = True
        return 'Até outra hora! Espero te ver mais uma vez!'

        