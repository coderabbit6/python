import requests
url = "http://www.baidu.com/s"


def getinfo(url):
    try:
        kv = {'wd': a}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        print(r.status_code)
        print(len(r.text))
    except:
        return "爬取失败"


if __name__ == "__main__":
    # url = "http://www.baidu.com/s?wd="
    a = input("输入想搜索的内容:")
    print(a)
    # getinfo(url+a)
    getinfo(url)