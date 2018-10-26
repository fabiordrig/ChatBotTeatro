import telepot
class Commands():
    def __init__(self,key):
        self.telegram = telepot.Bot(key)
    def getCommand(self, msg, msg_id):
        if msg["text"] == '/help':
            self.telegram.sendMessage(msg_id,"Então mano, se você digitar /start eu começo, se digitar /sobre vai descobrir quem me fez")
        elif msg["text"] == "/start":
            self.telegram.sendMessage(msg_id,"Olá para começar me diga qual tipo de evento você pretende ir")
        else:
            self.telegram.sendMessage(msg_id,"Desculpe, não entendi o seu comando :/")