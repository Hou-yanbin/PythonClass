#-*- codeing = utf-8 -*-
#@Time: 2021/3/8 16:29
#@Auther: Jack hou
#@File: 求三数和和平均值.py
#@Software: PyCharm

"""
编程从键盘读入3个整数，输出它们的和与平均值。其中，平均值保留2位小数。

输入格式:
整数1
整数2
整数3

输出格式:
和,平均值
"""
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
print(sum, end = '' )
print((",""%.2f" %(sum/3)))


