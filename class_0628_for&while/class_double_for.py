# -*- coding: utf-8 -*-
"""
# @Author  : xiaobei
# @contact: 1642092466@qq.com
# @Software: PyCharm
# @File    : class_double_for.py
# @Time    : 2021/7/2 0002 下午 14:47
"""

    #嵌套循环 for; for if
a=[[1,2,3,4],[5,6,7,8]]
#有几个元素？ 2
#子元素是什么类型？ 列表 子列表有4个元素
#把a里面的元素全部打印出来

#1:第一个方式
#print(a[0])
#print(a[1])

#2:第二方式
#for item in a:
#    print(item)

#把a里面的元素一个一个的打印出来
#item是一个列表  对item进行一个遍历
for item in a:
    print(item)
for date in item:
    print(date)






