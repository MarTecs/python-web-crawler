# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: prac 结合一下 BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.erlaile.com")
except :
    print("Page Not Found Or Page Exception")
else:
    if html == None:                            ## 链接打不开或者链接写错了
        print("Server Not Found")
    else:
        bsObj = BeautifulSoup(html.read(), "lxml")
        '''
        使用bs4打印标签内容需要注意，如果标签不存在，有时报错有时返回None
        1. 对于获取不存在标签的子标签将会报错
        2. 对于获取存在标签的不存在子标签将会返回None
        '''
        try:
            title = bsObj.title.title
            #title = bsObj.title.title.title
        except AttributeError as e:
            print(e)
        else:
            if title == None:
                print("Tag was not found")
            else:
                print(title)
