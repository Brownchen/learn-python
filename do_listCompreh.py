L = ['Hello','World',18,"Apple",None]
M = [s.lower() for s in L if isinstance(s,str)]  #列表生成式
print(M)
