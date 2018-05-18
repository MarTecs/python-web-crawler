# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 在这个例子中，我们创建了一个 getTitle 函数，可以返回网页的标题，如果获取网页的时候遇到问题就返回一个 None 对象

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.erlaile.com")
if title == None:
    print("Title could not be found.")
else:
    print(title)