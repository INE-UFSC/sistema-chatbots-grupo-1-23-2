#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Gustavo Vonn"), BotTriste("Thom Yorke")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
