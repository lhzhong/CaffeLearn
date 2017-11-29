#!/usr/bin/env bash

#############################################
#1.make sure ffmpeg is installed
#2.place this file at your data directory menu
#############################################

FFMPEGBIN=ffmpeg
UCF101DIR=UCF101
for f in ${UCF101DIR}/*/*.avi; do
  sub_dir=${f#*/}
  new_dir=UCF101_RGB/${sub_dir::-4}
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
