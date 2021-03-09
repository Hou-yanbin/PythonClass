#-*- codeing = utf-8 -*-
#@Time: 2021/3/9 10:09
#@Auther: Jack hou
#@File: 函数f(x).py
#@Software: PyCharm

import math
x=float(input())
f=(math.sin(35)+((math.pow(math.e,x)-15*x)/(math.sqrt(math.pow(x,4)+1)))-math.log(7*x))
print(round(f,3))

# a=int(input())
# hour=int(a/60/60)%24
# hour1=str(hour)
# minute=int((a-hour*3600)/60)
# minute1=str(minute)
# second=int((a-hour*3600-minute*60))
# second1=str(second)
# print(hour1+" : "+minute1+" : "+second1)

# a = float(input())
# b = float(input())
# c = float(input())
#
# # 计算半周长
# s = (a + b + c) / 2
#
# # 计算面积
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('%0.1f' % area)