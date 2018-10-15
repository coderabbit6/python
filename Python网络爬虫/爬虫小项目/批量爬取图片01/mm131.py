import requests
import time
url = "http://www.mm131.com"
root = "F://壁纸//爬取壁纸//mm131//1//"
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mm131.com'
               }
for i in range(1, 50):
    # time.sleep(2)
    fullurl = url + str(i) + ".jpg"
    path = root + str(i) + ".jpg"
    r = requests.get(fullurl, headers=Hostreferer)
    print(r.status_code)
    with open(path, "wb") as f:
        f.write(r.content)
        f.close()

# 好像可以了

