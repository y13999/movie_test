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
    for ch in check_str:
        if ord(ch) > 255:
            return False
        if check_str==' ' or check_str=='':
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

def input_path():
    path = input('请输入文件路径：')
    if path == '':
        print('无任何输入，当前执行目录为：', os.getcwd())
        path = os.getcwd()
    else:
        if os.path.exists(path) == True:
            print('目录路径为：', path)
        else:
            print('目录出错。退出')
            sys.exit()
    if path[-1] != os.sep:
        path = path + os.sep
        print('目录路径windows格式为：', path)
    return(path)

if __name__ == "__main__":

    #全局定义
    movie_size_difind = ['720p', '1080p', '2160p', '720P', '1080P', '2160P','1080i', '1080I']
    douban_name_key = r'qcat.*\s*.*>(.*?)\s*</a>'
    douban_ori_name_key = r'span class="subject-cast">原名:(.*?)\s/'
    douban_point_key = r'span class="rating_nums">(.*?)\s*</span>'
    imdb_point_key = r'span itemprop="ratingValue">(.*?)</span>'
    season001=['S00','S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12',
               's00','s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11','s12']
    mark02=0
    '''
    定义file_all的各项名称
    file_all[
    0，序号
    1，原始文件名
    2，转换后的文件名
    3，电影年份
    4，电影格式
    5，豆瓣中文名
    6，豆瓣原始名
    7，豆瓣分数
    8，imdb分数
    9，文件是否以imdb或者douban开头
    10，新文件的文件夹名称
    11，文件夹或者文件标识位，0为文件夹，1为文件
    ]
    '''
    #开始#################
    # 获取该目录下所有文件，存入列表中
    path=input_path()
    filelist001 = os.listdir(path)
    number001 = len(os.listdir(path))
    file_all = [['' for i in range(15)] for j in range(number001)]
    print('文件数：', number001)
    #分析获取文件名等信息
    for b in range(number001):
        file_all[b][0] = b
        file_all[b][1] = filelist001[b]
        # 将文件分割为多个单词的格式
        # 定义分隔符为.全部转换为空格
        newlistname = re.split(r'[._\s]', file_all[b][1])
        # 循环标示位
        mark001 = 1
        movie_name001 = ''
        movie_years001 = ''
        movie_size001 = ''
        for cccc in newlistname:
            if cccc in movie_size_difind:
                movie_size001 = cccc
            if int_it(cccc) in range(1900, 2999):
                movie_years001 = cccc
                mark001 = 0
            elif mark001 == 1:
                movie_name001 = movie_name001 + cccc + ' '
                mark001 = 1
            if cccc  in season001:
                break
        file_all[b][2] = movie_name001[:len(movie_name001) - 1]
        file_all[b][3] = movie_years001
        file_all[b][4] = movie_size001
        if newlistname[0] == 'imdb' or newlistname[0] == 'douban':
            file_all[b][9]=1

    for b in range(number001):
        sleep(random.random() * 1.2)
        if file_all[b][9]==1:
            continue
        aaaa = get_douban_html(file_all[b][2])
        file_all[b][5] = get_douban_chinese_name(douban_name_key, aaaa)
        if (get_douban_chinese_name(douban_name_key, aaaa) != get_douban_origin_name(douban_ori_name_key, aaaa)):
            file_all[b][6] = get_douban_origin_name(douban_ori_name_key, aaaa)
        file_all[b][7] = get_douban_point(douban_point_key, aaaa)
        print(file_all[b][6],'________',is_all_english(file_all[b][6]))
        if (is_all_english(file_all[b][6]) and file_all[b][6]!='') == True:
            print(file_all[b][6])
            dddd = get_imdb_html(file_all[b][6])
            file_all[b][8] = get_imdb_point(imdb_point_key, dddd)
        new_doc_name = ''
        new_doc_name02 = ''
        if os.path.isdir(path + filelist001[b]) == True:
            file_all[b][11]=0
            if (imdb01 := file_all[b][8]) != '':
                if (zwmz01 := file_all[b][5]) != '':
                    if (ywmz01 := file_all[b][6]) != '':
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + ywmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + ywmz01
                    else:
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01
                else:
                    new_doc_name = 'imdb_' + imdb01 + '_' + file_all[b][2]
            elif (douban01 := file_all[b][7]) != '':
                if (zwmz01 := file_all[b][5]) != '':
                    if (ywmz01 := file_all[b][6]) != '':
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + ywmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + ywmz01
                    else:
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01
                else:
                    new_doc_name = 'douban_' + douban01 + '_' + file_all[b][2]
        elif os.path.isfile(path + filelist001[b]) == True:
            file_all[b][11] = 1
            if (imdb01 := file_all[b][8]) != '':
                if (zwmz01 := file_all[b][5]) != '':
                    if (ywmz01 := file_all[b][6]) != '':
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + ywmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + ywmz01
                    else:
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'imdb_' + imdb01 + '_' + zwmz01
                else:
                    new_doc_name = 'imdb_' + imdb01 + '_' + file_all[b][2]
            elif (douban01 := file_all[b][7]) != '':
                if (zwmz01 := file_all[b][5]) != '':
                    if (ywmz01 := file_all[b][6]) != '':
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + ywmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + ywmz01
                    else:
                        if (wjdx01 := file_all[b][4]) != '':
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01 + '_' + wjdx01
                        else:
                            new_doc_name = 'douban_' + douban01 + '_' + zwmz01
                else:
                    new_doc_name = 'douban_' + douban01 + '_' + file_all[b][2]
        else:
            print('出错', path + filelist001[b])
        if (file_all[b][7] =='' and file_all[b][8]=='') or file_all[b][7]==' ':
            new_doc_name=''
        for nouse in new_doc_name:
            if nouse not in [':',':','\\','/','?','*','|']:
                new_doc_name02+=nouse
        file_all[b][10]=new_doc_name02
        if file_all[b][11]==0 and new_doc_name != '':
            for cc001 in range(b-1):
                if new_doc_name02 ==file_all[b][10]:
                    mark02=1
                    print('有重复文件',new_doc_name02,file_all[b][1])
            print(filelist001[b], '重命名为--->', new_doc_name02)
            rename_ok((path + filelist001[b]),(path + new_doc_name02))
        elif file_all[b][11]==1 and new_doc_name != '':
            print(filelist001[b], '移动到--->', new_doc_name02)
            if os.path.exists((path + new_doc_name02))==False:os.mkdir((path + new_doc_name02))                             #新建文件夹
            shutil.move((path + filelist001[b]), (path + new_doc_name02))          #移动文件
        print(file_all[b])


