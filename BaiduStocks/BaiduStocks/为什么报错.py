# -*- coding: utf-8 -*-
import sys
count = 0
for i in range(300):
    print(i)
    count = count + 1
    if count > 100:
        sys.exit("Error message")

    try:
        with open("stocksTest.txt", 'a') as f:
            f.write(count + '\n')
    except Exception as e:
        print(e)
    # except BaseException:
        # print("error")
        # continue
