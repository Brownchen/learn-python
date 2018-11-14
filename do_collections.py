##collections是python内建的一个集合模块，提供了很多有用的集合类

##from collections import nametuple
##Point = nametuple('Point',['x','y'])
##p = Point(1,2)
##p.x
##p.y
###nametuple函数可以一个自定义的tuple对象，它具备了tuple的不变性，又可以方便的根据属性来引用tuple中的单个值


>>> from collections import deque
>>> q = deque(['a','b','c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
##deque可以高效地实现插入和删除操作地双向列表，适合用于队列和栈

>>> from collections import defaultdict
>>> dd = defaultdict(lambda:'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1']
'abc'
>>> dd['key2']
'N/A'
##使用defauldict后，当引用的key不存在时不会抛出keyerror，而是返回一个默认值



##OrderedDict会按照插入的顺序排列其中的元素
##可以用OrderedDict实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
##do_OrderedDict.py


##ChainMap??


##Counter
##Counter实现了一个简单的计数器
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'you never konw if you never try':
	c[ch] = c[ch] + 1

	
>>> c
Counter({' ': 6, 'e': 4, 'y': 3, 'o': 3, 'n': 3, 'r': 3, 'u': 2, 'v': 2, 'k': 1, 'w': 1, 'i': 1, 'f': 1, 't': 1})



