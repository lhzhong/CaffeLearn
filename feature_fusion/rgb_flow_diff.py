#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:50:07 2017

@author: zhong
"""

import scipy.io as sio
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import time

start_time = time.time()
data_rgb = sio.loadmat('/home/cpss/caffe/zhong/KTH/feature_fusion/rgb_feature_fc6.mat')
data_rgb = data_rgb['feats']
data_rgb = preprocessing.scale(data_rgb)

data_flow = sio.loadmat('/home/cpss/caffe/zhong/KTH/feature_fusion/flow_feature_fc6.mat')
data_flow = data_flow['feats']
data_flow = preprocessing.scale(data_flow)

data_diff = sio.loadmat('/home/cpss/caffe/zhong/KTH/feature_fusion/diff_feature_fc6.mat')
data_diff = data_diff['feats']
data_diff = preprocessing.scale(data_flow)

file_name='/home/cpss/caffe/zhong/KTH/feature_fusion/rgb_label.txt'
labels_rgb=[]
with open(file_name) as file_object:
    for line in file_object:
        labels_rgb.append(line)
labels_rgb = np.array(labels_rgb,dtype=int)
labels_rgb = labels_rgb[:42200].reshape(42200,1)

file_name='/home/cpss/caffe/zhong/KTH/feature_fusion/flow_label.txt'
labels_flow=[]
with open(file_name) as file_object:
    for line in file_object:
        labels_flow.append(line)
labels_flow = np.array(labels_flow,dtype=int)
labels_flow = labels_flow[:42100].reshape(42100,1)

file_name='/home/cpss/caffe/zhong/KTH/feature_fusion/diff_label.txt'
labels_diff=[]
with open(file_name) as file_object:
    for line in file_object:
        labels_diff.append(line)
labels_diff = np.array(labels_diff,dtype=int)
labels_diff = labels_diff[:42100].reshape(42100,1)

data = np.vstack((data_rgb,data_flow,data_diff))
data_labels = np.vstack((labels_rgb,labels_flow,labels_diff)).ravel()

data_train,data_test,label_train,label_test = train_test_split(data,data_labels,test_size=0.3)

model = SVC()
model.fit(data_train,label_train)

duration = (time.time()-start_time)
print model.score(data_test,label_test)
print 'time:' + str(duration) + 's'
