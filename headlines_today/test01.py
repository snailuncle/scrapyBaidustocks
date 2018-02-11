import os
from hashlib import md5
content = 'abc'.encode('utf-8')
print(os.getcwd())
file_path = '{0}/{1}.{2}'.format(os.getcwd() + '\pic', md5(content).hexdigest(), 'jpg')
print(file_path)
with open(file_path, "w") as f:
    f.write("def")
