from Crawler import *
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import inspect
import ctypes
'''
使用方法：
建立WPSource对象，构造函数输入(网址源，类型，关键词)
	网址源目前包括{"Pixabay","Pexels","Unsplash", "WallPapersCraft"}
	类型默认为temp


通过getImageList获取WPImage图像列表
'''
import pichub

class WPSource(object):
	WPList = [] #壁纸列表
	WPusedList = []
	crawlerType = None
	authorisation = None
	parserElement = None
	perPage = 9

	def __init__(self, sourceWeb, genre = "temp", keyWord = None):
		self.page = 1
		self.sourceWeb = sourceWeb
		self.genre = genre
		self.keyWord = keyWord
		self.thread = threading.Thread(target = self.fetch)

	def run(self):
		#self.stop_thread(self.thread)
		self.thread = threading.Thread(target = self.fetch)
		self.thread.start()

	def fetch(self):
		url = self.createURL()
		if self.crawlerType == "API":
			crawler = APICrawler(self.sourceWeb, url)
			crawler.request(self.authorisation)
			crawler.parse()
		if self.crawlerType == "Auto":
			crawler = AutoCrawler(self.sourceWeb, url)
			crawler.request()
			crawler.parse()
		for x in crawler.imageList:
			x.download(self.genre)
			print("download")
		self.WPList.extend(crawler.imageList) #append
		pichub.showWallPaper()
		print("hahaha")
		

	def nextPage(self):
		self.page = self.page + 1

	def toPage(self, page):
		self.page = page

	def changeSourceWeb(self, sourceWeb):
		self.sourceWeb = sourceWeb

	def changeKeyWord(self, keyWord):
		self.keyWord = keyWord

	def changePerPage(self, perPage):
		self.perPage = perPage

	def getImageList(self):
		return self.WPList

	def markUsed(self, name):
		mark = next((x for x in self.WPList if x.fileName == name), None)
		self.WPusedList.append(mark)
		self.WPList.remove(mark)

	def markLike(self, name, like):
		for x in WPusedList:
			if x.fileName == name:
				x.like = True

	def getLikeList(self):
		return [x.like == True for x in self.WPusedList]

	def inStock(self):
		return self.WPList.size()

	def createURL(self):
		if self.sourceWeb == "Pixabay":
			self.crawlerType = "API"
			API_KEY = "18782431-49126f726e89ec4331126b0fa"
			parameter = {
				"q": self.keyWord,
				"lang": "en",
				"image_type": "all",
				"orientation": "horizontal",
				"category": "all",
				"colors": "all",
				"editors_choice": "false",
				"order": "latest",
				"per_page": str(self.perPage),
				"page": str(self.page)
				}
			url = "https://pixabay.com/api/?key="+API_KEY
			for key in parameter:
				url = url + "&" + key + "=" + parameter[key]
			return url

		if self.sourceWeb == "Pexels":
			API_KEY = "563492ad6f9170000100000141baaf1898864c69b8f747000709fb7f"
			self.crawlerType = "API"
			self.authorisation = {"Authorization":API_KEY}
			parameter = {
				"query": self.keyWord,
				"orientation": "landscape",
				"per_page": str(self.perPage),
				"page": str(self.page)
			}
			url = "https://api.pexels.com/v1/search?query=" + self.keyWord
			for key in parameter:
				url = url + "&" + key + "=" + parameter[key]
			return url

		if self.sourceWeb == "Unsplash":
			API_KEY = "q81I4S31cD_ro5loDpeH2brUlOBUs8nQDBxrHbqfrxo"
			self.crawlerType = "API"
			parameter = {
				"query": self.keyWord,
				"orientation": "landscape",
				"per_page": str(self.perPage),
				"page": str(self.page)
			}
			url = "https://api.unsplash.com/search/photos?client_id="+API_KEY
			for key in parameter:
				url = url + "&" + key + "=" + parameter[key]
			return url

		if self.sourceWeb == "WallPapersCraft":
			self.crawlerType = "Auto"
			url = "https://wallpaperscraft.com/search/?order=downloads&page=" + str(self.page) + "&query=" + self.keyWord
			return url


class WebRecommender(object):
	def __init__(self, keyWord):
		self.url = "https://unsplash.com/s/photos/" + keyWord
		self.crawler = Crawler("Recommender", self.url)
		self.crawler.request()
		self.recommendList = self.parse()

	def parse(self):
		soup = BeautifulSoup(self.crawler.webContent, 'lxml')
		return [x.contents[0] for x in soup.findAll(class_ = "_2634o _1CBrG _1ByhS _2bG1V xLon9")]

	def getRecommendList(self):
		return self.recommendList

def main():
	#wpSource = WPSource("WallPapersCraft", "Animal", "wolf")
	wr = WebRecommender("cougar, puma, catamount, mountain lion, painter, panther, Felis concolor")
	print(wr.getRecommendList())

if __name__ == "__main__":
    main()