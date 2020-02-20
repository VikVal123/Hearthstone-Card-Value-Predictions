import json

#JSON is a very common data formating. JSON is used alot for
#fetching data from online APIs. JSON - JacaScript Object Notation.
#JSON files can be read and changed with specific methods. Also 
#you can read a file, modify it and create a copy of it to remove any 
#unnecessary information that you do not need.

with open('cards.json') as f:
    data = json.load(f)

print(data)