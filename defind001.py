import os
import sys
import random
import re
import requests
import shutil
from openpyxl import Workbook
from time import sleep

# 以下是函数###########################################
def is_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_all_english(check_str):
    if check_str==' ' or check_str=='':
        return False
    for ch in check_str:
        if ord(ch) > 255:
            return False
    return True

def rename_ok(sor,dst):
    try:
        os.rename(sor, dst)
    except:
        return print(sor,' can not rename to:',dst)

# 尝试字符串转数字的函数
def int_it(v):
    try:
        return int(v)
    except:
        return v


def find_all_by_pat(pat, string):
    res = re.findall(pat, string)
    return res


def get_douban_chinese_name(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[1]
    except:
        return ' '


def get_douban_origin_name(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[0]
    except:
        return ' '


def get_douban_point(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[0]
    except:
        return ' '


def get_imdb_point(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[0]
    except:
        return ' '


def get_douban_html_doc(url):
    #pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
    head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
    #resopnse = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
    resopnse = requests.get(url, headers=head)
    resopnse.encoding = 'utf-8'
    html_doc = resopnse.text
    return html_doc


def get_douban_html(query_name):
    douban_search_url = 'https://www.douban.com/search?cat=1002&q=%s' % query_name
    douban_search_res = get_douban_html_doc(douban_search_url)
    return douban_search_res


def get_imdb_html_doc(url):
    #pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
    head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
    #resopnse = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
    resopnse = requests.get(url, headers=head)
    resopnse.encoding = 'utf-8'
    html_doc = resopnse.text
    try:
        return html_doc
    except:
        return ' '


def get_imdb_next_url(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return 'https://www.imdb.com' + res_list[0]
    except:
        return ' '


def get_imdb_html(query_name):
    imdb_search_url_01 = 'https://www.imdb.com/find?q=' + query_name + '&ref_=nv_sr_sm'
    # print(imdb_search_url_01)
    imdb_search_res = get_imdb_html_doc(imdb_search_url_01)
    key_word_01 = r'<td class="primary_photo"> <a href="(.*?)"\s>'
    res01 = get_imdb_next_url(key_word_01, imdb_search_res)
    # print(res01[0])
    imdb_search_res_02 = get_imdb_html_doc(res01)
    try:
        return imdb_search_res_02
    except:
        return ' '


# 函数结束########################################
print((random.uniform(0.5,1.1) )* 2)
a=''
b='te st'
c='测试'
d='测试 test'
print(a,'is_all_english:',is_all_english(a))
print(b,'is_all_english:',is_all_english(b))
print(c,'is_all_english:',is_all_english(c))
print(d,'is_all_english:',is_all_english(d))
print(a,'',a)


#aa=get_douban_html('Dark.Phoenix')
#print(aa)

#bb=get_imdb_html('Dark.Phoenix')
#douban_name_key = r'qcat.*\s*.*>(.*?)\s*</a>'
#douban_ori_name_key = r'span class="subject-cast">原名:(.*?)\s/'
#douban_point_key = r'span class="rating_nums">(.*?)\s*</span>'
#imdb_point_key = r'span itemprop="ratingValue">(.*?)</span>'
#print('imdb_point:',get_imdb_point(imdb_point_key,bb))
'''
aa=get_douban_html('宝莱坞机器人之恋')
pat2 = r'qcat.*\s*.*>(.*?)\s*</a>'
pat3=  r'span class="rating_nums">(.*?)\s*</span>'
pat4=r'span class="subject-cast">原名:(.*?)\s/'
chinise_name = get_douban_chinese_name(pat2, aa)
print(chinise_name)
point001=get_douban_point(pat3, aa)
print(point001)
orig001=get_douban_origin_name(pat4,aa)
print(orig001)
print(aa)
'''


'''
n=0
for b in fileist001:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符
    # 设置新文件名
    newname = path + + os.sep + 'a' + str(n + 1) + '.JPG'
    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)
    n += 1
'''
'''
for a in filelist001:
    #print(a)
    file_all.append(path+a)
    if os.path.isdir(path+a):print('文件夹',path+a)
    elif os.path.isfile(path+a):print('文件：',path+a)
    else :print('出错',path+a)
'''
'''path2=os.path.split(path)
print('path2:',path2)
print('path2[1]:',path2[1])
print(os.path.abspath(os.curdir))
print(os.path.dirname(__file__))
print(os.path.dirname(path))'''
