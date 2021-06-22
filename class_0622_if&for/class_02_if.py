# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 0022 下午 14:30
# @Author  : June
# @File    : class_02_if.py
# @Software: PyCharm

    #条件语句 循环语句
    #缩进 在python里 空格来控制
    #语法：if 条件表达式：
            #满足条件表达式执行的代码块  布尔值为ture时 满足条件


#1：else 后面不能加条件表达式
score=100
str_1='hello'
if score>0: #条件表达式-->比较运算符-->布尔值
    print('哎吆 很棒哦！')
else:
    print('小于100分了！继续努力了！')

#2：elif 后面必须加条件表达式
color='red'
if color=='red':
    print('红灯停')
elif color=='green':
    print('绿灯行')
else:
    print('黄灯等一等')

#3:一个完整的条件语句里面只有一个if 一个else里面可以有多个elif
color='red'
if color=='red':
    print('红灯停')
elif color=='green':
    print('绿灯行')
elif color=='yellow':
    print('黄灯等一等')
else:
    print('灯坏了！')

#4：如果数据为空或者为null 就代表false;不为空就为ture
a=[]
if a:
    print('我是if语句')
else:
    print('我是else语句')


a= {'age':18}
if a:
    print('我是if语句')
else:
    print('我是else语句')