def eladuosai(n):
    l = list(range(1,n+1))     # l是一个 1-n  的 list
    print(l)
    l[0] = 0
    print(l)
    for i in range(2,n+1):      # 从2开始的所有数
        print("现在判断的数字是i=", str(i-1), "   l["+str(i-1)+"]=", l[i-1])
        if l[i-1] != 0 :        # 0
           
            for j in range(i*2,n+1,i):  # start = i*2, end = n+1, step = i     i=2时, start = 4, end = 11, i = 2
                print(j)
                l[j-1] = 0
    result = [x for x in l if x != 0]  # 遍历一次l  如果不等于0 就返回这个数  这就是所有的素数
    return result

e = eladuosai(100)
print(e)
