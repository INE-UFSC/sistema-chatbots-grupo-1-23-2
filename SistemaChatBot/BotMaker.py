from Bots.Bot import Bot
from Bots.PerguntaResposta import PerguntaResposta
from SistemaChatBot import SistemaChatBot as scb

class BotMaker:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
        self.__perguntas_respostas = []
    
    @property
    def sistema(self):
        return self.__sistema
        
    def add_bot(self, nome, apresentacao, boas_vindas, despedida):
        if self.__nome in [bot.nome for bot in self.sistema.lista_bots]:
            raise ValueError("Já existe um bot com esse nome")
        elif nome == "" or apresentacao == "" or boas_vindas == "" or despedida == "" or self.__perguntas_respostas == []:
            raise ValueError("Por favor, preencha todos os dados do bot")
        else:
            self.sistema.lista_bots.append(Bot(nome, apresentacao, boas_vindas, despedida, self.__perguntas_respostas))
    
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