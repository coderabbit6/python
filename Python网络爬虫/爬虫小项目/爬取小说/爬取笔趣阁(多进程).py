import requests
import os
from bs4 import BeautifulSoup
from multiprocessing import Pool

#  http://www.biquge.com.tw/paihangbang/
#获取一章并写入文件
def geturllist(url):
	#获取排行榜中全本小说的全部链接并存在列表中
	print("正在获取页面......")
	try:
		url_list = []
		r = requests.get(url,headers = headers)
		r.raise_for_status()
		r.encoding = 'gbk'
		soup = BeautifulSoup(r.text, 'html.parser')
		fall = soup.find(attrs = {'class':'box b4'})
		# print(type(fall))
		fall1 = fall.ul
		fall2 = fall1.find_all(name = 'li')
		# print(fall2)
		print("正在获取列表......")
		# c = 0
		for li in fall2:
			# c +=1
			# print("第{0}部......".format(c))
			url_list.append(str(li.a).split('"')[1])
		return url_list
		# print(fall1)
		# print(fall.name)
		# print(fall)
		# fall1 = fall.find_all()
		# print(fall1)

	except Exception as e:
		raise e


def getone(url,path):
	print("\r第{0}部正在下载......".format(d),end = ' ')
	try:
		r = requests.get(url,headers = headers)
		r.raise_for_status()
		r.encoding = 'gbk'
		soup = BeautifulSoup(r.text,'html.parser')
		tage = soup.find(attrs ={'id':'list'}).dl
		# print(tage)
		tage1 = tage.find_all(name = 'dd')
		# print(tage1)
		count = 0
		path = root + soup.title.string.split('_')[0] + '.txt'
		for dd in tage1:
			count = count + 1
			one_url = str(dd.a).split('"')[1]
			try:
				r = requests.get(url_base + one_url,headers = headers)
				r.raise_for_status()
				r.encoding = 'gbk'
				soup = BeautifulSoup(r.text, 'html.parser')
				tage = soup.find(attrs = {'id':'content'})
				title = soup.find(attrs = {'class':'bookname'}).h1.string
				text =title + '\r\n' + tage.text
				try:
					if not os.path.exists(root):
						os.mkdiv(root)
					with open(path, 'ab+') as f:
						f.write((text + '\r\n').encode('utf-8'))
						print("第{0}章{1}\t\t\t下载完成".format(count,title))
						break
				except Exception as e:
					raise e
			except Exception as e:
				raise e
		f.close()
		print("")
		print("")
		print("")
	except Exception as e:
		raise e


if __name__ == '__main__':
	url = 'http://www.biquge.com.tw/paihangbang/'
	headers = {
	'Host':'www.biquge.com.tw',
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
	root = "F://小说//"
	url_list=[]
	path = ''
	url_list = geturllist(url)
	url_base = 'http://www.biquge.com.tw'
	d = 0
	pool = Pool(5)
	for url in url_list:
		d += 1
		pool.apply_async(getone, args=(url, path))
	pool.close()
	pool.join()
