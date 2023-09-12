#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotZangado import BotZangado
from Bots.BotFelizinho import BotFelizinho
from Bots.BotGago import BotGago
from Bots.BotNaruto import BotNaruto

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Gustavo Vonn"), BotTriste("Thom Yorke"), BotNaruto("Naruto"), BotGago("Elio"), BotFelizinho("Lucian")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
