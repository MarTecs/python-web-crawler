from urllib.request import urlopen

from bs4 import BeautifulSoup
# 这里会有两种异常：网页不存在（404）或者服务器不存在（urlopen返回一个None）

try:
    html = urlopen("http://www.sivan0222.cn")
    if html is None:
        print("url is not found")
    else:
        bsObj = BeautifulSoup(html.read())

except HTTPError as e:
    print(e)
    # 返回空值，执行另一种方案或者终止
else:
    # 继续运行
    print(bsObj.head.title)