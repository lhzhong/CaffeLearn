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
model_def = caffe_root + 'mytest/smalltest/deploy.prototxt'
model_weights = caffe_root + 'mytest/smalltest/snapshot/model_iter_50000.caffemodel'
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


# load the mean ImageNet image (as distributed with Caffe) for subtraction
mu = np.load(caffe_root + 'python/caffe/smalletst/mean.npy')
mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
print 'mean-subtracted values:', zip('BGR', mu)

# create transformer for the input called 'data'
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
# set the size of the input (we can skip this if we're happy
#  with the default; we can also change it later, e.g., for different batch sizes)
net.blobs['data'].reshape(1,        # batch size
                          3,         # 3-channel (BGR) images
                          64, 64)  # image size is 227x227

#Load an image (that comes with Caffe) and perform the preprocessing we've set up.
image = caffe.io.load_image(caffe_root + 'mytest/KTH_RGB/flow_i_0013.jpg')
transformed_image = transformer.preprocess('data', image)
#plt.imshow(image)

# copy the image data into the memory allocated for the net
net.blobs['data'].data[...] = transformed_image

### perform classification
output = net.forward()
output_prob = output['prob'][0]  # the output probability vector for the first image in the batch
print 'predicted class is:', output_prob.argmax()

#数据显示
feat = net.blobs['conv1'].data[0, :36]
vis_square(feat)
feat = net.blobs['conv5'].data[0,:36]
vis_square(feat)

feat = net.blobs['fc6'].data[0]
plt.subplot(2, 1, 1)
plt.plot(feat.flat)
plt.subplot(2, 1, 2)
_ = plt.hist(feat.flat[feat.flat > 0], bins=100)

feat = net.blobs['prob'].data[0]
plt.figure(figsize=(15, 3))
plt.plot(feat.flat)
