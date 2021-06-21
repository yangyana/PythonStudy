
s_1='hello'
s_2='python'

    #字符串之间的拼接 同类型
s_3=s_1+' '+s_2  #输出hello python
# print(s_3)
# print(s_1,s_2)  #这个不是拼接 是相当于连续输出两个变量的值


    #str(数据值或者变量名)函数直接转换数据为字符串
# print(s_1+str(666)+s_2)  #整数可利用str()可以变成字符串
    #字符串的值为数字的 可利用int()转换成整数
# print(type(int('666')))

    #格式化输出
# 第一种格式化输出
age='18'
name='小可爱'
score=99.789
# print("未来大佬"+name+"只有",age,"岁")
    # %s 输出一个字符串 占坑；%d digital 整数类型的数字; %f 默认精确到后6位
    #按顺序赋值
# print("未来大佬%s,只有%d岁,python考试成绩%f"%(name,age,score))
# 第二种格式化输出 .format()  用()来占坑
    #按顺序赋值
    #如果不指定顺序 给空的() 就按从左到右顺序赋值,如果有指定 有几个参数就给几个 否则 少了 就报错
print("未来大佬{0},只有{1}岁,python考试成绩是{2}".format(name,age,score))
    #format(name,age,score)  name 0,age 1,score 2
