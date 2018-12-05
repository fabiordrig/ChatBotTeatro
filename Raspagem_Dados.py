import requests
from bs4 import BeautifulSoup
#from telegram import Updater, MessageHandler, Filters 

global agenda


def Raspagem():
    global lista_titulo
    global lista_data
    global lista_imagem
    global lista_saiba_mais
    
    url = "http://www.teatrocolinas.com.br/inicio/"

    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")


        # ------------------------------ TITULO --------------------------------------

    titulo = soup.findAll("h2",{'class':'titulo_programacao_index'})
    lista_titulo = []
    for numero in range(0,len(titulo)):
        lista_titulo.append(titulo[numero])
        lista_titulo[numero] = str(lista_titulo[numero])
        lista_titulo[numero] = lista_titulo[numero].replace('<h2 class="titulo_programacao_index">','')
        lista_titulo[numero] = lista_titulo[numero].replace('</h2>','')



        # ---------------------------------- DATA ---------------------------

    data = soup.findAll("div",{'class':'data_index'})
    lista_data = []
    for numero in range(0,len(data)):
        lista_data.append(data[numero])
        lista_data[numero] = str(lista_data[numero])
        lista_data[numero] = lista_data[numero].replace('<div class="data_index">','')
        lista_data[numero] = lista_data[numero].replace('\n','')
        lista_data[numero] = lista_data[numero].replace('<img src="http://agenciaparla.com.br/teatrocolinas/wp-content/uploads/2018/08/calendar.png"/>','')
        lista_data[numero] = lista_data[numero].replace('</div>','')
        lista_data[numero] = lista_data[numero].replace('\t','')  


        #------------------------ SAIBA MAIS ------------------------------

    saiba_mais = soup.findAll('div', {'class':'botaosaibamais'})
    lista_saiba_mais = []
    for numero in range(0,len(saiba_mais)):
        lista_saiba_mais.append(saiba_mais[numero])
        lista_saiba_mais[numero] = str(lista_saiba_mais[numero])
        lista_saiba_mais[numero] = lista_saiba_mais[numero].replace('<div class="botaosaibamais">\n<a href="','')
        lista_saiba_mais[numero] = lista_saiba_mais[numero].replace('"><span class="btn_saibamais">Saiba Mais...</span></a>\n</div>','')


        #---------------------IMAGEM---------------

    imagem = soup.findAll('img', {'class':'attachment-thumb_programacao size-thumb_programacao wp-post-image'})
    lista_imagem = []
    for numero in range(0,len(imagem)):
        lista_imagem.append(imagem[numero])
        lista_imagem[numero] = str(lista_imagem[numero])
        lista_imagem[numero] = lista_imagem[numero].replace('<img alt="" class="attachment-thumb_programacao size-thumb_programacao wp-post-image" height="310" src="','')
        lista_imagem[numero] = lista_imagem[numero].replace('-419x310.jpg" width="419"/>','')

    return lista_titulo



    # -------------------------- ORGANIZAR ------------------------

def Agenda():
    agenda = {'nome' : [], 'data' : [], 'link' : [], 'imagem' : []}

    agenda['nome'].extend(lista_titulo)
    agenda['data'].extend(lista_data)
    agenda['link'].extend(lista_saiba_mais)
    agenda['imagem'].extend(lista_imagem)

    return agenda

   

