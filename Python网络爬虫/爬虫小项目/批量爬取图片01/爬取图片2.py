import requests
import re
import os

def getHtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        return r.text
    except:
        print("爬取失败")


def getimagelist(ilist, html):
    try:
        ilist = re.findall(r'http.*1x', html)
        return ilist
    except:
        print("")


def downlode(ilist, root, count):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        for i in range(len(ilist)):
            count += 1
            a = ilist[i].split('/')[-1].split('.')[0]
            path = root + a + ".jpg"
            if not os.path.exists(path):
                url2 = ilist[i]
                m = requests.get(url2)
                with open(path, "wb") as f:
                    f.write(m.content)
                    f.close()
                    print("{0}张图片下好了".format(count))
            else:
                print("文件已存在")
    except:
        print(" ")
        return None


if __name__ == '__main__':
    keyw = input("请输入要下载的图片:")
    url = "https://www.pexels.com/search/"
    root = "F://壁纸//爬取壁纸//" + keyw + "//"
    imglist = []
    page = 3
    count = 0
    for i in range(1, page):
        fallurl = url + keyw + "/?page=" + str(i)
        html = getHtmltext(fallurl)
        imglist = getimagelist(imglist, html)
        downlode(imglist, root, count)
