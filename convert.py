import json
from itertools import groupby
import yaml
x = json.load(open('fetch.json'))

sections = [];

for (club, persons) in groupby(sorted(x, key=lambda x:x['club_short']), lambda x: x['club_short']):
    name = club.replace('.', '')
    with open('_data/{}.yml'.format(name), 'w') as fp:
        y = list(persons)
        content = {"websites": y}
        sections.append({
            "id": name, 
            "title": y[0]['club_long'],
            "icon": "users",
            "size": len(y),
        })
        fp.write(yaml.dump(content))

with open('_data/sections.yml', 'w+') as fp:
    fp.write(yaml.dump(sorted(sections, reverse=True, key=lambda x: x['size'])))
