import urllib.request
import urllib.parse
import json
import sys
from bs4 import BeautifulSoup
import re
import os
import requests


def openUrl(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('gbk')
    return html


def getImg(html):
    print(html)


target = 'https://www.biqukan.com/1_1094/5403177.html'


def getT(target):
   req = requests.get(url=target)
   html = req.text
   bf = BeautifulSoup(html, 'html.parser')
   text = bf.find_all('div', class_='showtxt')
   print(text[0].text.replace('\xa0'*7, '\n\n'))

# print(req.text)
# getImg(openUrl(target))
# getT(target)


def getList():
      server = 'http://www.biqukan.com'
      target = 'http://www.biqukan.com/1_1094/'
      req = requests.get(url=target)
      html = req.text
      bf = BeautifulSoup(html, 'html.parser')
      text = bf.find_all('div', class_='listmain')
      af = BeautifulSoup(str(text[0]), 'html.parser')
      a = af.find_all('a')
      for each in a:
         print(each.text, server+each.get('href'))


def get_contents(target):
      req = requests.get(url=target)
      html = req.text
      bf = BeautifulSoup(html)
      texts = bf.find_all('div', class_='showtxt')
      if texts.__len__() > 0:
         text = texts[0].text.replace('\xa0'*7, '\n\n')
         return text
      else:
         return ''

def getList():
      server = 'http://www.biqukan.com'
      target = 'http://www.biqukan.com/1_1094/'
      req=requests.get(url=target)
      html=req.text
      bf=BeautifulSoup(html,'html.parser')
      text=bf.find_all('div',class_='listmain')
      af=BeautifulSoup(str(text[0]),'html.parser')
      a=af.find_all('a')
      try:
        os.mkdir('小说')
      except FileExistsError:
        print('文件夹已经存在')
      os.chdir('小说')
      for each in a[416:516]:
         with open(each.text+'.txt','a',encoding='utf-8') as f:
            url=server+each.get('href')
            txt=get_contents(url)
            f.write(each.text+'\n')
            f.write(url+'\n')
            f.writelines(txt)
            print(each.text,server+each.get('href')," 下载完成")

getList()

