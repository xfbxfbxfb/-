"""
作者：梦里北极光
时间：2021/11/5
功能：选定一个文件夹路径对文件进行遍历文件名，输出目录下所哟有文件名，文件名可选择增加路径
感受：很简单，但很久没碰代码，都不会了
"""

import os
#填写扫描文件的文件目录
print("请输入需要扫描的文件夹绝对路径")
Path = input()
#Path = "F:\备份E盘\python文件"
#填写需要过滤的格式
print("请输入你需要过滤的格式：如：.py")
GS = input()
#GS = '.py'
#填写数据保存位置
print(os.getcwd())
df = open(os.getcwd()+"\\文件名输出.txt","w")
#判断是只打印文件名还是加绝对路径
print("遍历文件夹打印文件夹包含绝对路径输入1,只打印文件名输入2")
num = int(input())
'''
过滤文件输出所有此文件到txt文件中
'''
#获取文件对象，返回元组，元组里有目录路径，目录名（下一级），文件名（下一级）
walk = os.walk(Path)
#创建类
class GetFile():
    #初始化函数
    def __init__(self,walk):
        self.walk = walk
    #定义函数获取带绝对路径的文件名
    def GetFile1(self):
        for dirpath, dirname, filename in walk:
            # 打印所有文件
            for filename_1 in filename:
                # print(filename_1)
                # 文件后缀为.py的
                if filename_1.endswith(GS):
                    # print(filename_1)
                    # 打印出文件路径
                    data = os.path.join(dirpath, filename_1)
                    print(data)
                    df.write(data + "\n")

    #只打印文件名
    def GetFile2(self):
        for dirpath, dirname, filename in walk:
            # 打印所有文件
            for filename_1 in filename:
                # print(filename_1)
                # 文件后缀为.py的
                if filename_1.endswith(GS):
                    # print(filename_1)
                    # 打印出文件路径
                    data = filename_1
                    print(data)
                    df.write(data + "\n")

#新建立对象
FN = GetFile(walk)
#调用打印所有文件夹下的文件
if num==1:
    FN.GetFile1()
elif num==2:
    FN.GetFile2()
else:
    print("您输入有误，请重新执行脚本")
df.close()





# for dirpath,dirname,filename in walk:
#     #打印所有文件
#     for filename_1 in filename:
#        # print(filename_1)
#         #文件后缀为.py的
#         if filename_1.endswith(GS):
#             #print(filename_1)
#             #打印出文件路径
#             data = os.path.join(dirpath,filename_1)
#             print(data)
#             df.write(data+"\n")











