from bs4 import BeautifulSoup
import requests

# This code will extract all of the meta decks that are currently being used in professional play

source = requests.get('https://www.hearthpwn.com/cards?filter-include-card-text=y&display=1').text

soup = BeautifulSoup(source, 'lxml')


for card in soup.find_all('td'):
    cards = card.text
    print(cards)