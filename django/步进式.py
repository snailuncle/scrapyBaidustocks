# -*- coding: utf-8 -*-
# print ('{0:<10}{1}'.format(123,8888888))
FORMAT = '{0:<10}{1}'
k = 1
MAX = 100000000
print(FORMAT.format(1,2), end='\n')
aList = []
for i in range(0, MAX+1):
    aList.append(0)
 
for i in range(3, MAX+1, 2): # 从3开始的所有  奇数
    for j in range(i+i, MAX+1, i):
        aList[j] = 1
 
for i in range(3, MAX+1, 2):
    if(aList[i]==0):
        k += 1
        print(FORMAT.format(k,i), end='\n')
