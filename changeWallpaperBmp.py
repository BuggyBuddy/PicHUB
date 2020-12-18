import os
import win32api
import win32con
import win32gui

def setWallpaper(path):
        #打开注册表
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        
        #2：拉伸  0：居中  6：适应  10：填充
        win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        
        #
        #win32api.RegSetValueEx(reg_key,"Wallpaper")
        
        #SPIF_SENDWININICHANGE:立即生效
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
        #path为绝对路径

f = open("fi.txt","r")
fi = f.read()
f.close()
fo = "0.bmp"
#转换为bmp文件才能被windows接口接受
fo = os.path.abspath(fo)
#相对路径改绝对路径
setWallpaper(fo)
