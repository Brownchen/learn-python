import re

def is_vaild_email(addr):
    if re.match(r'^[a-zA-Z0-9.]{0,13}\@.(a-z){0,3}$',str(addr)):
        print(addr)
        return true
    else:
        print('您输入的不是正确的邮箱号码！')
