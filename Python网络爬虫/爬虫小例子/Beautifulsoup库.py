from bs4 import BeautifulSoup
import requests

url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D1%A7%CF%B0&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
headers = {
	"UserAgent":":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

}
r = requests.get(url,headers = headers)
print(r.status_code)
soup = BeautifulSoup(r.text,"html.parser")
print(len(soup.head.contents))
# help(requests)