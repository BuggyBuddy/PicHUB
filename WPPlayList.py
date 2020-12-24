import threading
import WPPlayList

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
        timer = threading.Timer(Player.intervalTime, Player.__playNext)
        Player.autoPlaying = 1
        timer.start()

    @staticmethod
    def __playNext():
        Player.wallpaperList.showNext(Player.mode)
        Player.timer.start()
