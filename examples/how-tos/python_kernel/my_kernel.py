import scannerpy
import struct
import numpy as np
from PIL import Image
import StringIO
import time
import sys
import cv2

class MyOpKernel(scannerpy.Kernel):
  def __init__(self, config, protobufs):
    self.protobufs = protobufs

  def close(self):
    pass

  def encode(arr, format="jpeg"):
    im = Image.fromarray(arr)
    buf = StringIO.StringIO()
    im.save(buf, format=format)
    output = buf.getvalue()
    buf.close()
    return output

  def execute(self, input_columns):
    # cv2_im = cv2.cvtColor(input_columns[0],cv2.COLOR_BGR2RGB)
    # pil_im = Image.fromarray(input_columns[0])
    # width, height = pil_im.size
    # print('width {}, height {}'.format(width, height))
    print np.shape(input_columns)
    print len(np.shape(input_columns))
    dims = len(np.shape(input_columns))
    # print arr
    # arr = input_columns[0]
    # jpeg_image = encode(arr)
    # print('Raw={:d}, Jpeg={:d}'.format(len(encode(arr, format="bmp")), len(jpeg_image)))
      # print('list size :{:d}'.format(len(input_columns[0])))
    if dims > 4:
      input_count = len(input_columns[0])
      column_count = len(input_columns)
      return [[struct.pack('=q', 9000) for _ in xrange(input_count)] 
             for _ in xrange(column_count)]
    else:
      return [struct.pack('=q', 9000)]

KERNEL = MyOpKernel
