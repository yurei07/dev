from bs4 import BeautifulSoup # для парсинга html страницы
import requests  # для запросов к сайту, получаем содержимое веб сайта 
from requests import get
import time 
import random 

url = 'https://www.ebay.de/sch/i.html?_nkw=laptop&_sacat=0&_from=R40&_pgn=' # ссылка на сайт какой я буду парсить 
laptop = [] # список всех ноутов какие нашол на сайте 
low_price = []
count = 1 # страницы сайта
while count <= 2: #  пока страниц не будет 100, то выполняется то что с низу 
    url = 'https://www.ebay.de/sch/i.html?_nkw=laptop&_sacat=0&_from=R40&_pgn=' + str(count) # url = ссылка к сайту и добавляет один (типа следуйщяя страница)
    print(url) # выводит ссылку сайта 
    response = get(url) # вытягивает инфу с сайта это типа метод get
    html_soup = BeautifulSoup(response.text, 'html.parser') # создает парсинг сайта какой стоит url

    laptop_data = html_soup.find_all('div', class_='s-item__wrapper clearfix') # задаем чо надо парсирить. Типа какие теги и классы 
    if laptop_data != []:  # Проверяет, не пустой ли список laptop_data
        laptop.extend(laptop_data) # Добавляет элементы из laptop_data в конец списка laptop
        value = random.random()  
        scaled_value = 1 + (value * (9 - 5)) # Создать случайную задержку между запросами, чтобы сайт не заблокировал парсер
        print(scaled_value)
        time.sleep(scaled_value) # Приостанавливает выполнение программы на scaled_value секунд
    else:
        print('empty')
        break
    count += 1 # добавляет плюс сайтик 

print(len(laptop)) # длина laptop
print(laptop[1]) # индекс laptop
print() # пустое пространство
n = int(len(laptop)) # переводит в число 
count = 0

while count <= 5: # пока count меньше 5 
    info = laptop[int(count)] #  число или индекс count в laptop
    price = info.find('span',{'class':'s-item__price'}).text # finding price laptop
    title = info.find('a',{'class':'s-item__link'}).text # finding title laptop
    print(title, ' ', price) # выводит все вместе 
    count += 1    



