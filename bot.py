import requests, json, telepot, time, commands, rasa
from telepot.loop import MessageLoop
with open("config.json") as f:
    config = json.load(f)

rasa_url = config["rasa_url"]+"/parse?q=%s&project="+config["rasa_project"]
cmd = commands.Commands(config["bot_key"])
nlu = rasa.Rasa(config["bot_key"],rasa_url)
print('Servidor inicializado')
def handle(message):
    msg_type, chat_type, chat_id = telepot.glance(message)
    if "entities" in message and message["entities"][0]['type'] == 'bot_command':
        cmd.getCommand(message,chat_id)
    else:
        nlu.parseMessage(message,chat_id)

def on_callback_query(msg):
    data = msg
    print(data)
if __name__ == "__main__":
    telegram = telepot.Bot(config["bot_key"])
    MessageLoop(telegram, {
        "chat": handle,
        "callback_query": on_callback_query
    }).run_as_thread()
    while 1:
        try:
            time.sleep(10)
            pass
        except:
            break