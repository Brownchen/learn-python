# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:15:55 2018

@author: cm
"""
import numpy as np
import operator
import os
from collections import Counter
import matplotlib.pyplot as plt 
import scipy.io as sio
from sklearn.cross_validation import train_test_split



# =============================================================================
# def creatDataset():
#     '''
#     手动创建一个训练数据集，包括训练数据featrues和labels    
#     '''
#     group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#     labels = ['A','A','B','B']
#     return group,labels
# =============================================================================

def readDatasetfromMat():
# =============================================================================
    Img = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_Data')
    data = Img['IndianPine']
    GT = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_GT')
    labels = GT['GT']
# =============================================================================
#    data = sio.loadmat('C:/Users/lrsc/Desktop/kNN/INP_data_2dim')
#    labels = sio.loadmat('C:/Users/lrsc/Desktop/kNN/INP_labels')
    train_data,test_data,train_label,test_label = train_test_split(data,labels,test_size=0.3,random_state=0)
    return train_data,test_data,train_label,test_label


def classfiy0(inX,dataSet,labels,k):
    '''
    实现KNN算法的分类函数
    inX:测试数据的featrues
    dataSet:训练数据的features
    labels:训练数据的标签
    k：kNN的参数
    '''
    #dataSetSize = dataSet.shape[0]
    #diffMat = tile(inX,(dataSetSize,1)) - dataSet##测试数据与训练数据的矩阵格式不同
    #sqDiffMat = diffMat**2
    #sqDistances = sqDiffMat.sum(axis=1)
    #distances = sqDistances**0.5
    '''使用矩阵运算的方法计算两个矩阵之间的欧式距离 '''
    '''https://blog.csdn.net/frankzd/article/details/80251042'''
    dim = inX.shape[2]
    num_testSet = inX.shape[0]
    num_trainSet = dataSet.shape[0]
    inX2 = inX.reshape(-1,dim,order='C')
    dataSet2 = dataSet.reshape(-1,dim,order='C')
    labels2 = labels.reshape(-1)
# =============================================================================
#     print(inX2.shape)
#     print(dataSet2.shape)
# =============================================================================
    #dists = np.zeros((num_testSet,num_trainSet))
    dists = np.zeros((inX2.shape[0],dataSet2.shape[0]))
    dists = np.sqrt(-2*np.dot(inX2,dataSet2.T) + np.sum(square(dataSet2),axis=1) + np.transpose([np.sum(np.square(inX2),axis=1)]))
    print(dists.shape)
    '''从最近的k个点选出标签'''
# =============================================================================
#     sortedDistIndicies = dists.argsort()
#     classCount = {}
#     for i in range(k):
#         voteIlabel = labels[sortedDistIndicies[i]]
#         classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
#     sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
#     return sortedClassCount[0][0]
# =============================================================================
    pred = np.zeros(num_testSet)
    for i in range(num_testSet):
        slabels = labels2[np.argsort(dists[i,:])]
        clot_labels = slabels[0:k]
        pred[i] = np.argmax(np.bincount(clot_labels))
    return pred[i]


def test():
    #group,labels = creatDataset()
    #print(str(group))
    #print(str(labels))
    #print(classfiy0([0.1,0.1],group,labels,3))
    train_data,test_data,train_label,test_label = readDatasetfromMat()
    pred_label = classfiy0(test_data,train_data,train_label,3)
    print(pred_label)
    

if __name__ == '__main__':
    test()
