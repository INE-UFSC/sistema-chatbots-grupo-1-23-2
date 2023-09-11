from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self,nome):
        self.__comandos = {}

    @abstractmethod
    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @abstractmethod
    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self,):
        pass