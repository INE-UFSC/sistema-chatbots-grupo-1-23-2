from Bots.Bot import Bot

class BotNaruto(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.comandos= {"1" : 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA RASENGAAAAAAAAAANNNN!', "2": 'O Naruto pode ser um pouco duro às vezes, talvez você não saiba disso, mas o Naruto também cresceu sem pai. Na verdade ele nunca conheceu nenhum de seus pais, e nunca teve nenhum amigo em nossa aldeia.', "3": 'Minha comida preferida é o Ichiraku Ramen. Não tem nada melhor do que um prato quente de ramen depois de um dia de treinamento ou uma batalha intensa.', "4" : self.despedida()}

    def apresentacao(self):
        return 'Eu sou Naruto Uzumaki, o ninja número um da Vila da Folha, e o meu sonho é me tornar o Hokage, é isso aí dattebayo!'
 
    def mostra_comandos(self):
        return '1 - Rasengan\n2 - Motivacional\n3 - Comida preferida\n4 - Adeus\n'        

    def executa_comando(self,cmd):
        if cmd == "-1":
            return self.comandos["4"]
        return self.comandos[cmd]

    def boas_vindas(self):
        return 'Seja bem-vindo! Estou animado para ter você aqui comigo. Vamos juntos em busca dos nossos sonhos e se tornar hokages!'

    def despedida(self):
        return 'Até a próxima, pessoal! Nunca desistam dos seus sonhos no mundo ninja, DATTEBAYO!'