import telepot
class Commands():
    def __init__(self,key):
        self.telegram = telepot.Bot(key)
    def getCommand(self, msg, msg_id):
        if msg["text"] == '/help':
            self.telegram.sendMessage(msg_id,"COLOCAR O HELP AQUI TIU")
        elif msg["text"] == "/start":
            self.telegram.sendMessage(msg_id,"Olá para começar me diga qual tipo de evento você pretende ir")
        elif msg["text"] == "/sobre":
            self.telegram.sendMessage(msg_id,"sou um bot criado na FATEC SJC")
        else:
            self.telegram.sendMessage(msg_id,"Desculpe, não entedi o seu comando :/")