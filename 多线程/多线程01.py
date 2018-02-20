#-*-coding:utf-8-*-


import threading, time


def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        time.sleep(0.001)
    print(sum)


start_time = time.time()
sum(1000)
sum(1000)

interval_first = time.time() - start_time
print(interval_first)















