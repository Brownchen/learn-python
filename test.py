##import time
##import math
##import random
##
##import pandas as pd
##from sklearn.model_selection import train_test_split
##from sklearn.metrics import accuracy_score
##
##
##class LogisticRegression(object):
##
##    def __init__(self):
##        self.learning_step = 0.00001
##        self.max_iteration = 5000
##
##    def predict_(self,x):
##        wx = sum([self.w[j] * x[j] for j in xrange(len(self.w))])
##        exp_wx = math.exp(wx)
##
##        predict1 = exp_wx / (1 + exp_wx)
##        predict0 = 1 / (1 + exp_wx)
##
##        if predict1 > predict0:
##            return 1
##        else:
##            return 0
##
##
##    def train(self,features, labels):
##        self.w = [0.0] * (len(features[0]) + 1)
##
##        correct_count = 0
##        time = 0
##
##        while time < self.max_iteration:
##            index = random.randint(0, len(labels) - 1)
##            x = list(features[index])
##            x.append(1.0)
##            y = labels[index]
##
##            if y == self.predict_(x):
##                correct_count += 1
##                if correct_count > self.max_iteration:
##                    break
##                continue
##
##            # print 'iterater times %d' % time
##            time += 1
##            correct_count = 0
##
##            wx = sum([self.w[i] * x[i] for i in xrange(len(self.w))])
##            exp_wx = math.exp(wx)
##
##            for i in xrange(len(self.w)):
##                self.w[i] -= self.learning_step * \
##                    (-y * x[i] + float(x[i] * exp_wx) / float(1 + exp_wx))
##
##
##    def predict(self,features):
##        labels = []
##
##        for feature in features:
##            x = list(feature)
##            x.append(1)
##            labels.append(self.predict_(x))
##
##        return labels
##
##if __name__ == "__main__":
##    print ('Start read data')
##
##    time_1 = time.time()
##
##    raw_data = pd.read_csv('../data/train_binary.csv',header=0)
##    data = raw_data.values
##
##    imgs = data[0::,1::]
##    labels = data[::,0]
##
##
##    # 选取 2/3 数据作为训练集， 1/3 数据作为测试集
##    train_features, test_features, train_labels, test_labels = train_test_split(imgs, labels, test_size=0.33, random_state=23323)
##
##    time_2 = time.time()
##    print ('read data cost ',time_2 - time_1,' second','\n')
##
##    print ('Start training')
##    lr = LogisticRegression()
##    lr.train(train_features, train_labels)
##
##    time_3 = time.time()
##    print ('training cost ',time_3 - time_2,' second','\n')
##
##    print ('Start predicting')
##    test_predict = lr.predict(test_features)
##    time_4 = time.time()
##    print ('predicting cost ',time_4 - time_3,' second','\n')
##
##    score = accuracy_score(test_labels,test_predict)
##    print ("The accruacy socre is ", score)





from math import exp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

# data
def create_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['label'] = iris.target
    df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
    data = np.array(df.iloc[:100, [0,1,-1]])
    # print(data)
    return data[:,:2], data[:,-1]

X, y = create_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

class LogisticReressionClassifier:
    def __init__(self, max_iter=200, learning_rate=0.01):
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        
    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def data_matrix(self, X):
        data_mat = []
        for d in X:
            data_mat.append([1.0, *d])
        return data_mat

    def fit(self, X, y):
        # label = np.mat(y)
        data_mat = self.data_matrix(X) # m*n
        self.weights = np.zeros((len(data_mat[0]),1), dtype=np.float32)

        for iter_ in range(self.max_iter):
            for i in range(len(X)):
                result = self.sigmoid(np.dot(data_mat[i], self.weights))
                error = y[i] - result 
                self.weights += self.learning_rate * error * np.transpose([data_mat[i]])
        print('LogisticRegression Model(learning_rate={},max_iter={})'.format(self.learning_rate, self.max_iter))

    # def f(self, x):
    #     return -(self.weights[0] + self.weights[1] * x) / self.weights[2]

    def score(self, X_test, y_test):
        right = 0
        X_test = self.data_matrix(X_test)
        for x, y in zip(X_test, y_test):
            result = np.dot(x, self.weights)
            if (result > 0 and y == 1) or (result < 0 and y == 0):
                right += 1
        return right / len(X_test)

lr_clf = LogisticReressionClassifier()
lr_clf.fit(X_train, y_train)

lr_clf.score(X_test, y_test)

x_ponits = np.arange(4, 8)
y_ = -(lr_clf.weights[1]*x_ponits + lr_clf.weights[0])/lr_clf.weights[2]
plt.plot(x_ponits, y_)

#lr_clf.show_graph()
plt.scatter(X[:50,0],X[:50,1], label='0')
plt.scatter(X[50:,0],X[50:,1], label='1')
plt.legend()


clf = LogisticRegression(max_iter=200)

clf.fit(X_train, y_train)

clf.fit(X_train, y_train)

print(clf.coef_, clf.intercept_)


x_ponits = np.arange(4, 8)
y_ = -(clf.coef_[0][0]*x_ponits + clf.intercept_)/clf.coef_[0][1]
plt.plot(x_ponits, y_)

plt.plot(X[:50, 0], X[:50, 1], 'bo', color='blue', label='0')
plt.plot(X[50:, 0], X[50:, 1], 'bo', color='orange', label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
