# -*- coding: utf-8 -*-
"""
Created on 2019.4.27

@author: buaa.zhoupeng
"""

import os,shutil

file_path="./train_datas/labelme_json/"
new_traindata="./new_traindata/"
trash="./trash"
cv2_mask="./cv2_mask"
list_list=os.listdir(file_path)
file_counts=len(list_list)
print("在"+str(file_path)+"下的文件个数为：" +str(file_counts))


'''
删除label_names.txt中行数为1的
'''

for i in range (file_counts):
    file_path_label=file_path+str(i+1)+"_json/"+"label_names.txt"
    if os.path.exists(file_path+str(i+1)+"_json/"): 
        count = len(open(file_path_label, 'r').readlines())    
        print(str(i+1)+"_json's "+"line:",count)
    if count!=2:
        print("TODO:移动"+str(i+1)+"_json文件夹")
        '''
        #shutil.move 到新的文件夹中，如果不存在的话可以创建一个，
        #但是第一个文件夹中的数据将会全部拿出来
        #因为shutil.move创建一个新的文件夹的时间是大于shutil.move移动到一个新的文件夹的时间的
        '''
        if not os.path.exists(trash):
            os.mkdir(trash)
        shutil.move(file_path+str(i+1)+"_json",trash)
print("删除后的文件总数是：",len(os.listdir(file_path)))


'''
将删除完后的_json文件夹按连续递增排序
'''

for index,value in enumerate(os.listdir(file_path)):
    print(index,value)
    if not os.path.exists(new_traindata):
        os.mkdir(new_traindata)
    os.rename(file_path+"/"+str(value),
              new_traindata+str((index+1))+str("_json"))
'''
对new_traindata中的1_json...中的label.png进行编号
'''
list_list=os.listdir(new_traindata)
file_counts=len(list_list)
for i in range(file_counts):
    
    file_count=list_list[0].split('_')[0]
    file_path_label=new_traindata+str(i+1)+"_json/"+"label.png"#此处可以优化为寻找以.png格式的文件路径
#    if os.path.isfile(file_path_label):
    if 1:
        new_file_path_label=new_traindata+str(i+1)+"_json/"+str(i+1)+".png"
        os.rename(file_path_label,new_file_path_label)
        '''
        将new_file_path_label复制到cv2_mask目录下
        '''
        if not os.path.exists(cv2_mask):
            os.mkdir(cv2_mask)
        shutil.move(new_file_path_label,cv2_mask)
        
    else:
        pass

