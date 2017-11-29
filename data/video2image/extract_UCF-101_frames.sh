#!/usr/bin/env bash

#############################################
#      What you need to do
#1.modify the UCF-101 data directory
#2.make sure ffmpeg is installed
#3.place this file at your data directory menu
#############################################

FFMPEGBIN=ffmpeg
UCF101DIR=UCF101
for f in ${UCF101DIR}/*/*.avi; do
  cur_dir=${f#*/}
  new_dir=UCF101_RGB/${cur_dir::-4}
  echo -----
  echo Extracting frames from ${f} into ${new_dir}...
  if [[ ! -d ${new_dir} ]]; then
    echo Creating directory=${new_dir}
    mkdir -p ${new_dir}
  fi
  ${FFMPEGBIN} -i ${f} ${new_dir}/image_%4d.jpg
done

echo -------------------------------------------
echo Done!
