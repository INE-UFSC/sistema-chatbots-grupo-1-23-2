import PySimpleGUI as sg

class MenuInicialView:
    def __init__(self):
        self.__container = []
        self.__window = sg.Window(
            "Menu Inicial", self.__container, font=("Montserrat", 14))
    
    def tela_inicial(self):
        self.__container = [
            [sg.Text(f'Bem vindo ao ChatBot da empresa TESTE!', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, selecione uma opção:', font=('Montserrat', 18))],
            [sg.Text('', size=(15, 1))],
            [sg.Button('BotMaker', size=(25, 1), pad=(5, 0)), sg.Button('Chat', size=(25, 1), pad=(5, 0))],
        ]
        self.__window = sg.Window(
            "Menu Inicial", self.__container, font=("Montserrat", 14))
    
    def le_eventos(self):
        return self.__window.read()
    
menu = MenuInicialView()
menu.tela_inicial()
event, values = menu.le_eventos()
