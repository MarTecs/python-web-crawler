from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
#html = urlopen(url)                 # 这里可能会发生 网页在服务器不存在 或者 服务器错误

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
else:
    if html is None:                 # 这里当采用urlopen函数打开一个url的时候，如果Url不存在将会返回一个None
        print("Url is not found")
    bsObj = BeautifulSoup(html.read())
    try:
        a = bsObj.head.title
    except AttributeError as e:
        print("Tag was not found")
    else:
        if a == None:
            print("Tag is not appeared")
        else:
            print(a)


