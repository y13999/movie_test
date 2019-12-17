import os
import sys
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
'''
for a in filelist001:
    #print(a)
    filelist002.append(path+a)
    if os.path.isdir(path+a):print('文件夹',path+a)
    elif os.path.isfile(path+a):print('文件：',path+a)
    else :print('出错',path+a)
'''

for b in range(number001):
    print(b,'',filelist001[b])
    newlistname='newlist'+str(b)
    list(newlistname)
    newlistname=filelist001[b].split('.')
    print(newlistname)

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

'''path2=os.path.split(path)
print('path2:',path2)
print('path2[1]:',path2[1])
print(os.path.abspath(os.curdir))
print(os.path.dirname(__file__))
print(os.path.dirname(path))'''
