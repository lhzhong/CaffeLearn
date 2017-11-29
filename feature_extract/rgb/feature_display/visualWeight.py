import numpy as np
import matplotlib.pyplot as plt
import sys,os
caffe_root = '/home/zhong/caffe/'
os.chdir(caffe_root) #改变当前路径
sys.path.insert(0, caffe_root + 'python')
import caffe

# set display defaults
plt.rcParams['figure.figsize'] = (10, 10)        # large images
plt.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
plt.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a (potentially misleading) color heatmap

caffe.set_mode_cpu()
model_def = caffe_root + 'mytest/KTH_RGB/deploy.prototxt'
model_weights = caffe_root + 'mytest/KTH_RGB/snapshot/model_iter_50000.caffemodel'
net = caffe.Net(model_def, model_weights, caffe.TEST)

#net.blobs['data'].data.shape

net.forward()
#[(k, v.data.shape) for k, v in net.blobs.items()]
for k, v in net.blobs.items() :
    print k +',' +str(v.data.shape)

#[(k, v[0].data.shape) for k, v in net.params.items()]
for k, v in net.params.items():
      print k + ',' +str(v[0].data.shape)

def vis_square(data):
    """Take an array of shape (n, height, width) or (n, height, width, 3)
       and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)"""
    
    # normalize data for display
    data = (data - data.min()) / (data.max() - data.min())
    
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data, padding, mode='constant', constant_values=1)  # pad with ones (white)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    
    plt.imshow(data); plt.axis('off')

#第1层con显示
filters = net.params['conv1'][0].data
#vis_square(filters.transpose(0, 2, 3, 1))
vis_square(filters.reshape(96*3,11,11)[:256])
#第2层con显示
filters = net.params['conv2'][0].data
#vis_square(filters.transpose(0, 2, 3, 1))
vis_square(filters.reshape(256*48,5,5)[:256])
#第3层con显示
filters = net.params['conv3'][0].data
#vis_square(filters.transpose(0, 2, 3, 1))
vis_square(filters.reshape(384*256,3,3)[:256])
#第4层con显示
filters = net.params['conv4'][0].data
#vis_square(filters.transpose(0, 2, 3, 1))
vis_square(filters.reshape(384*192,3,3)[:256])
#第5层con显示
filters = net.params['conv5'][0].data
#vis_square(filters.transpose(0, 2, 3, 1))
vis_square(filters.reshape(256*192,3,3)[:256])
