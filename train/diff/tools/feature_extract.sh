#!/usr/bin/env sh 
set -e

./build/tools/extract_features.bin mytest/smalltest/model_iter_50000.caffemodel mytest/smalltest/deploy.prototxt conv5 mytest/KTH_conv5 100 lmdb CPU
