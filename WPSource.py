from Crawler import *

'''
使用方法：
建立WPSource对象，构造函数输入(网址源，类型，关键词)
	网址源目前包括{"Pixabay","Pexels","Unsplash"}
	类型默认为temp


通过getImageList获取WPImage图像列表
'''

class WPSource(object):
	WPList = [] #壁纸列表
	crawlerType = None
	authorisation = None
	parserElement = None
	def __init__(self, sourceWeb, genre = "temp", keyWord = None):
		self.page = 1
		self.sourceWeb = sourceWeb
		self.genre = genre
		self.keyWord = keyWord

	def run(self):
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
		self.WPList.append(crawler.imageList) #append

	def nextPage(self):
		self.page = self.page + 1

	def changeSourceWeb(self, sourceWeb):
		self.sourceWeb = sourceWeb

	def createURL(self):
		if self.sourceWeb == "Pixabay":
			self.crawlerType = "API"
			API_KEY = "18782431-49126f726e89ec4331126b0fa"
			parameter = {
				"q": self.keyWord,
				"lang": "en",
				"image_type": "all",
				"orientation": "all",
				"category": "all",
				"colors": "all",
				"editors_choice": "false",
				"order": "popular",
				"per_page": "9",
				"page": str(self.page)
				}
			url = "https://pixabay.com/api/?key="+API_KEY+"&pretty=true"
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
				"per_page": "9",
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
				"per_page": "9",
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

	def getImageList(self):
		return self.WPList

def main():
	wpSource = WPSource("WallPapersCraft", "Animal", "wolf")

if __name__ == "__main__":
    main()