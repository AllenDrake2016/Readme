import requests
import json
import mechanicalsoup
import urllib.parse
broswer = mechanicalsoup.Browser()
login_page = broswer.get("https://blue.drake.edu/cp/home/displaylogin")
login_form = login_page.soup.select('table')[0]
a=login_form.select('script')[0]
# print(a)
# print(b)
data1={'user': '100187552', 'uuid': 'newxisuo18EX@', 'login_btn': '&nbsp;&nbsp;Login&nbsp;&nbsp;','cancel_btn':'Cancel'}
kwargs={}
kwargs['data']=data1
req=requests.Request('post', "https://blue.drake.edu/cp/home/login", files={}, **kwargs)
req=broswer.session.prepare_request(req)
resp=broswer.session.send(req)
print(resp.text)
