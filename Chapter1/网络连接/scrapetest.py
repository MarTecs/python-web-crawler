# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: Python如何实现网路爬虫

from urllib.request import urlopen
html = urlopen("https://github.com/sivanWu0222/python-web-crawler/tree/master")
print(html.read())