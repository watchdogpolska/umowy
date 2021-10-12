import json

with open('fetch_merged.json') as fp:
    target_content = json.load(fp)

done = [
]
for posel in target_content:
    if 'phone_numbers' not in posel:
        continue
    if posel['name'] in done:
        continue
    for phone in posel['phone_numbers']:
        if len(phone) != 9:
            continue
        # phone = '737164661'
        if posel['gender'] == 'M':
            print(f'python sms_send.py "+48{phone}" "Szanowny Panie Pośle {posel["name"]}, jestem Adam Dobrawy (lider inicjatywy Publiczny Rejestr Umów, członek Sieci Obywatelskiej Watchdog Polska). Czy mogę liczyć na poparcie w czwartek poprawki Senatu dot. Centralnego Rejestru Umów? Chętnie porozmawiam i rozwieje ewentualne wątpliwości (adam.dobrawy@siecobywatelska.pl, +48737164661). Więcej o poprawce: umowy.siecobywatelska.pl" ')
        else:
            print(f'python sms_send.py "+48{phone}" "Szanowna Pani Posłanko {posel["name"]}, jestem Adam Dobrawy (lider inicjatywy Publiczny Rejestr Umów, członek Sieci Obywatelskiej Watchdog Polska). Czy mogę liczyć na poparcie w czwartek poprawki Senatu dot. Centralnego Rejestru Umów? Chętnie porozmawiam i rozwieje ewentualne wątpliwości (adam.dobrawy@siecobywatelska.pl, +48737164661). Więcej o poprawce: umowy.siecobywatelska.pl" ')
