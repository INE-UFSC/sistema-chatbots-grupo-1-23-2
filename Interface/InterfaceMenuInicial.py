import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot as scb

class MenuInicialView:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
        self.__container = []
        self.__window = sg.Window(
            "Menu Inicial", self.__container, font=("Montserrat", 14))
    
    def tela_inicial(self):
        self.__container = [
            [sg.Text(f'Bem vindo ao ChatBot da empresa {self.__sistema.empresa}!', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, selecione uma opção:', font=('Montserrat', 18))],
            [sg.Text('', size=(15, 1))],
            [sg.Button('BotMaker', size=(25, 1), pad=(5, 0)), sg.Button('Chat', size=(25, 1), pad=(5, 0))],
        ]
        
    