from bs4 import BeautifulSoup 
from requests import get
import requests

city = "youngstown"
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

if temp >= 90:
    print (f"the temp is {temp} and its way to hot")
elif temp >= 65:
    print (f"its {temp} and its just right")
elif temp <= 65:
    print (f"its {temp} and its way too cold")

#i did this right but it wont work 