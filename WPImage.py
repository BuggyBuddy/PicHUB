import urllib3
import json
import os

class WPImage():
	genre = None
	labelList = []
	size = [0,0]
	rootPath = "wallpaper\\"
	def __init__(self, sourceWeb, webID, url, width, height):
		self.sourceWeb = sourceWeb
		self.webID = webID
		self.fileName = sourceWeb + str(webID) + ".jpg"
		self.url = url
		self.size[0] = width
		self.size[1] = height

	def download(self, genre):
		self.genre = genre
		r = urllib3.PoolManager().request('GET', self.url, preload_content = False)
		if not os.path.exists(self.rootPath + genre):
			os.mkdir(os.path.join(self.rootPath, genre))
			print("created")
		with open(self.rootPath + genre + "\\" + self.fileName, 'wb') as out:
			out.write(r.data)
		r.release_conn()

	def addLabel(self, label):
		self.labelList.append(label)

	def getFilePath(self): #返回图片相对路径
		return os.path.join(self.rootPath, self.genre, self.fileName)

	def getLabelList(self):
		return self.labelList
