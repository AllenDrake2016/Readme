from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
class Myspider(BaseSpider):
   name='craig'
   allowed_domains=['craigslist.org']
   start_urls=["http://sfbay.craigslist.org/sfc/npo"]

   def parse(self,response):
      hxs=HtmlXPathSelector(response)
      titles=hxs.select("//p")
      print(titles)
      for title in titles:
          self.title=titles.select("a/text()").extract()
          link=titles.select("a/href").extract()
          print title, link
