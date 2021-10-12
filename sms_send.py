import json
import serwersms
import sys;
import time
import os

from itertools import islice

api = serwersms.SerwerSMS(os.environ['SERWERSMS_LOGIN'], os.environ['SERWERSMS_PASSWORD'])

params = {
    # 'test': 'true',
    'details': 'true',
}
# update account settings to send multipart message

response = api.message.send_sms(sys.argv[1], sys.argv[2], 'INFORMACJA', params)
result = json.loads(response)
print(result),
if 'items' not in result:
    raise Exception('Empty items')

for item in result['items']:
    print(item['id'] + ' - ' + item['phone'] + ' - ' + item['status'])