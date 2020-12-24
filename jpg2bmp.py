import PIL
fi = "E:/课程/软件工程/pic.jpg"
fo = "E:/课程/软件工程/0.bmp"
img = PIL.Image.open(fi)
img.save(fo)
