import requests
import bs4
import json
import speech_recognition as sr
def search(text):
    url = "https://www.google.com/search?q=" + text
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text
                         , "html.parser")
    #print(soup)
    temp = soup.find("div", class_='BNeawe').text
    print('O resultado da sua pesquisa esta abaixo')
    print(temp)


