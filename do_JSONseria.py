import json


obj = dict(name='小明',age=20)
s = json.dumps(obj,ensure_ascii=False)
print(s)


#ensure_ascii=False  ==> 输出字符中的非ASCII字符会按照本来的样子输出
#ensure_ascii=True   ==> 输出字符中的非ASCII字符会显示为未编码的原码
