from Bots.PerguntaResposta import PerguntaResposta


class Chat:
    def __init__(self, bot):
        self.__bot = bot
        self.__mensagem = ''
        
    @property
    def mensagem(self):
        return self.__mensagem
    
    @mensagem.setter
    def mensagem(self, mensagem):
        self.__mensagem = mensagem

    @property
    def bot(self):
        return self.__bot
    
    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    def apresentacao(self):
        return f"{self.bot.nome}: {self.bot.apresentacao}"

    def boas_vindas(self):
        return f"{self.bot.nome}: {self.bot.boas_vindas}"

    def despedida(self):
        return f"{self.bot.nome}: {self.bot.despedida}\n" + "-*- O chat foi encerrado -*-"

    def mostrar_pergunta(self):
        return self.bot.perguntas_respostas

    def mostrar_resposta(self, pergunta: PerguntaResposta):
        return f"{self.bot.nome}: {pergunta.resposta}"
    
    # fim