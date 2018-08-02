import requests


def getInfo(url):
    try:
        kv = {'user_agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        print(r.request.headers)

        print(r.text[1000:2000])
    except:
        return "爬取失败"


if __name__ == "__main__":
    url = "https://www.amazon.cn/gp/product/B078FFX8B6/ref=as_li_tf_tl?ie=UTF8&camp=536&creative=3200&creativeASIN=B078FFX8B6&linkCode=xm2&tag=bss09-news6-23"
    getInfo(url)
