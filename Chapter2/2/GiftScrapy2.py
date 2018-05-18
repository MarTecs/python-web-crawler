# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description:

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

for sibling in bsObj.find("table", { "id" : "giftList" } ).tr.next_siblings:
    print(sibling)