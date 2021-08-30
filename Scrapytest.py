import requests

r = requests.get('https://brickset.com/sets/year-2000')
print("\t *", r.status_code)


h = requests.head('https://brickset.com/sets/year-2000')
print("Header:")
print("****")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("****")


# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)



import scrapy
class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://brickset.com/sets/year-2000']

 

    def start_requests(self):
        headers= {USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"}
        for url in self.start_urls:
            yield Request(url, headers=headers)
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

 

            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
