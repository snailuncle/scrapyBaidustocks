def eladuosai(n):
    l = list(range(1, n+1))
    print(l)
    l[0] = 0
    print(l)
    for i in range(2, n+1):
        print("现在判断的数字是i=", str(i-1), "   l["+str(i-1)+"]=", l[i-1])
        if l[i-1] != 0:
            for j in range(i*2, n+1, i):
                print(j)
                l[j-1] = 0
    result = [x for x in l if x != 0]
    return result


e = eladuosai(10)
print(e)
