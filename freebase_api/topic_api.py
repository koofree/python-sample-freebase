__author__ = 'Koo Lee'

import json
import urllib

answers = ['Michael Gray', 'Billy', 'Rose Marie', 'Room Service', 'Moon'];

api_key = open(".api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/topic'
topic_id = '/en/frank_zappa'
params = {
    'key': api_key,
    'filter': 'suggest'
}
params = {
    'key': api_key,
    'filter': 'all'
}
params = {
    'key': api_key,
    'filter': 'all'
}
url = service_url + topic_id + '?' + urllib.urlencode(params)
topic = json.loads(urllib.urlopen(url).read())

answer = [];

for property in topic['property']:
    print property + ':'
    for value in topic['property'][property]['values']:
        try:
            text = value['text']
        except KeyError:
            text = ''
        print ' - ' + text
        for _a in answers:
            if (text in _a) or (_a in text):
                if not _a in answer:
                    answer.append(_a)

print ':: answer is ' + ', '.join([str(x) for x in answer])