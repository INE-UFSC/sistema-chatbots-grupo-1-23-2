from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def mostra_comandos(self):
        resposta = ""
        for i in range(len(self.__comandos)):
            resposta += f"{i} - {self.__comandos[i]}\n"
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