import re
import requests

# 获取老九链接
def getxurHtml(url):
  html2 = requests.get(url)
  html2.encoding = 'utf-8'
  html2 = html2.text
  return html2

# 获取老九图片链接的字符串
def getxurImg(html2):
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg|https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.png)', html2)
  for url2 in imglist:
    return url2

def sethtml2():
  html2 = str(getxurHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9711351&wiki_id=1085660&is_share=1"))
  return html2

# print(getxurImg(sethtml2()))
