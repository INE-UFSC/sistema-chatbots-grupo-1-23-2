class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id: int, mensagem: str, respostas: list):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    # get id
    @property
    def id(self):
        return self.__id

    # get mensagem
    @property
    def mensagem(self):
        return self.__mensagem
    
    #get respostas
    @property
    def respostas(self):
        return self.__respostas
    

    
    

    # retorna uma resposta aleatória
    def getRandomResposta(self):

    # adiciona resposta
    def addResposta(self, resposta):
    
    # remove resposta (opcional)
    def delResposta(self, resposta):
