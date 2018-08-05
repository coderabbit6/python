import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("异常")
        return None


def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        print(tlt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodlist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    goods = input("输入你要查询的商品名称:")
    deps = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(deps):
        try:
            url = start_url + "&s" + str(44*i)
            print(url)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
printGoodlist(infoList)
