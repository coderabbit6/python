import requests
import re


# https://pic2.zhimg.com/80/v2-837f13141383705363ec1985c871de35_hd.jpg
# https://pic2.zhimg.com/80/v2-5b796f7146679b87685500910a710b81_hd.jpg
url = "https://www.zhihu.com/question/58954408/answer/219501796"
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
r = requests.get(url,headers = headers)
r.encoding = "utf-8"
print(r.status_code)
html = r.text
# print(html)
urllist = re.findall(r'data-original="https://pi.*?r.jpg"',html)
# print(urllist)
# print(urllist[0].split('"')[1])
a = 0
for i in urllist:
	# print(i)
	a = a+1
	path = "F://壁纸//爬取壁纸//知乎//"+str(a)+".jpg"
	s = i.split('"')[1]
	b = requests.get(s)
	r.encoding = "utf-8"
	# print(r.status_code)
	with open(path,"wb") as f:
		f.write(b.content)
		f.close()
		print("正在下载第"+str(a)+"张图片")
# root = "F://壁纸//爬取壁纸//"
# r = requests.get(url, headers=headers)
# r.encoding = "utf-8"
# print(r.status_code)
# html = r.text
# print(html)
# urllist = []
# urllist = re.findall(r'src=.*\.img', html)
# print(len(urllist))
# print(urllist)
# for i in range(len(urllist)):