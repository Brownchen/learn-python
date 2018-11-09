import re

def name_of_email(addr):
    re_noe = re.split(r'[<>@]+',addr)
    if re_noe[0] == '':
        print(re_noe[1])
    else:
        print(re_noe[0])


# 测试:
##assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
##assert name_of_email('tom@voyager.org') == 'tom'
##print('ok')

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
