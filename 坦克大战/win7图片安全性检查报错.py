import os
# rootPath是需要转换的图片所在的根目录
rootPath = r"D:\scrapyProject\pic"
# magick.exe所在的路径
commandTool = os.getcwd()+os.sep+"tools"+os.sep+'magick.exe'
print(commandTool)
# 获得rootPath目录下所有图片文件的全路径
def FindExamAllFiles():
    tmp = []
    for root, dirs, files in os.walk(rootPath):
        for filepath in files:
            imgFileFullPath = os.path.join(root, filepath)
            if imgFileFullPath.endswith('.png'):
                tmp.append(imgFileFullPath)
    return tmp

if __name__ == "__main__":
    pngPathList = FindExamAllFiles()
    for pngPath in pngPathList:
        # 拼凑cmd命令
        command = "{0} {1} {2}".format(commandTool, pngPath, pngPath)
        os.system(command)
