# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:56:48 2018

@author: lrsc
"""

import matplotlib.pyplot as plt  
import numpy as np
import scipy.io as sio
#from scipy.io import loadmat
import spectral


#读入数据，但是得到的Img是一个dict类型，
#其中'IndianPine'key对应的就是145*145*200的数据
Img = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_Data')
data = Img['IndianPine']
#print(data.shape)
print(data.type)
(x,y,z) = data.shape
#print(data.shape[0])

#读入标签，首先利用matlab的multibandread函数
#从92AV3GT_cls.bin文件中取出标签并保存为IndianPine_GT.mat
#然后与读入数据一样，从dict中取出label
GT = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_GT')
label = GT['GT']
#print(label.shape)
# =============================================================================
# data_matrix = np.zeros((x,y))
# for i in range(x):
#     for j in range(y):
#         data_matrix[i][j] = data[i][j]
# print(data_matrix.shape)
# =============================================================================
