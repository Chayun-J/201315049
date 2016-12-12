# -*- coding:utf-8 -*-

#! /usr/bin/python2

from urllib import quote
from urllib import urlopen
import re, sys, csv
import scrapy
from bs4 import BeautifulSoup

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

def query_url(keyword, start_date, end_date):
	"""
	keyword: 검색어, start_date: 시작일, end_date: 끝일
	위의 자료를 입력받아 파싱 및 urlencode하여 유효한 검색 주소를 반환한다.

	"""
	euckr_keyword = quote(keyword)
	dashed_start_date = start_date[:4] + '-' + start_date[4:6] + '-' + start_date[6:]
	dashed_end_date = end_date[:4] + '-' + end_date[4:6] + '-' + end_date[6:]

	return 'http://news.naver.com/main/search/search.nhn?query={0}&st=news.all&q_enc=EUC-KR&r_enc=UTF-8&r_format=xml&rp=none&sm=title.basic&ic=all&so=datetime.dsc&stDate=range:{1}:{2}&detail=0&pd=4&r_cluster2_start=1&r_cluster2_display=10&start=1&display=10&startDate={3}&endDate={4}&dnaSo=rel.dsc'.format(euckr_keyword, start_date, end_date, dashed_start_date, dashed_end_date)

keyword = sys.argv[1] # 첫번재 전달인자
start_date = sys.argv[2] # 두번째 전달인자
end_date = sys.argv[3] # 세번째 전달인자
savefile = sys.argv[4] # 네버째 전달인자

target_url = query_url(keyword, start_date, end_date) # 검색주소를 target_url에 저장

html = urlopen(target_url).read() # target_url 페이지를 열어 html내용을 얻는다.
try:
	total_page = re.findall('1\s~\s\d+\s\/\s((?:\d|\,)+)', html)[0] # 총 검색개수가 나오는 정보를 정규표현식으로 찾아 얻는다.
except:
	print u'검색결과가 없습니다'
	sys.exit()	
total_page = int(total_page.replace(',', '')) # 숫자에 있는 콤마 제거
last_page = total_page / 10 + 1 # 한페이지 기사 10개 므로 10으로 나누어 총 몇 페이지 인지 계산.

url_list = [] # 검색한 url들 저장할 리스트

class NewsSpider(scrapy.Spider):
	"""
	start_urls 에 있는 페이지 부터 시작하여 page를 하나씩 올려가면서 파싱한다.
	파싱한 url은 url_list에 저장한다. 재귀적으로 파싱을 지속한다.
	"""
	name = 'news'
	start_urls = [
		target_url,
	]
	page_num = 1
 
	def parse(self, response):

		for naver_news in response.xpath('//div[@class="srch_result_area"]/descendant::a[@class="go_naver"]'):
			"""yield {
			'link':naver_news.xpath('@href').extract_first(),
			}
			"""
			url_list.append(naver_news.xpath('@href').extract_first())

		self.page_num += 1

		next_page = target_url + '&page={0}'.format(self.page_num)
		
		if self.page_num <= last_page:
			yield scrapy.Request(next_page, callback=self.parse)


contents = []



class DataSpider(scrapy.Spider):
	"""
	start_url에 이전에 저장한 url_list를 써서 모든 url들을 돌아가면서 파싱한다.
	xpath를 활용하여 기사 제목, 주소, 본문을 가져오며 정규표현식으로 기사본문중 키워드와 몇개가 매치하는지 확인한다.
	이후 contents 에 자료를 저장한다.
	"""
	name = 'save_data'
	
	"""f = open('news.csv', 'r')
	url_list = []
	for url in f.readlines()[1:]:
		url_list.append(url.strip())
	f.close()
	"""

	start_urls = url_list

	def parse(self, response):
		soup = BeautifulSoup(response.xpath('//div[@id="newsEndContents"]|//div[@id="articleBodyContents"]|//div[@id="articeBody"]').extract_first(), 'lxml')
		"""yield {
			u'기사주소': response.url,
			u'기사제목': response.xpath('//title/text()').extract_first(),
			u'키워드 숫자': len(re.findall(u'홍명보', soup.text))
		}
		"""
		contents.append([response.url, response.xpath('//title/text()').extract_first().encode('euc-kr') ,len(re.findall(keyword.decode('euc-kr'), soup.text))])


#2개의 크롤링을 순서대로 진핸한다.
configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks

def crawl():
	yield runner.crawl(NewsSpider)
	yield runner.crawl(DataSpider)
	reactor.stop()

crawl()
reactor.run()


#csv라일로 저장한다.
with open(savefile, 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Article address', 'Article subject', 'Number of keyword({0})'.format(keyword)])
	for content in contents:
		writer.writerow(content)
