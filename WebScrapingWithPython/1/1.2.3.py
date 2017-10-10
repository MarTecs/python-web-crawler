from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
#html = urlopen(url)                 # 这里可能会发生 网页在服务器不存在 或者 服务器错误

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
else:

bsObj = BeautifulSoup(html.read())
print(bsObj.head.title)

