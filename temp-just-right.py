from bs4 import BeautifulSoup 
from requests import get
import requests

url = "https://www.wunderground.com/weather/us/oh/canfield/41.02,-80.76"
response = requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')
temp = soup.find(class_= 'wu-value wu-value-to')

print(temp.text)
int_temp = int(temp.text)

comfortatbility = ''

if temp >= 90:
    comfortatbility = 'its too hot'
elif temp >= 65:
    comfortatbility = 'its just right'
elif temp <= 65:
    comfortatbility = 'its too cold'

print(f"the current temp is {int_temp}. Its {comfortatbility}")