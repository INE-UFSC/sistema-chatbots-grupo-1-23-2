from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots=lista_bots
        if not all(isinstance(bot, Bot) for bot in self.__lista_bots):
            raise ValueError("A lista deve conter apenas Bots.")
        self.__bot = None
    
    def boas_vindas(self):
        return f"Olá, esse é o sistema de chatbots da empresa {self.__empresa}\n"
        

    def mostra_menu(self):
        resposta = "Os chat bots disponíveis no momento são:\n"
        for i in range(len(self.__lista_bots)):
            resposta += f"{i} - Bot: {self.__lista_bots[i].nome} - Mensagem de apresentação: {self.__lista_bots[i].apresentacao()}\n"
        return resposta
            
    def escolhe_bot(self):
        bot = int(input("Digite o número do chat bot desejado: "))
        self.__bot = self.__lista_bots[bot]
        return f"\n--> {self.__bot.nome} diz: {self.__bot.boas_vindas()}\n"

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()
       
    def le_envia_comando(self):
        comando = input("Digite o comando desejado (ou -1 para fechar o programa e sair): ")
        return f"--> {self.__bot.nome} diz: {self.__bot.executa_comando(comando)}\n"
        
    def inicio(self):
        print(self.boas_vindas())
        print(self.mostra_menu())
        print(self.escolhe_bot())
        
        while True:
            print(self.mostra_comandos_bot())
            print(self.le_envia_comando())
            if self.__bot.sair == True:
                break
