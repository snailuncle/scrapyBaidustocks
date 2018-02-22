import math

def producePrime2(max):  
    li = []  


    # 奇数设置为本身,  偶数全部置为0,   2除外
    for i in range(2, max + 1):  
        if i > 2 and i % 2 == 0:  
            li.append(0)  
        else:  
            li.append(i)  
    #所有奇数中的   非质数   筛一筛  筛掉
    for i in range(3, int(math.sqrt(max)) + 1, 2):  
        if li[i - 2] != 0:  
            for j in range(i + i, max + 1, i):  
                li[j - 2] = 0  


    # k = 0
    # for index, name in enumerate(li):

    #     if k == 3:
    #         # print(name)
    #         print('names[{}] = {}'.format(index, name))
    #     if name != 0:
    #         k = k + 1
    # print('质数总数', k)
    k = 0
    for i in li:  
        if i != 0:  
            # print(i)
            # print("前", k)
            k += 1
            # print("后", k)
            if k == 521025:
                print("k=", k, "i=", i)

num = 11000000
producePrime2(num)
