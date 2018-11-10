import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    #利用re模块的正则表达式匹配出时区信息
    re_tz = re.match(r'UTC([+-]\d+):\d+',tz_str).group(1)
    print(re_tz)

    #日期时间str转化成datetime
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')      #str变量作为参数传入时不需要打''
    print(dt)

    #本地时间转化成UTC时间
    now_tzinfo = timezone(timedelta(hours=int(re_tz)))  #获取本地的时区属性
    utc_dt = dt.replace(tzinfo = now_tzinfo)                   #将本地时间根据本地时区属性转化为UTC时间
    print(utc_dt)

    #datetime转化为timestamp
    return utc_dt.timestamp()


#测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
