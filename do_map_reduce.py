from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    s1,s2=s.split('.')
    s2 = [s2[len(s2)-n-1] for n in range(len(s2))]   #将小数序列颠倒过来,注意列表生成式的使用
    def char2num(s):
        return DIGITS[s]
    def fp(x,y):
        return x*10 + y
    def fn(x,y):
        return x*0.1 + y
    return reduce(fp,map(char2num,s1)) + reduce(fn,map(char2num,s2))*0.1


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
