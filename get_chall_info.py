import re
import requests

# 获取试炼链接
def getchallHtml(url):
  html3 = requests.get(url)
  html3.encoding = 'utf-8'
  html3 = html3.text
  return html3

# 获取试炼图片链接的字符串
def getchallImg(html3):
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg|https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.png)', html3)
  for url3 in imglist:
    return url3

def sethtml3():
  html3 = str(getchallHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9711350&wiki_id=1085660&is_share=1"))
  return html3


# print(getchallImg(sethtml3()))
