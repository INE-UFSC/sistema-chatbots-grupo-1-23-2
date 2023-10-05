import PySimpleGUI as sg
from Bots.PerguntaResposta import PerguntaResposta
from SistemaChatBot.SistemaChatBot import SistemaChatBot as scb

class BotMakerView:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
        self.__container = []
    
    def tela_selecao(self):
        self.__container = [
            [sg.Text('BotMaker selecionado!', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, selecione uma opção:', font=('Montserrat', 16))],
            [sg.Button('Criar', size=(12, 1), pad=(20, 0)), sg.Button('Editar', size=(12, 1), pad=(20, 15))],
        ]
        self.__window = sg.Window(
            "Selecionador do BotMaker", self.__container, font=("Montserrat", 14))
    
    def tela_criacao(self, perg_resp: list = [1, 2, "banana"]):
        self.__container = [
            [sg.Text('Criar um novo Bot', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, preencha os dados abaixo:', font=('Montserrat', 16))],
            [sg.Text('', size=(15, 1))],
            [sg.Text('Nome do bot:'), sg.Text('', size=(7, 1)), sg.InputText(key="nome")],
            [sg.Text('Apresentação do bot:'), sg.InputText(key="apresentacao", size=(40, 1))],
            [sg.Text('Mensagem de boas vindas:'), sg.InputText(key="boas_vindas", size=(36, 1))],
            [sg.Text('Mensagem de despedida:'), sg.InputText(key="despedida", size=(38, 1))],
            [sg.Text('Perguntas e respostas:'), sg.Combo(perg_resp, size=(30, 1)), sg.Button('Editar', size=(10, 1)), sg.Button('Novo', size=(10, 1))],
            [sg.Text('', size=(15, 1))],
            [sg.Button('Criar', size=(25, 1), pad=(5, 0)), sg.Button('Voltar', size=(25, 1), pad=(5, 0))],
        ]
        self.__window = sg.Window(
            "Criador de Bots", self.__container, font=("Montserrat", 14))
    
    def tela__criar_pergunta_resposta(self):
        self.__container = [
            [sg.Text('Criador de Perguntas e Respostas:', font=('Montserrat', 24, "bold"))],
            [sg.Text('Pergunta:', font=('Montserrat', 16)), sg.InputText(key="pergunta", pad=(0, 10))],
            [sg.Text('Resposta:', font=('Montserrat', 16)), sg.InputText(key="resposta")],
            [sg.Button('Salvar', size=(12,1), pad=(0, 15))]
        ]
        self.__window = sg.Window(
            "Criador de Pergunta", self.__container, font=("Montserrat", 14))
        
    def tela__editar_pergunta_resposta(self, pergunta: PerguntaResposta):
        self.__container = [
            [sg.Text('Editor de Perguntas e Respostas:', font=('Montserrat', 24, "bold"))],
            [sg.Text('Pergunta:', font=('Montserrat', 16)), sg.InputText(key="pergunta", default_text=f"{pergunta.pergunta}", pad=(0, 10))],
            [sg.Text('Resposta:', font=('Montserrat', 16)), sg.InputText(key="resposta", default_text=f"{pergunta.resposta}")],
            [sg.Button('Salvar', size=(12,1), pad=(0, 15))]
        ]
        self.__window = sg.Window(
            "Criador de Pergunta", self.__container, font=("Montserrat", 14))
        
    # criar tela de edição de bot
    