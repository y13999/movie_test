'''
file_all=[ ['' for i in range(0,10)] for j in range(0,6)]
file_all[2][3]=10
for j in range(6):
    for i in range(10):
        print(file_all[j][i],end='_')
    print()
'''
import re

test1='70周年阅兵'
test2='Batman.Hush.2019.1080p.WEB-DL.H264.AC3-EVO.chn'
test3='Batman.Hush 2019 1080p.WEB-DL.H264.AC3-EVO.chn'
print(re.split(r'[.|_|\s]', test1))
print(re.split(r'[.|_|\s]', test2))
print(re.split(r'[.|_|\s]', test3))

for nouse in ntest2:
    if nouse not in test2
        print(nouse)