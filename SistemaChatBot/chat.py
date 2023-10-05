from Bots.Bot import Bot
from Bots.PerguntaResposta import PerguntaResposta


class Chat:
    def __init__(self, bot: Bot):
        self.__bot = bot
    
    @property
    def bot(self):
        return self.__bot

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

