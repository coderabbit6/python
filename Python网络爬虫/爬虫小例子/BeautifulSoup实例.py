from bs4 import BeautifulSoup
import requests
import os
'''
获取一章


'''

root = 'F://小说//'
url = 'http://www.biquge.com.tw/6_6595/8391973.html'
try:
	r = requests.get(url)
	print(r.status_code)
	r.raise_for_status()
	r.encoding = 'gbk'		#转码
	soup = BeautifulSoup(r.text,'html.parser')
	# print(soup.prettify)
	# print(soup.title.string.split(str = '_')[0])
	m = str(soup.title.string).split('_')     #切片
	# print(type(m))
	text = m[0] + '\r\n'     #切片
	p = soup.find_all(attrs = {'id':'content'})
	for br in p:
		text +=br.get_text()
except Exception as e:
	print("爬取失败")

# print(text)
	
path = root + m[1] + ".txt"
try:
	if not os.path.exists(root):
		os.mkdir(root)
	with open(path, 'ab+') as f:
		f.write(text.encode('utf-8'))
		f.close()
		print("下载成功")
except Exception as e:
	raise e
