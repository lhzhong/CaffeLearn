# coding: utf-8

import os  
  
def IsSubString(SubStrList,Str):  
    flag=True  
    for substr in SubStrList:  
        if not(substr in Str):  
            flag=False  
      
    return flag 



def GetFileListTrain(ActionPath):  
    ActionList=[]  
    ActionNames=os.listdir(ActionPath)  
    if len(ActionNames)>0:  
        for Action in ActionNames[:int(len(ActionNames)*0.3)]:  
            ActionName=os.path.join(ActionPath,Action)
            x=os.listdir(ActionName)
            if len(x)>0:
                for xt in x[:int(len(x)*0.5)]:
                    fullfilename=os.path.join(ActionName,xt)
                    ActionList.append(fullfilename)
          
    return ActionList 
 

#train label
ActionPath='/home/cpss/caffe/zhong/KTH/data/KTH_RGB/'
ActionNum=os.listdir(ActionPath)
data='/home/cpss/caffe/zhong/KTH/feature_extract/rgb/feature/data.txt'
label='/home/cpss/caffe/zhong/KTH/feature_extract/rgb/feature/label.txt'
data_txt=open(data,'w')
label_txt=open(label,'w')
k=0
n=0
for i in ActionNum:
    imagefile=GetFileListTrain(ActionPath+i)
    for img in imagefile:
        str1=img+'\n'
	str2=str(k)+'\n'
        data_txt.writelines(str1)
	label_txt.writelines(str2)
	n=n+1
    k=k+1
data_txt.close()  
label_txt.close()  
 
print 'Successfully generated datas and labels'
print 'totla progress '+ str(n) + ' photos'
