from urllib.request import urlopen

from bs4 import BeautifulSoup
# 这里会有两种异常：网页不存在（404）或者服务器异常（500）
try:
    html = urlopen("http://www.sivan0222.cn")
    bsObj = BeautifulSoup(html.read())
except HTTPError as e:
    print(e)
    # 返回空值，执行另一种方案或者终止
else:
    # 继续运行
    print(bsObj.head.title)