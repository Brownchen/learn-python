from numpy import *
import operator
import os
from collections import Counter
import matplotlib.pyplot as plt 
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
    Img = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_Data')
    data = Img['IndianPine']
    GT = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/kNN/IndianPine_GT')
    labels = GT['GT']
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
    num_testSet = inX.shape[0]
    num_trainSet = dataSet.shape[0]
    dists = np.zeros((num_testSet,num_trainSet))
    dists = np.sqrt(-2*np.dot(inX,dataSet.T) + np.num(square(dataSet,axis=1)) + np.transpose([np.sum(np.square(inX,axis=1))]))
    
    sortedDistIndicies = dists.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def test():
    #group,labels = creatDataset()
    #print(str(group))
    #print(str(labels))
    #print(classfiy0([0.1,0.1],group,labels,3))
    train_data,test_data,train_label,test_label = readDatasetfromMat()
    pred_label = classfiy0(test_data,train_data,train_label,3)
    

if __name__ == '__main__':
    test()