import re

def  name_of_email(addr):
    #re_noe = re.compile(r'(<(.*)>(.*)@(.*))|((.*)@(.*))')
    re_noe = re.compile(r'<?(\w+\s?\w+)>?.*@\w+.\w{3}')     # <?和>? 表示 有一个或没有 这样就既可以匹配有<>的也可以匹配没有的
    m = re_noe.match(addr)
    print(m.group(1))


name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
