from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)             #last=False是popitem方法的参数，这里是指定采用FIFO
            print('remove',last)
        if containsKey:                                         #更新已有值
            del self[key]                                         #删除已有的键值对，更新后的键值对会插入最后
            print('set:',(key,value))
        else:
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)     #主体功能继承父类的方法！！

if __name__ == '__main__':
    luod = LastUpdatedOrderedDict(3)
    luod['a'] = 1
    luod['b'] = 2
    luod['c'] = 3
    print(luod)
    luod['x'] = 2
    print(luod)
    luod['b'] = 1
    print(luod)
    
