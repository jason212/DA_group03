#TASK 6 -kenneth
import scrappy
classNewSpider(scrapytest.Spider):
    name = "new_spider"
    start_urls = ["https://brickset.com/sets/year-2000"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel ='@src'
            yield{
                'image Link':x.xpath(newsel).extract_first(),
            }
