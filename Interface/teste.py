import PySimpleGUI as sg

class MenuInicialView:
    def __init__(self):
        self.__container = []
    
    def tela_inicial(self):
        self.__container = [
            [sg.Text(f'Bem vindo ao ChatBot da empresa TESTE!', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, selecione uma opção:', font=('Montserrat', 18))],
            [sg.Text('', size=(15, 1))],
            [sg.Button('BotMaker', size=(25, 1), pad=(5, 0)), sg.Button('Chat', size=(25, 1), pad=(5, 0))],
        ]
        self.__window = sg.Window(
            "Menu Inicial", self.__container, font=("Montserrat", 14))
    
    def tela_selecao(self):
        self.__container = [
            [sg.Text('BotMaker selecionado!', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, selecione uma opção:', font=('Montserrat', 16))],
            [sg.Button('Criar', size=(12, 1), pad=(20, 0)), sg.Button('Editar', size=(12, 1), pad=(20, 15))],
        ]
        self.__window = sg.Window(
            "Selecionador do BotMaker", self.__container, font=("Montserrat", 14))
        
    def tela_criacao(self, perg_resp: list = [1, 2, "banana"]):
        string = "batata com batata, rodrigo rei!\n\ntom nada."
        self.__container = [
            [sg.Text('Sistema ChatBot EMPRESA', font=('Montserrat', 24, "bold"))],
            [sg.Text('Você está conversando com o bot YODA, seja gentil!', font=('Montserrat', 16))],
            [sg.Multiline(string, size=(72, 20), font=('Montserrat', 14), autoscroll=True, disabled=True, pad=(10, 18))],
            [sg.Text(' Selecione sua pergunta:', font=('Montserrat', 16)), sg.Combo(["bot.perguntas_respostas batabtatantbatejvgg ghjghejhge gjeghgj"], size=(40, 1), readonly=True), sg.Button('Enviar', size=(10, 1))]
            ]
        
        self.__window = sg.Window(
            "Criador de Bots", self.__container, font=("Montserrat", 14))

    
    def le_eventos(self):
        return self.__window.read()
    
menu = MenuInicialView()
menu.tela_criacao()

event, values = menu.le_eventos()
    
