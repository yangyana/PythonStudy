# -*- coding: utf-8 -*-
"""
# @Author  : xiaobei
# @contact: 1642092466@qq.com
# @Software: PyCharm
# @File    : class_while.py
# @Time    : 2021/7/12 0012 下午 13:28
"""

#while循环
#语法：
#   while   条件表达式
    #循环的代码块
#执行顺序：首先判断while后面的条件 如果满足就执行代码块，执行完毕之后
# 再去判断while后面的条件  再执行代码块 执行完了再判断...如此反复

#a=-1
#while a<9:
   # print("python的while循环式  正在进行中")
    #a=a+1  #a=9 8 7 6 5 4 3 2 1
    #if a>10:
       # break

#用while循环 很容易陷入死循环，一定要设置好条件
#防止while语句进入死循环:
#1: break 终止循环
#2: 利用一个变量控制循环次数


#分别利用for循环,while循环完成1-100整数相加，求出和
#1：要拿到1-100的整数 range（1,101）

#for循环
sum=0 #存储值
for item in range(1,101):
    sum=sum+item
    print(sum)

#while循环
sum=0
a=1
while True:
    sum=sum+a #控制加法
    a=a+1 #控制a参数
    if a>100:
        break
print(sum)

# ==：判断两边的条件是否相等