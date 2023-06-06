import json

a = []

with open('маты.txt', encoding='UTF-8') as r:
    for i in r:
        mat = i.lower().split('\n')[0]
        if mat != '':
            a.append(mat)

with open('маты.json', 'w', encoding='utf-8') as e:
    json.dump(a, e)