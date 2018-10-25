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
            resposta = "Ola, tudo bem?\nQue tal um cinema?\nÉ so perguntar!"
            self.telegram.sendMessage(chat_id,resposta)
        elif intent == "cinema":
            cinema = False
            for key in entities:
                if key["entity"] == "cinema":
                    cinema = key["value"]
                    break
            if cinema:
                resposta = "Ok, um segundo estou pesquisando os horários disponiveis"
                self.telegram.sendMessage(chat_id,resposta)
            else:
                resposta = "Em qual cinema você pretende ir?"
                self.telegram.sendMessage(chat_id,resposta)
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Center Vale", callback_data="351",)],
                    [InlineKeyboardButton(text="Colinas", callback_data="377",)],
                    [InlineKeyboardButton(text="Vale Sul", callback_data="1064",)]
                ])
                self.telegram.sendMessage(chat_id,"Escolha um cinema",reply_markup=keyboard,)
        else:
            self.telegram.sendMessage(chat_id,"Desculpe não entendi :(")        