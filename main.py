from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.komm.one/aktuelles/aktuelle-meldungen"

page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")

text_elemente = soup.find_all('div', class_='pm-content')

for text_element in text_elemente:
    print(text_element.text)