import math
import numpy

#L = [3,3,3,3,2,2,2,2,4,4,4,4]
#L = [20.0015,20.0016,20.0018,20.0015,20.0011]
#L = [236.45,236.37,236.51,236.34,236.39,236.48,236.47,236.40]
#L = [25.94,25.97,25.98,26.01,26.04,26.02,26.04,25.98,25.96,26.07]
#L = [25.93,25.94,25.98,26.02,26.01,25.90,25.93,26.04,25.94,26.02]
L = [28.53,28.52,28.50,28.53,28.53,28.50,28.49,28.49,28.51,28.53,28.52,28.49,28.50]

def calc_mean(L):
    n = len(L)
    #print(n)
    sum = 0
    for x in L:
        sum += x
    #print(sum/n)
    return sum/n

def calc_var(L):
    n = len(L)
    m = calc_mean(L)
    sum = 0
    for x in L:
        sum = sum + numpy.square(x-m)
    #print(sum/n)
    return sum/n

def calc_meas_std(L):
    #由贝塞尔公式计算出的测量标准差
    n = len(L)
    m = calc_mean(L)
    sum = 0
    for x in L:
        sum = sum + numpy.square(x-m)
    return numpy.sqrt(sum/(n-1))

mean = calc_mean(L)
print('mean = ',mean)
var = calc_var(L)
print ('variance = ',var)
meas_std = calc_meas_std(L)
print('meas_std = ',meas_std)
    
