from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
html = urlopen(url)
bsObj = BeautifulSoup(html.read())
print(bsObj.head.title)

