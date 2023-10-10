import PySimpleGUI as sg
from SistemaChatBot import SistemaChatBot
from Interface.InterfaceBotMaker import InterfaceBotMaker
from Interface.InterfaceChat import InterfaceChat
from Interface.InterfaceMenuInicial import InterfaceMenuInicial

class Controle:
    def __init__(self, nome_empresa: str):
        self.__sistema = SistemaChatBot(nome_empresa, "bots.pkl")
        self.__viewmenu = InterfaceMenuInicial(self.sistema)
        self.__viewbotmaker = InterfaceBotMaker(self.sistema)
        self.__viewchat = InterfaceChat(self.sistema)
        
    @property
    def sistema(self):
        return self.__sistema
    
    @property
    def viewmenu(self):
        return self.__viewmenu
    
    @property
    def viewbotmaker(self):
        return self.__viewbotmaker

    @property
    def viewchat(self):
        return self.__viewchat

    def inicio(self):
        self.menuprincipal()
    
    def menuprincipal(self):
        self.viewmenu.tela_inicial()
        
        while True:
            evento, valores = self.viewmenu.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.__view_selecao.fim()
                return

            if evento == 'BotMaker':
                self.botmaker()
                
            elif evento == "Chat":
                pass
                
    def botmaker(self):
        self.viewbotmaker.tela_selecao_inicial()

        while True:
            evento, valores = self.viewbotmaker.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.__view_selecao.fim()
                return

            if evento == 'Editar':
                self.botmaker()
                
            elif evento == "Chat":
                pass