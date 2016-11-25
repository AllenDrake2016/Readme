# import requests
# # print(requests.get('http://www.google.com'))
# # print(type(requests.get('http://www.google.com')))
# my_list_of_links=['http://www.google.com']
# for index, link in enumerate(my_list_of_links):
#     payload={'q':'test'}
#     test=requests.get(link,params=payload)
#     test.encoding='ISO-8859-1'
#     print(test.text)

####################################################### 1
# import urllib.request
# import urllib.parse
# import json
#
# url='http://pythonprogramming.net'
#
# values={'s':'basic', 'submit':'search'}
# data=urllib.parse.urlencode(values)
# print('data1:'+data)
# data=data.encode('utf-8')
# print('data2:')
# print(data)
# req=urllib.request.Request(url,data)
# print('req:')
# print(req)
# resp=urllib.request.urlopen(req)
# print('resp:')
# print(resp)
# respData=resp.read()
# print('respData')
# print(respData)
#
# try:
#     url='https://www.google.com/search?q=test'
#     headers={}
#     headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
#     req=urllib.request.Request(url,headers=headers)
#     resp=urllib.request.urlopen(req)
#     respData=resp.read()
#     savefile=open('Withheaders.txt','w')
#     savefile.write(str(respData))
#     savefile.close()
#
# except Exception as e:
#     print(str(e))
#
# resp.json()
# print(resp.json())


####################################################### https://posttestserver.com/

# import urllib.request
# import urllib.parse
# import json
#
# url='https://posttestserver.com/post.php'
#
# values={'s':'basic', 'submit':'search'}
# data=urllib.parse.urlencode(values)
# print('data1:')
# print(type(data))
# data=data.encode('utf-8')
# print('data2:')
# print(type(data))
# req=urllib.request.Request(url,data)
# print('req:')
# print(type(req))
# resp=urllib.request.urlopen(req)
# print('resp:')
# print(type(resp.url))
# print(type(resp.read()))
# #
# # try:
# #     url='https://posttestserver.com/post.php'
# #     headers={}
# #     headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
# #     req=urllib.request.Request(url,headers=headers)
# #     resp=urllib.request.urlopen(req)
# #     respData=resp.read()
# #     savefile=open('Withheaders.txt','w')
# #     savefile.write(str(respData))
# #     savefile.close()
# #
# # except Exception as e:
# #     print(str(e))
#
#
#
#
import requests
import urllib.parse
import mechanicalsoup
broswer = mechanicalsoup.Browser()
login_page = broswer.get("https://github.com/login")
# print(type(broswer))
# print(type(login_page))
# print(type(broswer.session))
# print(type(broswer.soup_config))

login_form = login_page.soup.select('#js-pjax-container')[0]
# print(type(login_form))
login_form = login_form.select('form')[0]
# print(type(login_form))
login_form.find('input', {'name': 'login'})['value'] = 'AllenDrake2016'
login_form.find('input', {'name': 'password'})['value'] = '1234abcd'
# print(type(login_form))
# login_page=broswer.get('https://posttestserver.com/post.php')
data = {}
# print(login_form.get("method", "get"))
print(login_form.get("action"))
print(type(login_form.get("action")))
print(urllib.parse.urljoin(login_page.url, login_form.get("action")))
print(type(urllib.parse.urljoin(login_page.url, login_form.get("action"))))
# print(login_form.select("input"))
for input in login_form.select("input"):
    name = input.get("name")
    # print(name)
    value = input.get("value", "")
    # print(value)
    data[name] = value
    # print(data)
# print(type(data))
# print(type(broswer.submit(login_form, login_page.url)))
# print(type(broswer._prepare_request(login_form, login_page.url)))
# print(type(broswer.session.send(broswer._prepare_request(login_form, login_page.url))))

# page2 = broswer.submit(login_form, login_page.url)
# print(type(page2.text))
# print(login_form)

####################################################### class
# print('hello')
# a={}
# files={}
# method=login_form.get("method", "get")
# action=login_form.get("action")
# url='https://posttestserver.com/post.php'
#
# request=requests.Request(method, url, files=files, data=data)
# print(request)
#
#
# # r = requests.post("https://posttestserver.com/post.php", data=data)
# r = requests.post("https://github.com/login/", data=data)
# print(r.status_code, r.reason)
# print(r.text)
#
# #print(broswer.submit(login_form, "https://github.com/login"))
# print(broswer.submit(login_form, "http://posttestserver.com/post.php?dump&html&dir=henry&status_code=202&sleep=2"))

# with requests.Session() as c:
#     url='https://github.com/login'
#     c.get(url)
#     c.post(url, data=data,headers={"Referer":"https://github.com/"})
#     page=c.get(url,data=data)
#     print(page)
#     print(page.content)
#     print(page.text)
#     print(page.status_code)


# import requests
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
#
# # both 'x-test' and 'x-test2' are sent
# a=s.get('http://posttestserver.com/post.php?dump&html&dir=henry&status_code=202&sleep=2', headers={'x-test2': 'true'})
# print(a.text)

####################################################### try

# try:
#     try:aosidhasdasdasdkshdfklanklsnaklsbflbkasbdjans.d,bkafvkbzkfbabasd
#     except: print('what?')
# except ZeroDivisionError:
#     print('hey there!')

####################################################### urlparse
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(s)
# server='pythonprogramming.net'
# port=80
# server_ip=socket.gethostbyname(server)
#
# request="GET / HTTP/1.1\nHOST:"+server+'\n\n'
# s.connect((server,port))
# s.send(request.encode())
# result=s.recv(4096)
# print(result)
#
# while (len(result)>0):
#     print(result)
#     result=s.recv(1024)


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server='pythonprogramming.net'
# def pscan(port):
#     try:
#         s.connect((server,port))
#         return True
#     except:
#         return False
#
# for x in range(1,26):
#     if pscan(x):
#         print('Port',x,'is open')
#     else:
#         print('Port',x,'is closed')

# from pip._vendor import html5lib
# with open("mydocument.html", "rb") as f:
#     lxml_etree_document = html5lib.parse(f, treebuilder="lxml")
#     print('lxml_etree_document:')
#     print(lxml_etree_document)
# parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
# minidom_document = parser.parse("<p>Hello World!")
# print('parser:')
# print(parser)
# print('minidom_document:')
# print(minidom_document)

