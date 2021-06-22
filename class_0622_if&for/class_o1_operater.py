# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 0022 下午 14:04
# @Author  : June
# @File    : class_o1_operater.py
# @Software: PyCharm

    #运算符
    #算数运算符：+ - * / %
    # % 取余(余数)运算 判断奇偶数时 会用到  返回值是Ture False
print(6%2==0) #Ture 能够整除2是偶数，不能整除2 ！=0 就是奇数


    #比较运算符：>、 <、 !=、 >=、 <=、 ==  6种常用的比较关系————运算结果是布尔值
    #布尔值 Ture False
a=10
b=8
print(a==b) #False


    #赋值运算符：=  +=  -=
a=10
a+=1 #a=a+1(推荐)  自身的基础上加几  返回a=11
a-=6 #a=a-6  返回a=5
print(a)

    #逻辑运算符 and(且/和),or(或), not
    #and 运算结果:ture false
a=0
b=10
print(a>0 and b>0) #返回F
print(a>0 or b>0)  #T
#and 真真为正,  or 假假为假

    #成员运算符：in not in  运算结果也是 ture false
a='hello'
print('h' in a)     #Ture
print('h' not in a)     #False



