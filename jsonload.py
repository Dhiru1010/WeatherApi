import json
from pprint import pprint as pp

with open('in.json',encoding='utf-8-sig') as a:
    data = json.load(a)

    print(pp(data))

