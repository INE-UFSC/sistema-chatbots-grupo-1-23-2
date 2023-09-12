from Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome, comandos):
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
            return 'Até outra hora! Espero te ver mais uma vez!'
    
    def quero_um_conselho(self):
        return 'Veja a vida de forma mais positiva!'

    def despedida(self):
        return 'Até outra hora! Espero te ver mais uma vez!'

        