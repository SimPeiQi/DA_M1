#1-reconnaissance lab 10b (done. only extra 2 url if want)

#1.1-perform "get" request on web
import requests
url = 'https://brickset.com/sets/year-1998'
r = requests.get(url)
#1.2-display "OK"
print("Status code:")
print("\t*",r.status_code)
#1.3-display web header
h = requests.head(url)
print("Header:")
print("**********")
r = requests.get('https://brickset.com/sets/year-1998%27')
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("**********")
#1.4-modify header user-agent to display "Mobile"
headers = {
    'User-Agent' : 'Mobile'
}
url2= 'http://httpbin.org/headers'
rh = requests.get(url2,headers=headers)
print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
    name ="new_spider"
    start_urls = ['http://brickset.com/sets/year-1998']
def pharse(self, response):
    css_selector = 'img'
    for x in response.css(css_selector):
        newsel ='@src'
        yield{
            'imageLink':
                x.xpath(newsel).extract_first(),
        }
        Page_selector = '.next a:attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse
            )

#3-test case with apprioriate test funcions. (havent test fully)
import unittest

class TestImage(unittest.TestCase):

    def test_pic(self):
        self.assertEqual(h.status_code, jpg)

    if "__name__" == '__main__':
        unittest.main()