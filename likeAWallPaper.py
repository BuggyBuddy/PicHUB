import WPImage
import WPPlayList
import os
import shutil

recFilePath = os.path.join(os.getcwd(), 'preference')

"""
    复制一个文件夹中的文件到另一个文件夹中
"""
def copyFile(scrFile, dstPath):
    if os.path.isfile(scrFile)
        fPath, fName = os.path.split(scrFile)
        if not os.path.exists(dstPath)
            os.makedirs(dstPath)
        shutil.copy(scrFile, dstPath + fName)

"""
    收藏一个壁纸
    首先将其加入壁纸队列中
    再将其复制到preference文件夹中，用于偏好算法调用
"""
def likeAWallPaper(wallpaper, playList):
    playList.append(wallpaper)
    copyFile(wallpaper.getFilePath(), recFilePath)
