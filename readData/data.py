'''
author：Liuzixu
data:2018.11.27 16:20
'''
import scipy.io as sio###导入mat文件所需要的库
'''BOT数据（迁移学习数据）'''
def BOT_TL_small(id):
    #return the train data and test data
    data = sio.loadmat('TL_BOT_data.mat')
    
    Train_data_1 = data['train_data_TL'][:, id]##训练数据
    Train_label_1 = data['train_label_TL'][:, id]##训练数据标签
    Test_data_1 = data['test_data_TL'][:, id]##测试数据
    Test_label_1 = data['test_label_TL'][:, id]##测试数据标签
    
    Train_data1 = Train_data_1[0]
    Train_label1 = Train_label_1[0]
    Train_label = Train_label1[:, 0]
    
    Test_data1 = Test_data_1[0]
    Test_label1 = Test_label_1[0]
    Test_label = Test_label1[:, 0]
    return Train_data1, Train_label, Test_data1, Test_label
def BOT_TL_ALL(id):
    #return the train data and test data
    data = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/readData/TL_BOT_ALL.mat')
    Train_data_1 = data['Train_data_TL'][:, id]
    Train_label_1 = data['Train_label_TL'][:, id]
    Test_data_1 = data['Test_data_TL'][:, id]
    Test_label_1 = data['Test_label_TL'][:, id]
    Train_data1 = Train_data_1[0]
    Train_label1 = Train_label_1[0]
    Train_label = Train_label1[:, 0]
    Test_data1 = Test_data_1[0]
    Test_label1 = Test_label_1[0]
    Test_label = Test_label1[:, 0]
    return Train_data1, Train_label, Test_data1, Test_label
x1,y1,t1,t2 = BOT_TL_ALL(0)
print(t1.shape)

# =============================================================================
# def WV2_TL_ALL(id):
#     data = sio.loadmat('E:/陈敏/Data/cmWork/learn_python/learn-python/readData/TL_WV2.mat')
#     Train_data_1 = data['Train_data_TL'][:, id]
#     Train_label_1 = data['Train_label_TL'][:, id]
#     Test_data_1 = data['Test_data_TL'][:, id]
#     Test_label_1 = data['Test_label_TL'][:, id]
#     Train_data1 = Train_data_1[0]
#     Train_label1 = Train_label_1[0]
#     Train_label = Train_label1[:, 0]
#     Test_data1 = Test_data_1[0]
#     Test_label1 = Test_label_1[0]
#     Test_label = Test_label1[:, 0]
#     return Train_data1, Train_label, Test_data1, Test_label
# x1,y1,t1,t2 = WV2_TL_ALL(0)
# print(x1.shape)
# =============================================================================




