import json
from itertools import groupby
import yaml
import re

x = json.load(open('fetch_merged.json'))

sections = [];

def reverse(v):
    v.reverse()
    return v

for (club, persons) in groupby(sorted(x, key=lambda x:x['club_short']), lambda x: x['club_short']):
    name = club.replace('.', '')
    with open('_data/{}.yml'.format(name), 'w') as fp:
        y = list(persons)
        for v in y:
            v['twitter_links'] = [re.sub('\?.+?$', '', x.replace('https://twitter.com/', '')) for x in v.get('twitter_links', [])]
            v['phone_numbers'] = [re.sub('[\(\) ]', '', x) for x in v.get('phone_numbers', [])]
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

with open('fetch_merged.json', 'w+') as fp:
    fp.write(json.dumps(sorted(x, reverse=True, key=lambda x: " ".join(reverse(x['name'].split(" ")))), indent=4, sort_keys=True))
