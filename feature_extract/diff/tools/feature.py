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
data = sio.loadmat('/home/cpss/caffe/zhong/KTH/feature_extract/diff/feature/feature_fc6.mat')
data = data['feats']
data = preprocessing.scale(data)

file_name='/home/cpss/caffe/zhong/KTH/feature_extract/diff/feature/label.txt'
labels=[]
with open(file_name) as file_object:
    for line in file_object:
        labels.append(line)
labels = np.array(labels,dtype=int)
data_labels = labels[:42100]

data_train,data_test,label_train,label_test = train_test_split(data,data_labels,test_size=0.3)

model = SVC()
model.fit(data_train,label_train)

duration = (time.time()-start_time)
print model.score(data_test,label_test)
print 'time:' + str(duration) + 's'
