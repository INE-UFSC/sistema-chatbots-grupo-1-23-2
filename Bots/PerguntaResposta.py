class PerguntaResposta:
    def __init__(self, pergunta: str, resposta: str):
        self.__pergunta = pergunta
        self.__resposta = resposta
    
    @property
    def pergunta(self):
        return self.__pergunta
    
    @property
    def resposta(self):
        return self.__resposta
    
    def __str__(self):
        return self.pergunta