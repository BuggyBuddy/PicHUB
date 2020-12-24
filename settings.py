import pickle
from queue import Queue

class Settings():
    def __init__(self):
        self.pathPics = ""#待写
        self.listOfQueues = []
        self.queue2Display = Queue()
        self.isContinousPlayiing = False
        self.isCyclePlaying = True
        self.page = 0
        self.pageMax = 0
    def getSettings(self,path):
        f = open(path,"rb")
        self = pickle.load(f)
        f.close()
    def updateSettings(self,path):
        obj=pickle.dumps(self)
        with open(path,"ab")as f:
            f.write(obj)
    def refresh(self):
        self.isCyclePlaying = True
