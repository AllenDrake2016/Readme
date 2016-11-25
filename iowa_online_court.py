####################################################### iowa court online

# import argparse
# import mechanicalsoup
# broswer = mechanicalsoup.Browser()
#
# parser = argparse.ArgumentParser()
# parser.add_argument("username",action="store")
# parser.add_argument("password",action="store")
# args = parser.parse_args(["Lederman2016","lovelydayisntit"])
#
# login_page = broswer.get("https://www.iowacourts.state.ia.us/ESAWebApp/ESALogin.jsp")
# login_form = login_page.soup.select('form')[0]
#
# login_form.input['value'] = args.username
# login_form.find('input', {'name': 'password'})['value'] = args.password
# data={}
# for input in login_form.select("input"):
#     name = input.get("name")
#     # print(name)
#     value = input.get("value", "")
#     # print(value)
#     data[name] = value
#     print(data)
# page1 = broswer.submit(login_form, login_page.url)
# html=page1.soup.select('html')[0]
# print(html)
# login_form=html.find('form',{'name':"logoffButton",'method':"POST"})
# page2 = broswer.submit(login_form, page1.url)
# print(page2.url)
# print(page2.text)
# print(page2.text)
#
# page3=broswer.get('http://www.iowacourts.gov/')
# print(page3.text)

####################################################### iowa court logoff
# import requests
# import urllib.parse
# import mechanicalsoup
# broswer = mechanicalsoup.Browser()
#
# page0 = broswer.get("https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame")
#
# html=page0.soup.select('html')[0]
# # print(html)
#
# data1={'loginButton':'Logon','referrer':'init','registrationButton':'Register'}
# kwargs={}
# kwargs['data']=data1
# # print(data)
# # files = kwargs.pop("files", dict())
# req=requests.Request('post', page0.url, files={}, **kwargs)
# req=broswer.session.prepare_request(req)
# resp=broswer.session.send(req)
# print(resp.url)
# import urllib.parse
# import urllib.request
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(urllib.request.urlopen('https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame'))
# framexx = soup.find_all('frame')
# # print(framexx)
# for frame in framexx:
#     # print(urllib.parse.urljoin('https://www.iowacourts.state.ia.us',frame.attrs['src']))
#     # response = urllib.request.urlopen(urllib.parse.urljoin('https://www.iowacourts.state.ia.us',frame.attrs['src']))
#     # frame_soup = BeautifulSoup(response,"html.parser")
#     # print(frame_soup)
#     print(type(soup))
#     print(type(frame))
#     print(type(Frames))

####################################################### testing
import urllib.parse
import urllib.request
import mechanicalsoup
broswer = mechanicalsoup.Browser()
page0 = broswer.get("https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame")
page1=broswer.get("https://www.iowacourts.state.ia.us/ESAWebApp/SelectAction")
# print(page1)
# print(page1.text)
html=page1.soup.select('HTML')[0]
# print(html)
login_form = html.find('form',{'name':"footerForm",'method':"POST",'target':"_top"})
print(login_form)
# page1 = broswer.submit(login_form, login_page.url)
# print(urllib.parse.urljoin('https://www.iowacourts.state.ia.us',framexx.attrs['src']))
# response = urllib.parse.urljoin('https://www.iowacourts.state.ia.us',framexx.attrs['src'])
#
# frame_soup = BeautifulSoup(response,"html.parser")
# print(frame_soup.text)


