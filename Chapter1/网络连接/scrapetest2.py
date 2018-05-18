# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 对上一个例子使用BeautifulSoup改写

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read())
print(bsObj.title)