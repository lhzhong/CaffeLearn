#!/usr/bin/env sh
set -e

LOG=/home/cpss/caffe/zhong/KTH/train/rgb/finetune/log/finetune_out.log
/home/cpss/caffe/build/tools/caffe train  --solver=/home/cpss/caffe/zhong/KTH/train/rgb/finetune/finetune_solver.prototxt --weights=/home/cpss/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0 2>&1 |tee $LOG  
