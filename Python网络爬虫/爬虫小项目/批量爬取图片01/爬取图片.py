import requests

# /photos/398/big-tiger-whiskers-animal-feline.jpg


# 获取搜索后页面结果
def getHtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
    except:
        print("异常")
        return None

# 从结果中解析每张图片链接并存储到列表里


def getImglist(ilist,html):
	pass

# 通过每张图片链接下载图片并存到文件中
def downlodeimg(path,html):
	pass


if __name__ == '__main__':

	url = "https://www.pexels.com/search/"

	imglist = []

	keyw = input("输入你要下载的图片类型:")

	fallurl = url + keyw

	getHtmltext(fallurl)

	getImglist(imglist,html)

	downlodeimg(path,imglist)
