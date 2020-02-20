import json
from urllib.request import urlopen

with urlopen("https://api.hearthstonejson.com/v1/40734/enUS/cards.json") as response:
    source = response.read()

print(source)