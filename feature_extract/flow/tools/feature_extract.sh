#!/usr/bin/env sh 
set -e

MODEL=/home/cpss/caffe/zhong/KTH/feature_extract/flow/snapshot/KTH_flow_model_iter_50000.caffemodel
PROTOTXT=/home/cpss/caffe/zhong/KTH/feature_extract/flow/imagenet_val.prototxt
LAYER=fc6
LMDB_OUTPUT_PATH=/home/cpss/caffe/zhong/KTH/feature_extract/flow/feature/feature_lmdb
BATCH_SIZE=842

/home/cpss/caffe/build/tools/extract_features.bin $MODEL $PROTOTXT $LAYER $LMDB_OUTPUT_PATH $BATCH_SIZE lmdb GPU 0
