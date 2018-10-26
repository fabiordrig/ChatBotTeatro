import telepot, requests, raspa
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

class Rasa():
    def __init__(self,key, rasa_url):
        self.telegram = telepot.Bot(key)
        self.conversations = {}
        self.rasa_url = rasa_url

    def parseMessage(self, message,chat_id,):
        
        response = requests.get(self.rasa_url%message["text"])
        intent = response.json()["intent"]["name"]
        entities = response.json()["entities"]
        if intent == "cumprimento": 
            resposta = "Ola, tudo bem?\n"
            self.telegram.sendMessage(chat_id,resposta)
        elif intent == "encomenda":
            encomenda = False
            for key in entities:
                if key["entity"] == "encomenda":
                    encomenda = key["value"]
                    break
            if encomenda:
                resposta = "Ok, um segundo estou pesquisando a sua encomenda"
                self.telegram.sendMessage(chat_id,resposta)
            else:
                resposta = "Pode digitar novamente sua encomenda?"
                self.telegram.sendMessage(chat_id,resposta)
        else:
            self.telegram.sendMessage(chat_id,"Desculpe não entendi :(")        