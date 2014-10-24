__author__ = 'koo'

import json
import urllib

query = 'mother'

api_key = open(".api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/search'
params = {
    'key': api_key,
    'filter': '(all child:"Frank Zappa")'
}
# params = {
#     'key': api_key,
#     'query': query
# }
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for result in response['result']:
    try:
        print result['name'] + ' (' + str(result['score']) + ')' +  ' [' + result['id'] + ']'
    except KeyError:
        print result['name'] + ' (' + str(result['score']) + ')'
