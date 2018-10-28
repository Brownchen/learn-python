from functools import reduce
##
##def prod(L):
##    #return L[k] * L[k+1] for k in range(len(L)) 这是在列表生成式中的用法
##    t = 1
##    for k in range(len(L)):
##        t = t*L[k] 
##    return t
##
##print(prod([3,5,7,9]))

def prod(L):
    def p(x,y):
        return x*y
    return reduce(p,L)

print(prod([3,5,7,9]))
