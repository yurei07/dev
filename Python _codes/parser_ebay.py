import requests 
from bs4 import BeautifulSoup
import time 
import random

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

console.rule("[red]Parser ebay Ipads")

url = 'https://www.ebay.de/sch/i.html?_nkw=ipad&_sacat=0&_from=R40&_pgn='
ipad = []
count = 1

while 200 > count:
    link = 'https://www.ebay.de/sch/i.html?_nkw=ipad&_sacat=0&_from=R40&_pgn=' + str(count)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    divBlock = soup.find_all('div', class_='s-item__wrapper clearfix')
    if divBlock != []:
        ipad.extend(divBlock)

        value = round(random.random() + 1.5, 2)
        secondsTime = time.sleep(value)
        beautifulTimer = Panel(
            '[bold yellow]TIMER[/bold yellow]\n' + str(value) + ' s',
        )
        console.print(beautifulTimer)

    beautifulLink = Panel(
        '[bold yellow]LINK OF WEBSITE[/bold yellow]\n[white]https://www.ebay.de/sch/i.html?_nkw=ipad&_sacat=0&_from=R40&_pgn=' + str(count),
    )
    console.print(beautifulLink)
    count += 1

table = Table(title='Resulsts')

count = 0 
    
table.add_column('Name', justify='right', style='cyan', no_wrap=True)
table.add_column('Price', style='green')
table.add_column('Link', justify='right', style='magenta')

while 500 > count:
    info = ipad[int(count)]
    title = info.find('span', {'role':'heading'}).text
    price = info.find('span', {'class':'s-item__price'}).text
    link = info.find('a', {'class':'s-item__link'}).get('href')

    count += 1

    table.add_row( title, price, link)
console.print(table)






