#!/usr/bin/env sh
set -e

LOG=/home/cpss/caffe/zhong/KTH/train/flow/log/out.log
/home/cpss/caffe/build/tools/caffe train  --solver=/home/cpss/caffe/zhong/KTH/train/flow/solver.prototxt -gpu 0 2>&1 |tee $LOG  
