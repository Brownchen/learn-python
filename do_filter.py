# 利用埃氏筛法生成质数序列
# 算法原理：
##先构造一个从3开始的奇数序列
##然后通过筛选函数筛选掉3的倍数
##将筛选后序列的第一个数作为除数对序列继续取余，不断筛选出新序列
##同时将序列的第一个数不断返回出，就能不断产生质数序列

def odd_iter():     #生成从3开始的奇数序列的生成器
    n = 1
    while True:
        n = n + 2
        yield n

def not_divisible(n):   #定义一个能筛去n的倍数的筛选器
    return lambda x:x % n >0

def primes():
    yield 2
    it = odd_iter()     #初始序列
    while True:
        n = next(it)    #返回序列的第一个数
        yield n
        it = filter(not_divisible(n),it)    #构造新序列

#打印1000以内的质数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
    
