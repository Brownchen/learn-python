L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

#L2 = sorted(L,key = by_name)
L2 = sorted(L,key = by_score,reverse=True)
print(L2)

#注意sorted中传入的函数是作用在L中的单独元素上

#当对字符串或者dict进行排序时，就要利用函数将比较的依据（key）抽象出来
