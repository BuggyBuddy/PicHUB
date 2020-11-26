import urllib3
import json
from WPImage import *

'''
内部爬虫类
当前仅实现API爬取
'''

class Crawler(object):
	webContent = None
	imageList = []
	def __init__(self):
		pass
	def request():
		pass
	def parse():
		pass


class APICrawler(Crawler):
	def __init__(self, sourceWeb, url):
		super().__init__()
		self.sourceWeb = sourceWeb
		self.url = url

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



