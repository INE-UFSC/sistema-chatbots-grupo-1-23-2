from Bots.Bot import Bot

class BotGago(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome       
        self.comandos = {'1' : 'Bo-bo-bom dia!', '2': 'Se um estra-tra-tra-tranho o-ofe-fe-ferecer drogas, a-a-aceite. Drogas são caras!', '3': 'Vai cho-chover ca-ca-canivetes', '4' : self.despedida() }

    def apresentacao(self):
        return 'O-o-olá, me-meu nome-me-me-me-me é Gaguinho, espe-pe-pe-ro po-de-der aju-ju-ju-ju-ju-ju-dar!'
 
    def mostra_comandos(self):
        return '1 - Bom dia\n2 - Preciso de um conselho\n3 - Previsão do tempo\n4 - Adeus\n'        

    def executa_comando(self,cmd):
        if cmd == "-1":
            return self.comandos["4"]
        return self.comandos[cmd]

    def boas_vindas(self):
        return 'Obriga-do-do-do-do-do por me es-co-co-co-lher!'

    def despedida(self):
        return 'Po-po-por hoje-je é só, pe-pe-pe-pessoal!'