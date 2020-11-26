import urllib3
import json

class WPImage():
	labelList = []
	size = [0,0]
	def __init__(self, sourceWeb, webID, url, width, height):
		self.sourceWeb = sourceWeb
		self.webID = webID
		self.fileName = sourceWeb + str(webID) + ".jpg"
		self.url = url
		self.size[0] = width
		self.size[1] = height

	def download(self):
		r = urllib3.PoolManager().request('GET', self.url, preload_content = False)
		with open(self.fileName, 'wb') as out:
			out.write(r.data)
		r.release_conn()

	def addLabel(self, label):
		self.labelList.append(label)

	def display(): #返回图片名string
		return self.fileName
