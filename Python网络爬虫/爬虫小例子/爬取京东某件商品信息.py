import requests

def getHtmlText(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"


if __name__ == "__main__":
    url="https://re.jd.com/cps/item/5089275.html?cu=true&utm_source=cps.youmai.com&utm_medium=tuiguang&utm_campaign=t_1000049399_40729106&utm_term=3cc491b6601c4aaebecb5c7db0176d04&abt=3"
    print(getHtmlText(url))
