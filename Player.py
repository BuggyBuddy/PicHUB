import threading
import WPPlayList
import os
from WPImage import WPImage


listOfWPPlayList=[]
listNum=0
def noneFunc():
    return

class Player:
    """
    intervalTime:自动播放间隔时间（单位秒）
    mode:播放模式
    wallpaperList:被播放的队列
    timer:用来实现自动播放的定时器
    autoPlaying:自动播放的标志
    """
    intervalTime = 300
    mode = 'InOrder'
    wallpaerList = WPPlayList.WPPlayList("Temp")
    timer = threading.Timer(300, noneFunc)
    autoPlaying = 0

    @staticmethod
    def setWPList(wallpaperList):
        Player.wallpaperList = wallpaperList

    @staticmethod
    def setIntervalTime(time):
        Player.intervalTime = time

    @staticmethod
    def playInOrder():
        Player.mode = 'InOrder'
        Player.__play()

    @staticmethod
    def playInShuffle():
        Player.mode = 'InShuffle'
        Player.__play()

    @staticmethod
    def playIndex(index):
        if Player.autoPlaying:
            Player.stop()
            Player.wallpaperList.showIndex(index)
            Player.__play()
        else:
            Player.wallpaperList.showIndex(index)

    @staticmethod
    def stop():
        Player.autoPlaying = 0
        Player.timer.cancel()

    @staticmethod
    def __play():
        Player.timer = threading.Timer(Player.intervalTime, Player.__playNext)
        Player.autoPlaying = 1
        Player.timer.start()

    @staticmethod
    def __playNext():
        Player.wallpaperList.showNext(Player.mode)
        Player.timer.cancel()
        Player.timer = threading.Timer(Player.intervalTime, Player.__playNext)
        Player.timer.start()
        
    @staticmethod
    def __onStartUp():
        if os.path.exists('setting.txt') and os.path.getsize('setting'):
            with open('setting.txt','r')as file_obj:
                listNum=file_obj.readline().rstrip()
                for i in range(listNum):
                    listLength=int(file_obj.readline().restrip())
                    tempList=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                    for j in range(listLength):
                        sourceWeb=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                        webID=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                        url=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                        width=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                        height=WPPlayList.WPPlaylist(file_obj.readline().restrip())
                        tempImage=WPImage(sourceWeb, webID, url, width, height)
                        templist.append(temoImage)
                    ListOfWPPlayList.append(tempList)
                    
    @staticmethod
    def __onShutDown():
        if os.path.exists('setting.txt') :
            with open('setting.txt','w')as file_obj:
                file_obj.write([str(listNum),'\n'])
                for i in range(listNum):
                    tempList=ListOfWPPlayList[i]
                    file_obj.write([str(tempList.len),'\n'])
                    for j in range(tempList.len):
                        file_obj.write([templist[j].sourceWeb,'\n'])
                        file_obj.write([templist[j].webID,'\n'])
                        file_obj.write([templist[j].url,'\n'])
                        file_obj.write([templist[j].shape[0],'\n'])
                        file_obj.write([templist[j].shape[1],'\n'])
                        
                        

