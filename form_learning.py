import requests
import mechanicalsoup
import urllib.parse
broswer = mechanicalsoup.Browser()
login_page = broswer.get("https://github.com/login")


login_form = login_page.soup.select('#js-pjax-container')[0]
# login_form = login_form.select('form')[0]
# login_form.find('input', {'name': 'login'})['value'] = 'AllenDrake2016'
# login_form.find('input', {'name': 'password'})['value'] = '1234abcd'
# print(login_form.find('input', {'name': 'authenticity_token'})['value'])
a=login_form.find('input', {'name': 'authenticity_token'})['value']
# page2 = broswer.submit(login_form, login_page.url)
# print(login_form)
# print(page2.text)
# req=broswer._prepare_request(login_form, login_page.url)
data1={'commit': 'Sign in', 'login': 'AllenDrake2016', 'authenticity_token': a, 'password': '1234abcd', 'utf8': '✓'}
kwargs={}
kwargs['data']=data1
# print(data)
print(kwargs)
# files = kwargs.pop("files", dict())
req=requests.Request('post', urllib.parse.urljoin(login_page.url, "/session"), files={}, **kwargs)
req=broswer.session.prepare_request(req)
# resp=broswer.session.send(broswer._prepare_request(login_form, "https://posttestserver.com/post.php"))
resp=broswer.session.send(req)
# print(resp.text)
# from mechanicalsoup import Browser
# Browser.add_soup(resp, broswer.soup_config)
# print(req.body)
# print(broswer._prepare_request(login_form, login_page.url).body)

# print(type(broswer._prepare_request(login_form, login_page.url)))
# print(type(req))
# print(resp.text)