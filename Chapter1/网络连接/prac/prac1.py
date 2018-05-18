# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用Python进行爬虫

from urllib.request import urlopen
from urllib.error import HTTPError

'''
使用urlopen打开一个链接将会出现两种如下情况：
1. 服务器不存在，将会返回一个None
2. 服务器存在，页面不存在 或者 获取页面的时候报错 ，将会出现异常
'''
try:
    html = urlopen("http://www.erlaile.com/")
except HTTPError as e:
    print(e)
    print("Page Not Found Or Page Exception")
else:
    if html == None:
        print("Server Not Found")
    else:
        print(html.read())
