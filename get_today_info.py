import re
import requests

# 获取日报链接
def gettodayHtml(url):
  html4 = requests.get(url)
  html4.encoding = 'utf-8'
  html4 = html4.text
  return html4

# 获取日报图片链接的字符串
def gettodayImg(html4):
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg|https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.png)', html4)
  for url4 in imglist:
    return url4

def sethtml4():
  html4 = str(gettodayHtml("http://www.tianque.top/d2api/today/"))
  return html4

# print(gettodayImg(sethtml4()))
