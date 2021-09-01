#to have some time in between
import time

# 1-reconnaissance lab 10b

#1.1-perform "get" request on web 
import requests

url = 'https://brickset.com/sets/year-1998'
r = requests.get(url)

#1.2-display "OK"
print("Status code:")
print("\t*", r.status_code)

#1.3-display web header
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t", x, ":", h.headers[x])
print("**********")

#1.4-modify header user-agent to display "Mobile"
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

#pause
time.sleep(1)

#2 using scrapy webcrawler (lab 10c)
import scrapy
from scrapy.http.request import Request

#2.1-allowing spider to crawl 
class ProjectSpider(scrapy.Spider):
    name = 'Project'
    start_urls = ['http://brickset.com/sets/year-1998']

#2.2-sending request to the web
    def start_requests(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0.3"}
        for url in self.start_urls:
            yield Request(url, headers=headers)

#2.3-asking web to extract image links
    def parse(self, response):
        SET_SELECTOR = '.set'
        for x in response.css(SET_SELECTOR):
            IMAGE_SELECTOR = "img ::attr(src)"
            yield {
                "image": x.css(IMAGE_SELECTOR).extract_first(),
            }

#2.4-recursively extract JPG images on all known links 
        NEXT_PAGE_SELECTOR = '.next a::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

#3-unit testing for http status code to be 200
import unittest


class TestImage(unittest.TestCase):

    def test_pic(self):
        self.assertEqual(h.status_code, 200)

    if __name__ == '__main__':
        unittest.main()

#ways to run all your file

#copy code and run directly from pycharm to obtain part 1 (http headers and get request) and part 3 (unit testing) 
#use the code -> scrapy runspider (filename).py -s USER_AGENT="mozilla/5.0" -o (any name).json -t json. This is to send the output to json file
#cat (any name).json to show the json output
