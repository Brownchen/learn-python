##def createCounter():
##    a = [0]                     #在内部函数里修改外部函数局部变量的方法之一：把外部变量变成容器（可变变量）
##    def counter():
##        a[0] = a[0] +1
##        return a[0]
##    return counter

def createCounter():
    a = 0
    def counter():
        nonlocal a                  #方法之二：在内部函数内将外部变量申明为nonlocal
        a += 1
        return a
    return counter

# 或者分别在内部和外部函数里声明global a 将变量申明为全局变量

#测试

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
