import urllib.request
import urllib.parse
import json
import sys
from bs4 import BeautifulSoup
import re
import os
# url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# data={}
# data['i']='成功'
# data['from']='AUTO'
# data['to']='AUTO'
# data['smartresult']='dict'
# data['client']='fanyideskweb'
# data['salt']='15533325348514'
# data['sign']='852a8ced179ef585e86bec1e6e2a8b3e'
# data['ts']='1553332534851'
# data['bv']='b223e3766c3e6b076e3a46dbe930ec0f'
# data['doctype']='json'
# data['version']='2.1'
# data['keyfrom']='fanyi.web'
# data['action']='FY_BY_CLICKBUTTION'
# data['typoResult']='false'
# data=urllib.parse.urlencode(data).encode('utf-8') 
# head={}
# head['Referer']='http://fanyi.youdao.com'
# head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

# req=urllib.request.Request(url,data,head)
# response=urllib.request.urlopen(req)
# html=response.read().decode('utf-8')
# target=json.loads(html)
# print(target)
# default_encodeing = 'gbk'
# if sys.getdefaultencoding != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)
url='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
# proxy_support=urllib.request.ProxyHandler({'http':'125.46.0.62:53281'})
# opener=urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
req=urllib.request.Request(url)
req.add_header('Referer','https://baike.baidu.com')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')

response=urllib.request.urlopen(req)
html=response.read()
soup=BeautifulSoup(html,'html.parser')
for each in soup.find_all(href=re.compile('view')):
    print(each.text,'->',''.join(['https://baike.baidu.com',each['href']]))

# re.search(r'(fish)\2',"fish")

def openUrl(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    return html

def getImg(html):
    p=r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist=re.findall(p,html)
    try:
        os.mkdir('NewPics')
    except FileExistsError:
        print('文件夹已经存在')
    os.chdir('NewPics')
    for each in imglist:
        fileName=each.split('/')[-1]
        urllib.request.urlretrieve(each,fileName,None)

url='https://tieba.baidu.com/p/3823765471?red_tag=0136158471'
getImg(openUrl(url))