import requests
from bs4 import BeautifulSoup
from random import choice

def get_random_anecdot():
    response = requests.get('https://anekdotov.net/anekdot/today.html') #Получаем ответ сервера
    soup = BeautifulSoup(response.text, 'lxml') #Создаем объект супа на основе кода страницы
    anekdot = soup.find_all('div', class_='anekdot') #Ищем все блоки div с классом anekdot
    
    random_anekdot = choice(anekdot) #Выбираем случайный блок
    return random_anekdot.text #Возвращаем текст блока
    

def get_random_pic():
    response = requests.get('https://anekdotov.net/pic/today.html')
    soup = BeautifulSoup(response.text, 'lxml') 
    blocks = soup.find_all('div', class_='pic')
    pic = []
    for block in blocks:
        pic.append(f"https://anekdotov.net{block.find('img').get('src')}")
        
    return choice(pic)