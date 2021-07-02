# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 0022 下午 18:36
# @Author  : June
# @File    : class_03_for.py
# @Software: PyCharm

    #for  while
    #for 遍历元素  通过元素的个数来控制循环的次数
    #语法：for item in datas: 是数据范围：字符串、列表、元组、字典
                #重复执行的代码块

a='456@y'   #长度为5
b=[1,2,3]   #长度为3
c=(1,2,[5,6],[7,8]) #元组会循环4次
d={'age':1,'name':'kk'}
for item in d.items():  #item是一个变量 他会依次去访问a里面的元素，然后取到他的值 赋值给item
    print(item)
    #for循环的次数是由数据的元素个数决定的


    #数据集合 range(m,n,k) 生成一个整数序列  生成一个数据集合
#1：range(m,n,k)
    # m 开始; n-1 结束; k 步长
r=list(range(0,6,4))    #取左不取右
print(r)    #输出 0,4

#2：rang(m,n) 默认k=1---步长默认为1
r=list(range(2,3))

#3：range(n) 默认m=0 k=1
r=list(range(8))
print(r)


for i in range(4):
    print(i)  #输出 0 1 2 3



#课堂练习
L=[1,2,3,4,5,6,7]
#利用for循环 倒序输出这个列表的每个元素
#7654321

#1:L.reverse()
for item in L:
    print(item)

#2:print(list(range(-1,-8,-1)))
