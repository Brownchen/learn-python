import re

##def is_vaild_email(addr):
##    if re.match(r'^[a-zA-Z0-9.]{0,13}\@.(a-z){0,3}$',str(addr)):
##        print(addr)
##        return true
##    else:
##        print('您输入的不是正确的邮箱号码！')

def is_valid_email(addr):
    re_email = re.compile(r'^([a-zA-Z0-9\.]*)\@([a-z]*)\.([a-z]{1,3})$')
    if re_email.match(addr) != None:
        return True
##    else:
##        print('您输入的不是正确的邮箱号码！')


#测试
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
