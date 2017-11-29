#!/usr/bin/env sh 
set -e

MODEL=/home/cpss/caffe/zhong/KTH/feature_extract/rgb/snapshot/50000KTH_rgb_model_iter_5000.caffemodel
PROTOTXT=/home/cpss/caffe/zhong/KTH/feature_extract/rgb/imagenet_val.prototxt
LAYER=fc6
LMDB_OUTPUT_PATH=/home/cpss/caffe/zhong/KTH/feature_extract/rgb/feature/feature_lmdb
BATCH_SIZE=844

/home/cpss/caffe/build/tools/extract_features.bin $MODEL $PROTOTXT $LAYER $LMDB_OUTPUT_PATH $BATCH_SIZE lmdb GPU 0
