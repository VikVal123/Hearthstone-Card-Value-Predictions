import json

#cards.json file is encoded in UTF-8. 

with open('cards.json', encoding='utf-8') as f:
    data = json.load(f)

print(data)