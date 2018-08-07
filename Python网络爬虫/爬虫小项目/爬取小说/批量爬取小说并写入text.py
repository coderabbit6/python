import requests
import re,os,time
from bs4 import BeautifulSoup




headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
base_url = 'http://www.qu.la/book/'
def getonepage(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		soup = BeautifulSoup(r.text,"html.parser")
		onepagename = soup.select('bookname')
		print(onepagename)
	except Exception as e:
		print("爬取失败")

if __name__ == '__main__':
	url = base_url + '260825.html'
	getonepage(url)