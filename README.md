# bot-fatec
chatbot do telegram para busca de pecas

#comandos
- docker run -p 5000:5000 rasa/rasa_nlu:latest-full - (Comando para baixar a imagem do rasa e subir o servidor da inteligencia artificial)

- curl 'https://raw.githubusercontent.com/RasaHQ/rasa_nlu/master/sample_configs/config_train_server_json.yml'  padrao de json de treino

- curl --request POST --header 'content-type: aplication/json' --data-binary @nomedojson.json --url 'localhost:5000/train?project=nomedoprojeto'

- curl 'localhost:5000/parse?q=frase&recebida&project=nomedoprojeto' - Comando para receber o json de intenções de acordo com a respostas com a resposta do usuário
