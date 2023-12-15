import requests
from bs4 import BeautifulSoup


url = 'https://tengrinews.kz/news/'

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

quates = soup.find_all('span', class_= 'tn-hidden')

for quate in quates:
    print(quate.text)