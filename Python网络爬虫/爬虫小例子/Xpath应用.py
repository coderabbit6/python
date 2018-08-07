import requests
from lxml import etree


url = 'http://www.biquge.com.tw/6_6595/8391973.html'
try:
	r = requests.get(url, timeout = 30)
	print(r.status_code)
except:
	print("超时")
