import json
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame

data = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
        {'name': {'given': 'Mose', 'family': 'Regner'}},
        {'id': 2, 'name': 'Faye Raker'}]

print(json_normalize(data))

