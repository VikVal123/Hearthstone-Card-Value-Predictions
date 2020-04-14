`import json
import pandas
from pandas.io.json import json_normalize

#cards.json file is encoded in UTF-8. 

# pandas.set_option('display.max_rows', 10000)
# pandas.set_option('display.max_columns', 11)

with open('cards.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)
    df = pandas.json_normalize(raw_data)

# print(data[['id', 'name', 'cost', 'text', 'attack', 'health', 
# 'cardClass', 'mechanics', 'rarity', 'set', 'type']])

df.to_excel("cards.xlsx")`