import json
# import requests
# from pathlib import Path
# import re

with open('fetch_poslowie_from_sejm_gov_pl.json') as fp:
    sejm_content = json.load(fp)

with open('fetch.json') as fp:
    target_content = json.load(fp)

def normalize_name(v):
    parts = v.split(' ')
    return f"{parts[0]} {parts[-1]}"

sejm_name = {normalize_name(x['name']) for x in sejm_content}
target_name = {normalize_name(x['name']) for x in target_content}
assert(len(sejm_name) == len(sejm_content))
assert(len(target_content) == len(target_content))

print('Extra sejm:', sejm_name - target_name)
print('Missing sejm:', target_name - sejm_name)

def find_person(name):
    return next(x for x in sejm_content if normalize_name(x['name']) == normalize_name(name))

short_map = {
    'Koalicyjny Klub Parlamentarny Lewicy (Nowa Lewica, PPS, Razem, Wiosna Roberta Biedronia)': 'Lewica',
    'Poseł niezrzeszony': 'niez.',
}

# def safe_name(x):
#     return re.sub('[^A-Za-z]', '_', x)

for target_person in target_content:
    name = target_person['name']
    sejm_person = find_person(name)
    if sejm_person['partia']['Klub/koło:'] != target_person['club_long']:
        print('missmatch club', name, sejm_person['partia']['Klub/koło:'], '!=', target_person['club_long'])
        target_person['club_long'] = sejm_person['partia']['Klub/koło:']
        target_person['club_short'] = short_map[target_person['club_long']]
    # p = Path(f'img/{safe_name(name)}.jpg')
    # if not p.exists():
    #     print('Download img for', p)
    #     p.write_bytes(requests.get(sejm_person['picute']).content)
    # target_person['img'] = str(p)


with open('fetch_merged.json', 'w') as fp:
    json.dump(target_content, fp, indent=4, sort_keys=True)
