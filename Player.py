import threading
import WPPlayList

class Player:
    """
    intervalTime:自动播放间隔时间（单位秒）
    mode:播放模式
    wallpaperList:被播放的队列
    timer:用来实现自动播放的定时器
    autoPlaying:自动播放的标志
    """
    intervalTime = 300;
    mode = 'InOrder'
    wallpaerList = WPPlayList()
    timer = threading.Timer()
    autoPlaying = 0

    def setWPList(self, wallpaperList):
        self.wallpaperList = wallpaperList

    def setIntervalTime(self, time):
        self.intervalTime = time

    def playInOrder(self):
        self.mode = 'InOrder'
        self.__play()

    def playInShuffle(self):
        self.mode = 'InShuffle'
        self.__play()

    def playIndex(self, index):
        if self.autoPlaying:
            self.stop()
            self.wallpaperList.showIndex(index)
            self.__play()
        else:
            self.wallpaperList.showIndex(index)

    def stop(self):
        self.autoPlaying = 0
        self.timer.cancel()

    def __play(self):
        self.timer = threading.Timer(self.intervalTime, self.__playNext)
        self.autoPlaying = 1
        self.timer.start()

    def __playNext(self):
        self.wallpaperList.showNext(self.mode)
        self.timer.start()
