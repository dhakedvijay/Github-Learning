import requests
from bs4 import BeautifulSoup
def temp():
    page=requests.get("https://weather.com/en-IN/weather/today/l/26.91,75.79?par=google&temp=c")
    soup=BeautifulSoup(page.content,'lxml')
    h4=soup.find(class_='today_nowcard-temp')
    h4=h4.find('span')                        
    return h4.text
