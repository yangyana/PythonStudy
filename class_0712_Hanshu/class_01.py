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
#3：默认参数必须放在位置参数的后面
def greet_user(content,name='1'):
    print('{0}同学,{1}!'.format(name, content))

greet_user('小七','你很臭美','也很可爱')