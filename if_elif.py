height = 1.77
weight = 62.5

BMI = weight/(height**2)

if BMI >= 32:
    print('严重肥胖')
elif BMI >= 28:
    print('肥胖')
elif BMI >= 25:
    print('过重')
elif BMI >= 18.5:
    print('正常')
else:
    print('过轻')