import os
import sys
import random
import re
import requests
from openpyxl import Workbook
from time import sleep

def find_all_by_pat(pat, string):
    res = re.findall(pat, string)
    return res

def get_html_doc(url):
    pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
    head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
    resopnse = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
    resopnse.encoding = 'utf-8'
    html_doc = resopnse.text
    return html_doc

def get_douban_html(query_name):
    url = 'https://www.douban.com/search?cat=1002&q=%s' % query_name
    douban_search_res = get_html_doc(url)
    return douban_search_res

def get_chinese_name(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[1]
    except:
        return ' '

def get_director_name(pat, doc):
    res = find_all_by_pat(pat, doc)
    try:
        return res[0].split('/')[1]
    except:
        return ' '

movie_info={
    'title_english':'',
    'title_chinese':'',
    'title_other':'',
    'point_imdb':'',
    'point_douban':'',
    'year':'',
    'size':'',
    'languge':''
          }

url_imdb_search=''
url_douban_search='https://www.douban.com/search?cat=1002&q=%s'

print(os.getcwd())
path = input('请输入文件路径：')
if path=='':
    print('无任何输入，当前执行目录为：',os.getcwd())
    path=os.getcwd()
else:
    if os.path.exists(path)==True:
        print('目录路径为：',path)
    else:
        print('目录出错。退出')
        sys.exit()
if path[-1]!=os.sep:
    path=path+os.sep
    print('目录路径windows格式为：',path)
# 获取该目录下所有文件，存入列表中
filelist001=os.listdir(path)
filelist002=[]
number001= len(os.listdir(path))
print('文件数：',number001)

for b in range(number001):
    print(b,'',filelist001[b])
    newlistname001='newlist'+str(b)
    list(newlistname001)
    newlistname001=filelist001[b].split('.')
    for c in newlistname001:
        if str.isdigit(c)==false:
            newlistname002.append(c)


    print(newlistname)


