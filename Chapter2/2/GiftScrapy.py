# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description:

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("file:///E:/page3.html")
html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml") ##使用lxml HTML解析器
bsObj2 = BeautifulSoup(html2, "lxml")

## 子标签
for child in bsObj.find("table", { "id" : "giftList" }).children:
    print(child)

print("-----------------------------")

# for child in bsObj2.find("table", { "id" : "giftList" } ).children:
#     print(child)

print("----------------------------------------------------------------------------------------")
## 后代标签
for houdai in bsObj2.find("table", { "id" : "giftList" } ).descendants:
    print(houdai)