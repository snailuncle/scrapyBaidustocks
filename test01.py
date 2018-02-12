
print('hello')
import shutil,os

# 删除目录使用如下函数：

# shutil.rmtree('d:/dd')

# 移动文件或者文件夹到另外一个地方：

# shutil.move('d:/c.png','e:/')

path = os.getcwd()
directory = '/pic'
folder_full_name = 'D:/scrapyProject/pic/'
if  os.path.exists(folder_full_name):
    print('存在')
    # 创建文件夹
    # os.makedirs(folder_full_name)
    shutil.rmtree(folder_full_name)  
    # os.mkdir(folder_full_name)  
else:
    print('不存在')
    os.makedirs(folder_full_name)
