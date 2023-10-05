from Bots.Bot import Bot
from Bots.PerguntaResposta import PerguntaResposta
from SistemaChatBot import SistemaChatBot as scb

class BotMaker:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
        self.__nome = None
        self.__perguntas_respostas = []
        self.__apresentacao = None
        self.__boas_vindas = None
        self.__despedida = None
    
    @property
    def sistema(self):
        return self.__sistema
        
    def add_bot(self):
        if self.__nome in [bot.nome for bot in self.sistema.lista_bots]:
            raise ValueError("Já existe um bot com esse nome")
        elif self.__nome == None or self.__apresentacao == None or self.__boas_vindas == None or self.__despedida == None or self.__perguntas_respostas == []:
            raise ValueError("Por favor, preencha todos os dados do bot")
        else:
            self.sistema.lista_bots.append(Bot(self.__nome, self.__apresentacao, self.__boas_vindas, self.__despedida, self.__perguntas_respostas))
    
    def remove_bot(self, bot: Bot):
        if bot in self.sistema.lista_bots:
            self.sistema.lista_bots.remove(bot)
        else:
            raise ValueError("Não é um bot válido ou não está na lista de bots")
        
    def add_pergunta_resposta(self, pergunta, resposta):
        self.__perguntas_respostas.append(PerguntaResposta(pergunta, resposta))
        
    def remove_pergunta_resposta(self, pergunta_resposta: PerguntaResposta):
        if pergunta_resposta in self.__perguntas_respostas:
            self.__perguntas_respostas.remove(pergunta_resposta)
        else:
            raise ValueError("Não é uma pergunta e resposta válida ou não está na lista de perguntas e respostas")