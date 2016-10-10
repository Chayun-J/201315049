regex,xpath,css selector,BeautifulSoup

1.
regex
import urllib
response = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200')
_html = response.read()
print response.info()
print len(_html)

import re
p=re.compile('href="(http://.*?)"')
res=p.findall(_html)
print len(res)
for item in res:
 print item

p=re.compile('<h1>(.*?)</h1>')
h1=p.findall(_html)
for i in h1:
 print i

2.
xpath

import urllib
response = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200')
_html = response.read()

from lxml import etree
_htmlTree = etree.HTML(_html)
result = etree.tostring(_htmlTree, pretty_print=True, method="html")

nodes = _htmlTree.xpath('//*[@href]')
print len(nodes)

for node in nodes:
 print node.attrib

3.
css selector

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('https://www.google.com/finance/historical?q=KRX%3AKOSPI200')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
results = sel(html)

for item in results:
 print item.get('href'), item.text

4.
BeautifulSoup
from BeautifulSoup import *
soup=BeautifulSoup(_html)
strongtags=soup('strong')
for tag in strongtags:
    print tag

from urllib import urlopen
from bs4 import BeautifulSoup
_html = urlopen("https://www.google.com/finance/historical?q=KRX%3AKOSPI200")
bsObj = BeautifulSoup(_html, "lxml")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

