import requests
import re
from bs4 import BeautifulSoup


# https://ws1.sinaimg.cn/large/6af89bc8gw1f8t0e12yv5j20ag081dg6.jpg
url = "http://www.doutula.com/search?keyword=代码"
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    # 'Referer': 'http://www.mm131.com'
               }
i = 0
r = requests.get(url,headers=Hostreferer)
print(r.status_code)
r.encoding = r.apparent_encoding
html = r.text
# print((html))
soup = BeautifulSoup(html,"html.parser")
# print(soup)
p = soup.find_all('img',class_="img-responsive lazy image_dtb")
# print(p)
root = "F://壁纸//爬取壁纸//mm131//"
for a in p:
    # print(a)
    i +=1
    href = a['data-backup']
    # print(href)
    path = root + str(i) + ".jpg"
    m = requests.get(href,headers=Hostreferer)
    with open(path,'wb') as f:
        f.write(m.content)
        f.close()