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
        for Action in ActionNames[:int(len(ActionNames)*0.7)]:  
            ActionName=os.path.join(ActionPath,Action)
            x=os.listdir(ActionName)
            if len(x)>0:
                for xt in x:
                    fullfilename=os.path.join(ActionName,xt)
                    ActionList.append(fullfilename)
          
    return ActionList 


def GetFileListTest(ActionPath):  
    ActionList=[]  
    ActionNames=os.listdir(ActionPath)  
    if len(ActionNames)>0:  
        for Action in ActionNames[int(len(ActionNames)*0.7):]:  
            ActionName=os.path.join(ActionPath,Action)
            x=os.listdir(ActionName)
            if len(x)>0:
                for xt in x:
                    fullfilename=os.path.join(ActionName,xt)
                    ActionList.append(fullfilename)
          
    return ActionList 

#train label
ActionPath='KTH_flow_color/'
ActionNum=os.listdir(ActionPath)
train='/home/cpss/caffe/zhong/KTH/train/flow/train.txt'
train_txt=open(train,'w')
k=0
for i in ActionNum:
    imagefile=GetFileListTrain(ActionPath+i)
    for img in imagefile:
        str1=img+' '+str(k)+'\n'
        train_txt.writelines(str1)
    k=k+1
train_txt.close()  

#test label
ActionPath='KTH_flow_color/'
ActionNum=os.listdir(ActionPath)
train='/home/cpss/caffe/zhong/KTH/train/flow/val.txt'
train_txt=open(train,'w')
k=0
for i in ActionNum:
    imagefile=GetFileListTest(ActionPath+i)
    for img in imagefile:
        str1=img+' '+str(k)+'\n'
        train_txt.writelines(str1)
    k=k+1
train_txt.close()  
print'Successfully generated labels'
