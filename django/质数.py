import math


n = 1
def prime(num):
    square_num = math.floor(num ** 0.5)
    for i in range(2, (square_num+1)):
        if (num % i) == 0:
            break
    else:
        print(num, '是质数')
NUM = 100
for i in range(2, NUM):
    


