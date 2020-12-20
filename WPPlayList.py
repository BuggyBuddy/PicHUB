import random

class WPPlayList:
    """
    length:壁纸队列长度
    wallpapers:WPImage对象队列
    showing:正被设置或者上次最后被设置的壁纸的序号
    name:壁纸队列的名字
    """
    def __init__(self, name):
        self.length = 0
        self.wallpapers = []
        self.showing = -1
        self.name = name

    def setName(self, name):
        self.name = name

    def append(self, wallpaper):
        self.wallpapers.append(wallpaper)
        self.length = self.length + 1

    def insert(self, index, wallpaper):
        if index < 0 or index > self.length:
            return
        if self.showing >= index:
            self.showing = self.showing + 1
        self.wallpapers.insert(index, wallpaper)
        self.length = self.length + 1

    def delete(self, index):
        if self.length == 0 or index >= self.length or index < 0:
            return
        if self.showing >= index:
            self.showing = self.showing - 1
        del self.wallpapers[index]
        self.length = self.length - 1

    def showIndex(self, index):
        self.showing = index
        self.__show(index)

    def showNext(self, showingMode):
        if showingMode == 'InOrder':
            self.showing = (self.showing + 1) % self.length
        elif showingMode == 'InShuffle':
            randomIndex = self.showing
            while randomIndex == self.showing:
                randomIndex = random.randint(0, self.length - 1)
            self.showing = randomIndex
        else:
            return
        self.__show(self.showing)

    def __show(self, index):
        self.wallpapers[index].changeWP()
