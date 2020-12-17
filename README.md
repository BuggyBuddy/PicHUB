Entrance.py分类器、推荐器、爬虫操作
其他文件下载至根目录
可调用函数：
分类器
	获取分类列表与数组    classifer(bool 是否第一次运行)
		输出为1. string[] 分类列表 2. float[] 对于标签的数值

推荐器
	本地推荐器           localRecommender(maxPoss, maxType)

爬虫 
	爬虫类 WPSource
	网址源目前包括{"Pixabay","Pexels","Unsplash", "WallPapersCraft"}
	构造函数             WPSource(string 网站源, string 图片类别, string 搜索词)
	开始爬虫线程         run()
	非线程爬虫           fetch()
	获取下一页搜索结果    nextPage()
	获取第n页搜索结果     toPage(int 页码)
	更改搜索词           changeKeyWord(string 关键词)
	更改网站源           changeSourceWeb(string 网站源)
	记录已使用           markUsed(string 壁纸文件名)
	记录喜欢             markLike(string 壁纸文件名, bool 喜欢)
	返回喜欢列表         getLike()
	库存数量             inStock()
	获取未使用壁纸列表    getImageList()

	壁纸图片类 WPImage 通过壁纸列表访问
		获取标签列表     getLabel()
		添加标签        	addLabel(string 标签)
		获取图片路径     getFilePath()
