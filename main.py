#1-reconnaissance lab 10b

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

#2-mapping lab 10c

#2.1-Scrapy web-crawler with appropriate parser "response.css"
import scrapy
class NewSpider(scrapy.Spider):
        name = "new_spider"
        start_urls = ['http://192.168.1.1/index.html']
        def parse(self, response):
            xpath_selector = '//img'
            for x in response.xpath(xpath_selector):
                newsel = '@src'
                yield {
                    'Image Link': x.xpath(newsel).extract_first(),
                }

# To recurse next page
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                )

#2.3-Store retrieve info in JSON
import urllib, json

url = "put url here"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)

#3.1-recursively extract JPG images on all known links
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
import urllib.request
import re

print("Input link: ")
link = input()

url = urllib.request.urlopen(link)
content = url.read()
imgs = bs(content)
links = [a['href'] for a in imgs.final_all('a',href=re.compile('http.*\.jpg'))]

#3.2-display list of img links
print(len(links))
print("\n".join(links))

#4-test case with apprioriate test funcions.





