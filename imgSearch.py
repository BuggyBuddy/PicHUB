import random
import requests
import json
import sys
import os
import path
import PIL
#from PIL import Image
import win32file
import win32con
import win32api
import win32gui



# Query Images
searchURL = 'https://unsplash.com/napi/search?client_id=%s&query=%s&page=1'
client_id = 'fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7'
categories = ['nature','flowers','wallpaper','landscape','sky']
searchURL = searchURL % (client_id,random.choice(categories))
response = requests.get(searchURL)
print(searchURL)
response.content.decode("utf-8")
print(u'正在从Unsplash上搜索图片...')

print(response)
# Parse Images
#data = json.loads(response.content.decode(encoding='utf8'))
data = json.loads(response.text,strict = False)
results = data['photos']['results']
print(u'已为您检索到图片共%s张' % str(len(results)))
results = list(filter(lambda x:float(x['width'])/x['height'] >=1.33,results))
result = random.choice(results)
resultId = str(result['id'])
resultURL = result['urls']['regular']

# Download Images
print(u'正在为您下载图片:%s...' % resultId)
basePath = sys.path[0]
if(os.path.isfile(basePath)):
    basePath = os.path.dirname(basePath)
baseFolder = basePath + '\\Download\\'
if(not os.path.exists(baseFolder)):
    os.makedirs(baseFolder)
jpgFile = baseFolder + resultId + '.jpg'
bmpFile = baseFolder + resultId + '.bmp'
response = requests.get(resultURL)
with open(jpgFile,'wb') as file:
    file.write(response.content)
img = PIL.Image.open(jpgFile)
img.save(bmpFile,'BMP')
os.remove(jpgFile)



print(u'正在设置图片:%s为桌面壁纸...' % resultId)
key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
    "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") 
#2拉伸适应桌面,0桌面居中
win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmpFile, 1+2)
print(u'成功应用图片:%s为桌面壁纸'  % resultId)

