import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot
from Interface.InterfaceBotMaker import BotMakerView
from Interface.InterfaceChat import InterfaceChat
from Interface.InterfaceMenuInicial import MenuInicialView
from SistemaChatBot.BotMaker import BotMaker

class Controle:
    def __init__(self, nome_empresa: str):
        self.__sistema = SistemaChatBot(nome_empresa, "bots.pkl")
        self.__viewmenu = MenuInicialView(self.sistema)
        self.__viewbotmaker = BotMakerView(self.sistema)
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
        self.viewmenu.tela_inicial()
        self.menuprincipal()
    
    def menuprincipal(self):
        while True:
            evento, valor = self.viewmenu.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.viewmenu.close()
                return

            if evento == 'BotMaker':
                self.viewmenu.close()
                self.viewbotmaker.tela_selecao_inicial()
                self.botmaker_selecao()
                
            elif evento == "Chat":
                pass
                
    def botmaker_selecao(self):       
        while True:
            evento, valor = self.viewbotmaker.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.viewbotmaker.close()
                return

            if evento == 'Criar':
                self.viewbotmaker.close()
                self.botcriar = BotMaker(self.sistema)
                self.botmaker_criar()
                
            elif evento == 'Editar':
                if self.sistema.lista_bots == []:
                    sg.popup("Não há bots para editar!")
                else:
                    self.viewbotmaker.close()
                    self.botmaker_editar()
                
            
    def botmaker_criar(self):
        while True:
            self.viewbotmaker.tela_criacao(self.botcriar.perguntas_respostas)
            evento, valor = self.viewbotmaker.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.viewbotmaker.close()
                return

            if evento == 'Editar':
                self.botcriar.add_pergunta_resposta("oi", "tchau")
                if valor[0] == "":
                    sg.popup("Por favor, selecione uma pergunta!")
                else:
                    self.viewbotmaker.tela_editar_pergunta_resposta(valor[0])
                    self.editar_pergunta(valor[0])
                
            elif evento == 'Novo':
                if self.sistema.lista_bots == []:
                    sg.popup("Não há bots para editar!")
                else:
                    self.viewbotmaker.close()
                    self.botmaker_editar()

            elif evento == 'Criar':
                pass
            
            elif evento == 'Voltar':
                pass
        
    def editar_pergunta(self, pergunta):
        while True:
            evento, valor = self.viewbotmaker.le_eventos()

            if evento == 'Salvar':
                if valor["pergunta"] == "" or valor["resposta"] == "":
                    sg.popup("Por favor, não deixe espaços vazios!")
                else:
                    self.botcriar.editar_pergunta_resposta(pergunta, valor["pergunta"], valor["resposta"])
                    self.viewbotmaker.close()
                    self.viewbotmaker.tela_criacao(self.botcriar.perguntas_respostas)
                    self.botmaker_criar()