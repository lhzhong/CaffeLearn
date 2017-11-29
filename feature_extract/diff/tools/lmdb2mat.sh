#!/usr/bin/env sh

LMDB=/home/cpss/caffe/zhong/KTH/feature_extract/diff/feature/feature_lmdb # lmdb文件路径
BATCHNUM=842
BATCHSIZE=50
# DIM=290400 # feature长度，conv1
# DIM=43264 # conv5
DIM=4096  # fc6
OUT=/home/cpss/caffe/zhong/KTH/feature_extract/diff/feature/feature_fc6.mat #mat文件保存路径

python /home/cpss/caffe/zhong/KTH/feature_extract/diff/tools/lmdb2mat.py $LMDB $BATCHNUM $BATCHSIZE $DIM $OUT
