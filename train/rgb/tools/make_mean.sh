#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/cpss/caffe/zhong/KTH/train/rgb #lmdb训练数据位置
DATA=/home/cpss/caffe/zhong/KTH/train/rgb #均值保存位置
TOOLS=/home/cpss/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/train_lmdb $DATA/KTH_rgb_mean.binaryproto

echo "Done."
