import requests
import os
# url = input("输入图片地址:")
url = "https://images.freeimages.com/images/large-previews/fcc/smoke-alone-1639248.jpg"
root = "F://壁纸//爬取壁纸//"
path = root + url.split('/')[-1]
print(url)
def getimag(url):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path ,"wb") as f:
                f.write(r.content)
                f.close()
                print("存储成功")
        else:
            print("文件已经存在")

            # print(r.status_code)
            # r.raise_for_status()
            # r.encoding = r.apparent_encoding
            # print(len(r.text))
    except:
        return "爬取失败"


if __name__ == "__main__":
    # url = "http://desk.zol.com.cn/bizhi/7209_89278_2.html"
    getimag(url)