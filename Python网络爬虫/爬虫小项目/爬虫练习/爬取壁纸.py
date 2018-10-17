import os
import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
	headers ={
	"UserAgent":":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
	try:
		r = requests.get(url)
		r.raise_for_status()
		# if r.status_code == 200:
		# 	print("connected")
		r.encoding = "utf-8"
		# print(r.text)
		return r.text
	except:
		print("there is something wrong....")


def getUrlList(html):
	soup = BeautifulSoup(html,'html.parser')
	list = soup.find_all('div',class_ = 'view view-first')
	imglist = []
	for i in list:
		s = str(i.a).split('"')[1]
		t = getHtmlText(s)
		soup1 = BeautifulSoup(t,"html.parser")
		a = soup1.find('div',class_ = 'form-group').find('a')
		# print(a['href'])
		imglist.append(a['href'])
	print(len(imglist))
	return imglist

def downLoad(root,imglist):
	# try:
	if not os.path.exists(root):
		os.mkdir(root)
	for i in imglist:
		name = str(i).split('/')[-1]
		path = root + name
		if not os.path.exists(path):
			r1 = requests.get(i)
			with open(path,'wb') as f:
				f.write(r1.content)
				f.close()
				print("downloading...")
		else:
			print("file is alrady extsis...")
	# except :
	# 	print("there is something wrong...")







if __name__ == '__main__':
	# k = input("what kind of image do you want to download:")
	root = "F://爬虫图片//cat//"
	url = "http://hddesktopwallpapers.in/?s=cat"
	l = getUrlList(getHtmlText(url))
	downLoad(root,l)