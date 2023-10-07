import PySimpleGUI as sg

class BotMaker:
    def __init__(self):
        self.state = 'menu_principal'
        self.layout_menu_principal = [[sg.Text('BotMaker', font=('Montserrat', 18))],
                                      [sg.Button('Criar Bot', size=(20, 2), font=('Montserrat', 14), key='-CRIAR_BOT-')],
                                      [sg.Button('Editar Bot', size=(20, 2), font=('Montserrat', 14), key='-EDITAR_BOT-')],
                                      [sg.Button('Excluir Bot', size=(20, 2), font=('Montserrat', 14), key='-EXCLUIR_BOT-')]]
        self.layout_criar_bot = [[sg.Text('Criando Bot', font=('Montserrat', 18))],
                                 [sg.Button('Voltar', size=(10, 1), font=('Montserrat', 14), key='-VOLTAR-')]]
        self.layout_editar_bot = [[sg.Text('Editando Bot', font=('Montserrat', 18))],
                                  [sg.Button('Voltar', size=(10, 1), font=('Montserrat', 14), key='-VOLTAR-')]]
        self.layout_excluir_bot = [[sg.Text('Excluindo Bot', font=('Montserrat', 18))],
                                   [sg.Button('Voltar', size=(10, 1), font=('Montserrat', 14), key='-VOLTAR-')]]

    def run(self):
        while True:
            if self.state == 'menu_principal':
                window = sg.Window('BotMaker', self.layout_menu_principal)
                event, values = window.read()
                window.close()
                if event == sg.WIN_CLOSED:
                    break
                elif event == '-CRIAR_BOT-':
                    self.state = 'criando_bot'
                elif event == '-EDITAR_BOT-':
                    self.state = 'editando_bot'
                elif event == '-EXCLUIR_BOT-':
                    self.state = 'excluindo_bot'
            elif self.state == 'criando_bot':
                window = sg.Window('BotMaker', self.layout_criar_bot)
                event, values = window.read()
                window.close()
                if event == sg.WIN_CLOSED:
                    break
                elif event == '-VOLTAR-':
                    self.state = 'menu_principal'
            elif self.state == 'editando_bot':
                window = sg.Window('BotMaker', self.layout_editar_bot)
                event, values = window.read()
                window.close()
                if event == sg.WIN_CLOSED:
                    break
                elif event == '-VOLTAR-':
                    self.state = 'menu_principal'
            elif self.state == 'excluindo_bot':
                window = sg.Window('BotMaker', self.layout_excluir_bot)
                event, values = window.read()
                window.close()
                if event == sg.WIN_CLOSED:
                    break
                elif event == '-VOLTAR-':
                    self.state = 'menu_principal'

bot_maker = BotMaker()
bot_maker.run()