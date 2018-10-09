import telepot
import requests
import json
bot = telepot.Bot("697985710:AAHNBhFF_-Q3oWL0k1PytlhXaCPt1Hpe9WQ")
bot.getUpdates()
numeroEncomenda=''
def recebendoMsg(msg):
    mensagem = msg['text']
    chatID = msg['chat']['id']
    nome = msg['chat']['first_name']
    print(nome+": "+msg['text'])

    if mensagem == '/start':
        bot.sendMessage(chatID,"Olá, " + nome +"!\nMeu nome é Lion, seu localizador de Encomendas!")
        bot.sendMessage(chatID,"Digite /encomenda mais o número da encomenda, para descobrir onde está sua encomenda\n")
        bot.sendMessage(chatID,"Exemplo : /encomenda 74845784.")
        mensagem = ''
    if  "/encomenda" in mensagem:
        numeroEncomenda=mensagem.replace('/encomenda','')
        mensagem = ''
        #teste
        print(numeroEncomenda)
        #requisicao do Rastro JS
        #r = requests.get('http://localhost:3000/track/' + numeroEncomenda+'/json')
        #print(r.text)
        #print(r)
        #print(r.json)
    if mensagem != '':
        bot.sendMessage(chatID,"Tente usar /start para saber em que posso ajudá-lo.")
        
bot.message_loop(recebendoMsg)

while True:
    pass
