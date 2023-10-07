import PySimpleGUI as sg
from Bots.PerguntaResposta import PerguntaResposta
from SistemaChatBot.SistemaChatBot import SistemaChatBot as scb
from Bots.Bot import Bot

class BotMakerView:
    def __init__(self, sistema: scb):
        self.__sistema = sistema
        self.__container = []

    @property
    def sistema(self):
        return self.__sistema
    
    def tela_selecao_inicial(self):
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
    
    def tela_criar_pergunta_resposta(self):
        self.__container = [
            [sg.Text('Criador de Perguntas e Respostas:', font=('Montserrat', 24, "bold"))],
            [sg.Text('Pergunta:', font=('Montserrat', 16)), sg.InputText(key="pergunta", pad=(0, 10))],
            [sg.Text('Resposta:', font=('Montserrat', 16)), sg.InputText(key="resposta")],
            [sg.Button('Salvar', size=(12,1), pad=(0, 15))]
        ]
        self.__window = sg.Window(
            "Criador de Pergunta", self.__container, font=("Montserrat", 14))
        
    def tela_editar_pergunta_resposta(self, pergunta: PerguntaResposta):
        self.__container = [
            [sg.Text('Editor de Perguntas e Respostas:', font=('Montserrat', 24, "bold"))],
            [sg.Text('Pergunta:', font=('Montserrat', 16)), sg.InputText(key="pergunta", default_text=pergunta.pergunta, pad=(0, 10))],
            [sg.Text('Resposta:', font=('Montserrat', 16)), sg.InputText(key="resposta", default_text=pergunta.resposta)],
            [sg.Button('Salvar', size=(12,1), pad=(0, 15))]]
        
        self.__window = sg.Window(
            "Editor de Pergunta", self.__container, font=("Montserrat", 14))
        
    def tela_selecao_bot(self):
        self.__container = [
            [sg.Text('Por favor selecione um bot', font=('Montserrat', 24, "bold"))],
            [sg.Text('Bot:', font=('Montserrat', 16), pad=(0, 18)), sg.Combo(self.sistema.lista_bots)],
            [sg.Button('Ok', size=(5,1))], sg.Button('Voltar', size=(5,1))]
        self.__window = sg.Window(
            "Selecao de Bot", self.__container, font=("Montserrat", 14))
        
    def tela_edicao_bot(self, bot: Bot):
        self.__container = [
            [sg.Text('Editar Bot', font=('Montserrat', 24, "bold"))],
            [sg.Text('Por favor, altere os dados abaixo:', font=('Montserrat', 16))],
            [sg.Text('', size=(15, 1))],
            [sg.Text('Nome do bot:'), sg.Text('', size=(7, 1)), sg.InputText(key="nome", default_text=bot.nome)],
            [sg.Text('Apresentação do bot:'), sg.InputText(key="apresentacao", default_text=bot.apresentacao, size=(40, 1))],
            [sg.Text('Mensagem de boas vindas:'), sg.InputText(key="boas_vindas", default_text=bot.boas_vindas, size=(36, 1))],
            [sg.Text('Mensagem de despedida:'), sg.InputText(key="despedida", default_text=bot.despedida, size=(38, 1))],
            [sg.Text('Perguntas e respostas:'), sg.Combo(bot.perguntas_respostas, size=(30, 1)), sg.Button('Editar', size=(10, 1)), sg.Button('Novo', size=(10, 1))],
            [sg.Text('', size=(15, 1))],
            [sg.Button('Confirmar', size=(25, 1), pad=(5, 0)), sg.Button('Voltar', size=(25, 1), pad=(5, 0))],
        ]
        self.__window = sg.Window(
            "Editor de Bot", self.__container, font=("Montserrat", 14))
       
    def le_eventos(self):
        return self.__window.read()
        
    
        