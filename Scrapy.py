class NewSpider(scrapy.Spider):
            name = "new_spider"
             start_urls = ['http://192.168.1.1/index.html']
            def parse(self, response):
                      css_selector = 'img'
                      for x in response.css(css_selector):
                                    newsel = '@src'
                                    yield {
                                           'Image Link': x.xpath(newsel).extract_first(),
                                    }
