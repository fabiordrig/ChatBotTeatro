##exemplo de raspagem de filmes

import requests
import json

def getFilmes(data,cinema):
    url = "https://api-content.ingresso.com/v0//sessions/city/46/theater/%s?partnership=&date=%s"%(cinema,data)
    html = requests.get(url)
    data = json.loads(html.content)
    col = [movies for movies in data[0]["movies"]]
    return col
        


def searchCinema(data):
    cinemas = ["351","377","1064"]
    for c in cinemas:
        yield getFilmes(data,c)

def getDates():
    cinemas = ["351","377","1064"]
    for c in cinemas:
        url = "https://api-content.ingresso.com/v0//sessions/city/46/theater/%s/dates"%c
        html = requests.get(url)
        data = json.loads(html.content)
        yield data

def getCinemas():
    
    return