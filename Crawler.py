import urllib3
import json
from WPImage import *
from bs4 import BeautifulSoup

'''
内部爬虫类
当前仅实现API爬取
'''

class Crawler(object):
	sourceWeb = None
	url = None
	webContent = None
	imageList = []
	def __init__(self, sourceWeb, url):
		super().__init__()
		self.sourceWeb = sourceWeb
		self.url = url

	def request(self):
		r = urllib3.PoolManager().request("GET", self.url)
		if r.status == 200:
			self.webContent = r.data.decode('utf-8')

	def parse():
		pass

class AutoCrawler(Crawler):
	def __init__(self, sourceWeb, url):
		super().__init__(sourceWeb, url)

	def parse(self):
		soup = BeautifulSoup(self.webContent, 'lxml')
		if self.sourceWeb == "WallPapersCraft":
			previewList = [x["src"] for x in soup.findAll(class_ = "wallpapers__image")]
			i = 1
			for link in previewList[:9]:
				temp = link.split("_")
				temp[-1] = "1280x720.jpg"
				link = "_".join(temp)
				i = i + 1
				self.imageList.append(WPImage(self.sourceWeb, i, link, 1280, 720))

class APICrawler(Crawler):
	def __init__(self, sourceWeb, url):
		super().__init__(sourceWeb, url)

	def request(self, authorisation):
		r = urllib3.PoolManager().request("GET", self.url, headers = authorisation)
		if r.status == 200:
			self.webContent = r.data.decode('utf-8')

	def parse(self):
		j = json.loads(self.webContent)
		if self.sourceWeb == "Pixabay":
			self.imageList = [WPImage(self.sourceWeb,x["id"],x["largeImageURL"],x["imageWidth"],x["imageHeight"]) for x in j["hits"][:]]
		if self.sourceWeb == "Pexels":
			self.imageList = [WPImage(self.sourceWeb,x["id"],x["src"]["original"],x["width"],x["height"]) for x in j["photos"][:]]
		if self.sourceWeb == "Unsplash":
			self.imageList = [WPImage(self.sourceWeb,x["id"],x["urls"]["regular"],x["width"],x["height"]) for x in j["results"][:]]
