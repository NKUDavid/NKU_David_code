#-- encoding :utf-8 --
'''
Create by NKU_David 
'''
import tensorflow as tf
import numpy as np
import os
import cv2
import sys

img_path = './img'
if __name__=='__main__':
    img_dic =os.listdir(img_path)
    # print(img_dic[0])
    path = img_path+'/'+img_dic[0]
    filename = './train_data.tfrecord'
    writer = tf.python_io.TFRecordWriter(filename)
    img = cv2.imread(path)
    cv2.imshow(img)