import json
import pandas
from pandas.io.json import json_normalize

#cards.json file is encoded in UTF-8. 

#pandas.set_option('display.max_rows', None)
#pandas.set_option('display.max_columns', 6)

with open('cards.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(json_normalize(data))
