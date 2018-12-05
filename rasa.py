import telepot, requests, raspa
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from Raspagem_Dados import Raspagem, Agenda

class Rasa():
    def __init__(self,key, rasa_url):
        self.telegram = telepot.Bot(key)
        self.conversations = {}
        self.rasa_url = rasa_url

    def parseMessage(self, message,chat_id,):
        response = requests.get("http://"+self.rasa_url%message["text"])
        intent = response.json()["intent"]["name"]
        entities = response.json()["entities"]
        if intent == "cumprimento": 
            resposta = "Ola, tudo bem?\n"
            self.telegram.sendMessage(chat_id,resposta)
        elif intent == "resposta":
            self.telegram.sendMessage(chat_id, "Otimo!")
        elif intent == "teatro":
            encomenda = True
            if encomenda:
                resposta = "Ok, estou pesquisando as pecas."
                self.telegram.sendMessage(chat_id,resposta)
                r = Raspagem()
                a = Agenda()
                self.telegram.sendMessage(chat_id, "Essas sao as pecas disponiveis no Teatro!")
                for numero in range(0, len(r)):
                    print(numero)
                    self.telegram.sendPhoto(chat_id, a['imagem'][numero])
                    self.telegram.sendMessage(chat_id,  str( a['nome'][numero]) + '\n' + str( a['data'][numero]) + '\n' + str(a['link'][numero]))
                    if numero == 5:
                        self.telegram.sendMessage(chat_id, "Gostou de alguma ? Clica no link abaixo da data para saber mais da peca.")
        else:
            self.telegram.sendMessage(chat_id,"Desculpe não entendi :(")        