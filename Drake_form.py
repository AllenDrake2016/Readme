import requests
import json
# import mechanicalsoup
# import urllib.parse
# broswer = mechanicalsoup.Browser()
# login_page = broswer.get("https://blue.drake.edu/cp/home/displaylogin")
# login_form = login_page.soup.select('table')[0]
# a=login_form.select('script')[0]
# print(a)
b='document.writeln("<input class=\"textform\" type=\"text\" id=\"user\" name=\"user\" size=\"" + size + "\" tabindex=1 onFocus=\"hadFocus(true)\">");'
# print(b)
# data1={'user': '100187552', 'pass': 'xisuo18EX@', 'login_btn': '&nbsp;&nbsp;Login&nbsp;&nbsp;'}
# kwargs={}
# kwargs['data']=data1
# req=requests.Request('post', "https://blue.drake.edu/cp/home/login", files={}, **kwargs)
# req=broswer.session.prepare_request(req)
# resp=broswer.session.send(req)
# print(resp.text)

import json
textValue = '''
var page_data = {
   "default_sku" : "SKU12345",
   "get_together" : {
      "imageLargeURL" : "http://null.null/pictures/large.jpg",
      "URL" : "http://null.null/index.tmpl",
      "name" : "Paints",
      "description" : "Here is a description and it works pretty well",
      "canFavorite" : 1,
      "id" : 1234,
      "type" : 2,
      "category" : "faded",
      "imageThumbnailURL" : "http://null.null/small9.jpg"
   }
};
'''
jsonValue = '{%s}' % (textValue.split('{', 1)[1].rsplit('}', 1)[0],)
value = json.loads(jsonValue)
print(value)
jsonValue1='{%s}' % (b.split('{', 1)[1].rsplit('}', 1)[0],)
value1=json.loads(b)
print(value1)
