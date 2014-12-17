from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_scraper.items import CraigslistScraperItem

class CraigslistSpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://newyork.craigslist.org/bka/"]

  def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//span[@class='pl']/a")
      items = []
      title = None
      for i in range(100):
          item = CraigslistScraperItem()
          title = titles[i]
          item ["title"] = title.select("text()").extract()
          item ["link"] = [u'http://newyork.craigslist.org' + title.select("@href").extract()[0]]
          items.append(item)
      return items
