import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot
from Interface.InterfaceBotMaker import BotMakerView
from Interface.InterfaceChat import InterfaceChat
from Interface.InterfaceMenuInicial import MenuInicialView
from SistemaChatBot.BotMaker import BotMaker

class Controle:
    def __init__(self, nome_empresa: str):
        self.__sistema = SistemaChatBot(nome_empresa, "bots.pkl") # sistema que gerencia os bots
        self.__viewmenu = MenuInicialView(self.sistema) # interfaces do menu inicial
        self.__botmaker = BotMaker(self.sistema) # classe gerencia o botmaker
        self.__viewbotmaker = BotMakerView(self.sistema, self.__botmaker) # interfaces do botmaker
        self.__viewchat = InterfaceChat(self.sistema) # interfaces do chat
        self.__window = None # janela atual
        
    # getters 
        
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
    
    @property
    def botmaker(self):
        return self.__botmaker
    
    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, window):
        self.__window = window
    

# organizacao de janelas

    def inicio(self):  # funcao que inicia o programa
        self.window = self.viewmenu.tela_inicial()
        self.menuprincipal()
    
    def menuprincipal(self): # menu que inicia tudo
        self.window.close()
        self.window = self.viewmenu.tela_inicial()
        
        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break

            if evento == 'BotMaker':
                self.botmaker_selecao()
                
            elif evento == "Chat":
                self.selecao_bot()

    def selecao_bot(self): # janela em que o usuário seleciona com qual bot irá conversar
        self.window.close()
        self.window = self.viewchat.tela_selecao_bot()

        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break

            elif evento == "Voltar":
                self.window.close
                self.menuprincipal() 

            elif evento == "Ok":
                if valor["bot"] == "":
                    sg.popup("Por favor selecione um bot!")
                else:
                    self.tela_chatbot(valor["bot"], "teste")

    def tela_chatbot(self, bot, mensagem):
        self.window.close()
        self.window = self.viewchat.tela_chat(bot, mensagem)
        
        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break

            elif evento == 'Voltar':
                self.selecao_bot()

                
    def botmaker_selecao(self): # janela em que seleciona se deve criar ou editar um bot
        self.window.close()
        self.window = self.viewbotmaker.tela_selecao_inicial()
            
        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break

            elif evento == 'Criar':
                self.botmaker_criar()
                
            elif evento == 'Editar':
                if self.sistema.lista_bots == []:
                    sg.popup("Não há bots para editar!")
                else:
                    pass
                
            elif evento == 'Voltar':
                self.menuprincipal()
                
            
    def botmaker_criar(self): # janela em que cria um bot
        self.window.close()
        self.window = self.viewbotmaker.tela_criacao()
        
        while True:

            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break
            
            elif evento == 'Editar': # botao para editar uma pergunta existente
                self.atualizar_valores(valor)
                if valor["pergunta_resposta"] == "":
                    sg.popup("Por favor, selecione uma pergunta!")
                else:
                    self.editar_pergunta(valor["pergunta_resposta"])
                
            elif evento == 'Novo': # criar nova pergunta
                self.atualizar_valores(valor)
                self.criar_pergunta()

            elif evento == 'Criar':
                try:
                    self.botmaker.cria_bot(valor["nome"], valor["apresentacao"], valor["boas_vindas"], valor["despedida"])
                    sg.popup(f"O Bot {valor['nome']} foi criado com sucesso!")
                    self.menuprincipal()
                except ValueError as e:
                    sg.popup(e)
                
            
            elif evento == 'Voltar':
                self.botmaker.clean()
                self.botmaker_selecao()
        
    def editar_pergunta(self, pergunta): # janela em que edita uma pergunta existente
        self.window.close()
        self.window = self.viewbotmaker.tela_editar_pergunta_resposta(pergunta)
        
        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break
            
            elif evento == 'Salvar':
                if valor["pergunta"] == "" or valor["resposta"] == "": # verifica se existem valores vazios
                    sg.popup("Por favor, não deixe espaços vazios!")
                else: # edita a classe pergunta com valores novos
                    self.botmaker.editar_pergunta_resposta(pergunta, valor["pergunta"], valor["resposta"])
                    self.botmaker_criar() # volta pra tela de criacao de bot
            
            elif evento == 'Voltar':
                self.botmaker_criar()
                    
    def criar_pergunta(self): # cria uma nova pergunta
        self.window.close()
        self.window = self.viewbotmaker.tela_criar_pergunta_resposta()
    
        while True:
            evento, valor = self.window.read()

            if evento == sg.WINDOW_CLOSED:
                self.window.close()
                break
            
            elif evento == 'Salvar': # verifica se existem valores vazios
                if valor["pergunta"] == "" or valor["resposta"] == "":
                    sg.popup("Por favor, não deixe espaços vazios!")
                else:
                    self.botmaker.add_pergunta_resposta(valor["pergunta"], valor["resposta"])
                    self.botmaker_criar()
                    
            elif evento == 'Voltar':
                self.botmaker_criar()
                    
    def atualizar_valores(self, valor): # atualiza os valores da tela de criacao de bot
        dicionario = {"nome": valor["nome"], "apresentacao": valor["apresentacao"], "boas_vindas": valor["boas_vindas"], "despedida": valor["despedida"]}
        self.botmaker.valores_padrao = dicionario