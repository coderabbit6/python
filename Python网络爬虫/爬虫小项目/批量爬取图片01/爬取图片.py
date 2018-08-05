import requests
import re
import os
# /photos/398/big-tiger-whiskers-animal-feline.jpg
# https://www.pexels.com/search/cat/?page=5&seed=2018-08-04+22%3A38%3A00++0000&format=js&seed=2018-08-04%2022:38:00%20+0000
# 获取搜索后页面结果
def getHtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        return r.text
    except:
        print("异常")
        return None

# 从结果中解析每张图片链接并存储到列表里


def getImglist(ilist, html):
    try:
        ilist = re.findall(r'http.*1x', html)
		# print(len(ilist))
		# print(type(ilist))
		# print(ilist)
        return ilist
    except:
        print(" ")

# 通过每张图片链接下载图片并存到文件中
def downlodeimg(path, imaglist):
	try:
	    if not os.path.exists(root):
            os.mkdir(root)
		for i in range(len(imaglist)):
			path = root + "i"
			url3 = imaglist[i]
			if not os.path.exists(path):
				r = requests.get(url3)
				with open(path, "wb") as f:
					f.write(r.content)
					# print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
					f.close()
					print("存储成功")
			else:
				print("文件已经存在")
    except:
        return None



if __name__ == '__main__':
    url = "https://www.pexels.com/search/"
    root = "F://壁纸//爬取壁纸//猫//"
    imglist = []
    page = 2
    keyw = input("输入你要下载的图片类型:")
    for i in range(page):
        fallurl = url + keyw + "/?page=" + i
        html = getHtmltext(fallurl)
        imglist = getImglist(imglist, html)
downlodeimg(root, imglist)
