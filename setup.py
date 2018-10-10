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

    #Requisição da mensagem
    #R = requests.get("curl 'localhost:5000/parse?q=tmensagem&project=teste' ")
    #JSON do treinamento
    #R.json()
        #Requisicao do Rastro JS
        #RastroJS = requests.get('http://localhost:3000/track/' + numeroEncomenda+'/json')
        #Tratando o JSON que vem do Rastro JS
        #RastroJS.json
        #Dentro do json pegar o tipo "data" dentro dele o "track"e por fim trazer tudo o que tiver dentro
        #Respondendo as informaçoes sobre a encomenda
        #bot.sendMessage(chatID," ")
    if mensagem == '/start':
        bot.sendMessage(chatID,"Olá, " + nome +"!\nMeu nome é Lion, seu localizador de Encomendas!")
        bot.sendMessage(chatID,"Digite /encomenda mais o número da encomenda, para descobrir onde está sua encomenda\n")
        bot.sendMessage(chatID,"Exemplo : /encomenda74845784.")
        mensagem = ''
    if  "/encomenda" in mensagem:
        numeroEncomenda=mensagem.replace('/encomenda','')
        mensagem = ''
        bot.sendMessage(chatID,"Em Processo.")
    if mensagem != '':
        bot.sendMessage(chatID,"Tente usar /start para saber em que posso ajudá-lo.")
        
bot.message_loop(recebendoMsg)

while True:
    pass
