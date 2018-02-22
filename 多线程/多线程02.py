from socket import *
import sys
import time

ports = [21, 23, 25, 53, 69, 80, 135, 137, 139, 1521, 1433, 3306, 3389]

# HOST = sys.argv[1]
HOST = '192.168.12.102'

print("Please waiting...\n")
t1 = time.time()


for p in ports:
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect((HOST, p))
        print(str(p) + " -> opened")

    except error:
        print(str(p) + " -> not open")
    finally:
        tcpCliSock.close()
        del tcpCliSock

print('interval:', time.time()-t1)
    
