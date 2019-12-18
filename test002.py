file_all=[ ['' for i in range(0,10)] for j in range(0,6)]
file_all[2][3]=10
for j in range(6):
    for i in range(10):
        print(file_all[j][i],end='_')
    print()
