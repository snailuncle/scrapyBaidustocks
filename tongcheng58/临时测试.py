from threading import Thread, Lock
#import time
g_num=0
def test1():
    global g_num
    for i in range(1000000):
#        mutexFlag=mutex.acquire(True)
#        if mutexFlag:
        g_num+=1
#            mutex.release()
    print('----test1----g_num=%d%g_num')
    

#mutex=Lock()
p1=Thread(target=test1)
p1.start()
p1.join()
p2=Thread(target=test1)
p2.start()
p2.join()
print('----g_num=%d----'%g_num)
