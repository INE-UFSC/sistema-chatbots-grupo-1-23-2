import PySimpleGUI as sg
from Bots.Bot import Bot
from SistemaChatBot.SistemaChatBot import SistemaChatBot as scb


class InterfaceChat:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
    
    def tela_selecao_bot(self):
        self.__container = [
            [sg.Text('Por favor selecione um bot', font=('Montserrat', 24, "bold"))],
            [sg.Text('Bot:', font=('Montserrat', 16), pad=(0, 18)), sg.Combo(self.sistema.lista_bots, readonly=True)],
            [sg.Button('Ok', size=(5,1))], sg.Button('Voltar', size=(5,1))]
        self.__window = sg.Window(
            "Selecao de Bot", self.__container, font=("Montserrat", 14))
        
    def tela_chat(self, bot: Bot, mensagem: str):
        self.__container = [
            [sg.Text(f'Sistema ChatBot {self.__sistema.empresa}', font=('Montserrat', 24, "bold"))],
            [sg.Text(f'Você está conversando com o bot {bot.nome}, seja gentil!', font=('Montserrat', 16))],
            [sg.Multiline(mensagem, size=(72, 20), font=('Montserrat', 14), autoscroll=True, disabled=True, pad=(10, 18))],
            [sg.Text(' Selecione sua pergunta:', font=('Montserrat', 16)), sg.Combo(bot.perguntas_respostas, size=(40, 1), readonly=True), sg.Button('Enviar', size=(10, 1))], 
            [sg.Button('Voltar', size=(10, 1))]
            ]
        
        self.__window = sg.Window(
            f"ChatBot com {bot.nome}", self.__container, font=("Montserrat", 14))
        
    def le_eventos(self):
        return self.__window.read()