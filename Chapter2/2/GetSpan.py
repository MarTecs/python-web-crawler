# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description:

'''
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
1.这两个函数第1个参数可以是列表，
例如.findAll({"h1","h2","h3","h4","h5"}) 将会返回一个包含指定标签的列表
2.attributes属性参数使用Python字典封装的一个标签若干属性和对应的值
.finaAll("span", { "class": {"green", "red"} }) ##找到class为green和red的span标签
3.recursive设置是否采用递归查找，默认为True，否则只找文档的一级标签
4.text指用标签文本内容去匹配，而不是用标签的属性，可以查看包含指定内容的标签
5.limit为范围限制参数(找到匹配的前几项)，只用于findAll方法，find其实等价于findAll的limit等于1的情形，
6.keywords就是关键词参数，用于获取具有指定属性的标签
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("file:///E:/www.pythonscraping.com.html")
bsObj = BeautifulSoup(html, "lxml")
nameList = bsObj.findAll("span", {"class" : "green"}, False)           ##这个是使用了Python的字典
for name in nameList:
    print(name.get_text())

