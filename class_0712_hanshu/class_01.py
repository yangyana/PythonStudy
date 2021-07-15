# -*- coding: utf-8 -*-
"""
# @Author  : xiaobei
# @contact: 1642092466@qq.com
# @Software: PyCharm
# @File    : class_01.py
# @Time    : 2021/7/12 0012 下午 14:56
"""

#什么是函数？ insert append print input range len upper lower
#特点：随意调用 直接调用 对次使用 复用性强
#函数是一段可以重复完成某个功能的代码块

#语法：define 定义
#def 函数名(参数1,,参数2,参数3):
    #函数代码块

#调用？函数名()

#1:写一个问候函数
# def greet_user():
#     print('甲甲，晚上好！')
# greet_user()


# def greet_user_2():
#     print('charm 晚上好！')
# greet_user_2()
#
#
# def greet_user_3():
#     print('hello 晚上好！')
# greet_user_3()


#2:如果要提高函数的复用性 哪里可以参数化
def greet_user(name,content):
    print('{0}同学,{1}!'.format(name,content))
greet_user('七月','你是一个小仙女')


#函数参数：
#1：函数名后面的参数叫做形参/位置参数,函数可以有多个参数 也可以没有参数; 调用函数：实参
#2：定义函数时 有几个传参数 调用时就得传几个参数
#3：默认参数 必须放在位置参数的后面  可以有多个
#4：调用函数时都是按顺序取值
#5：调用函数 可以强制指定参数的赋值
#6：return关键词 返回一个值 必须拿一个变量去接收，谁调用返回给谁
#7：可以说是函数结束的标志  执行函数的结束

#def greet_user(content='666',name='hi小北'):
def greet_user(name,content ):
    # 两种格式化输出方式
    #print('{0}同学,{1}!'.format(name, content))  #1：.format(name,content) 字符串的格式化输出
    print(name+'oo,'+content+'!')  #2：字符串拼接 输出到控制台

greet_user('小苹果','你好厉害')



#练习：写一个函数 计算1-100总和
#三步走 1.先用零散的代码写出这个功能1-5 1 2 3 4 5==15; 2.选取一组数据来完成功能; 3.把代码变成一个函数; 4.想办法提高他的复用性

#range函数默认值为1

def add_number(m,n):
    sum=0 #存储总和的一个变量
#for i in range(1,6):
    for i in range(m,n+1):
      sum=sum+i
print("总和是：{0}".formant(sum))
add_number(1,100)


# 练习
def add(a,b):
    # return("两数相加的和是",a+b)
    print("两数相加的和是",a+b)
#调用函数
res=add(1,3)
print("我收到的返回值是",res)


def add():
    print("相加和是{0}".format(3,4))