from Crawler import *

'''
输入：网址源，搜索关键字

可获取返回的WPList，类型为python list
'''

class WPSource(object):
	WPList = [] #壁纸列表
	crawlerType = None
	authorisation = None
	parserElement = None
	def __init__(self, sourceWeb, keyWord):
		self.sourceWeb = sourceWeb
		self.keyWord = keyWord
		url = self.createURL()
		if self.crawlerType == "API":
			crawler = APICrawler(self.sourceWeb, url)
			crawler.request(self.authorisation)
			crawler.parse()
			for x in crawler.imageList:
				x.download()
		self.WPList = crawler.imageList

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
				"per_page": "20",
				"page": "1"
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
				"per_page": "20",
				"page": "1"
			}
			url = "https://api.pexels.com/v1/search?query=" + self.keyWord
			for key in parameter:
				url = url + "&" + key + "=" + parameter[key]
			return url

		if self.sourceWeb == "Unsplash":
			pass

def main():
	keyWord = input()
	wpSource = WPSource("Pexels", keyWord)

if __name__ == "__main__":
    main()