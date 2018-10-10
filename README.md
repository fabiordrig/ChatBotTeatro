# Rastreador de Encomendas com inteligencia artificial
chatbot do telegram para localizar encomendas para o usuario para o usuário


comando iniciais:
- docker :

docker run -p 5000:5000 rasa/rasa_nlu:latest-full - Inicia o servidor

curl --request POST --header 'content-type: application/json' --data-binary @seu-arquivo.json --url 'localhost:5000/train?project=nome-projeto' -  Comando de treino e padrão de model para inteligencia artificial

curl 'http://localhost:5000/parse?q=hello' - Comando para teste de intenções