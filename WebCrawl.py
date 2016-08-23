# from requests import Request, Session
#
# s = Session()
# req = Request('GET',  url, data=data, headers=headers)
#
# prepped = s.prepare_request(req)
#
# # do something with prepped.body
# prepped.body = 'Seriously, send exactly these bytes.'
#
# # do something with prepped.headers
# prepped.headers['Keep-Dead'] = 'parrot'
#
# resp = s.send(prepped,
#     stream=stream,
#     verify=verify,
#     proxies=proxies,
#     cert=cert,
#     timeout=timeout
# )
#
# print(resp.status_code)
#
import requests
# s=requests.Session.send()

# import json
# import requests
#
# r = requests.get('http://httpbin.org/stream/20', stream=True)
# print(r.iter_lines())
# for line in r.iter_lines():
#
#     # filter out keep-alive new lines
#     if line:
#         print(json.loads(line))

import requests
r = requests.get('https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
if r.status_code == requests.codes.ok:
    print('header:')
    print(r.headers['content-type'])
commit_data = r.json()
print('keys:')
print(commit_data.keys())
print("u'committer:")
print(commit_data[u'committer'])
print("u'message:")
print(commit_data[u'message'])

