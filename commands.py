import telepot
from Raspagem_Dados import Raspagem, Agenda
class Commands():
    def __init__(self,key):
        self.telegram = telepot.Bot(key)
    def getCommand(self, msg, msg_id):
        if msg["text"] == '/help':
            self.telegram.sendMessage(msg_id,"HELP\nDigite /start para começar.\nDigite /criadores para descobrir quem me criou.\nDigite /sobre para descobrir o que eu faço.")
        elif msg["text"] == "/start":
            self.telegram.sendMessage(msg_id,"Olá, para começar me diga qual tipo de evento você pretende ir")
        elif msg["text"] == "/criadores":
            self.telegram.sendMessage(msg_id, "Criadores:\nFabio Rodrigues.\nLuciano Cabral.\nLuis Belo.\nProfessor:\nGiuliano Bertoti.")
        elif msg["text"] == "/sobre":
            self.telegram.sendMessage(msg_id, "Oi, Meu nome é Lion.\nFui criado com a itenção de ajudar as pessoas encotrarem suas peças favoritas! ")
        else:
            self.telegram.sendMessage(msg_id,"Desculpe, não entendi o seu comando :/")