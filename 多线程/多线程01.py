import threading
print('')


class My_thread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global n
        if lock.acquire():

            print('Thread:', n)
            n += 1
            lock.release()


n = 0
t = []
lock = threading.Lock()
for i in range(10):
    my = My_thread()
    t.append(my)

for i in range(10):
    t[i].start()

# for i in range(10):
#     t[i].join()
