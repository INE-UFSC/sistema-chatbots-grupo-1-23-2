from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {"1": "Bom dia", "2": "Qual o seu nome?", "3": "Quero um conselho", "4": "Adeus"}
        self.__sair = False
    
    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos
        
    @property
    def sair(self):
        return self.__sair

    @sair.setter
    def sair(self, sair):
        self.__sair = sair

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def mostra_comandos(self):
        resposta = ""
        for chaves in self.__comandos.keys():
            resposta += f"{chaves} - {self.__comandos[chaves]}\n"
        return resposta

    @abstractmethod
    def apresentacao(self):
        pass
    
    @abstractmethod
    def boas_vindas(self):
        pass

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def despedida(self):
        pass