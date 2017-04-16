# import requests
# from lxml import html
# import bs4
# import re
#
# s=requests.session()
# # login_url = "https://bitbucket.org/account/signin/?next=/"
# login_url="https://blue.drake.edu/cp/home/displaylogin"
# result = s.get(login_url)
#
#
# result.soup=bs4.BeautifulSoup(result.content, dict())
# Dtext=result.text
# Dtext.find("function")
# m = re.search('document.cplogin.uuid.value=', Dtext)
# n = re.search('document.cplogin.submit', Dtext)
# NDtext = Dtext[m.start():n.end()]
# NDtext=NDtext.replace('"','')
# q = re.search('=', NDtext)
# w = re.search(';', NDtext)
# NDtext=NDtext.replace('=','')
# NDtext=NDtext.replace(';','')
# c = NDtext[q.start():w.end()]
#
#
# # tree = html.fromstring(result.text)
# # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
# #
# # print(result)
# # print(tree)
# # print(authenticity_token.read())
#
# payload={'pass': 'newxisuo18EX@', 'uuid': c, 'user':'100187552'}
#
# result = s.post(
#     login_url,
#     data = payload,
#     headers = dict(referer=login_url)
# )
#
# print(result.text)









import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


