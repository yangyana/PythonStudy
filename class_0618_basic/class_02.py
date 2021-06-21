
    #详细讲解字符串  str
p='hello' #字符串
    #字符串的单个元素取值
    #字符串里面的值取出来还是字符串类型
    #字符串里面的元素是怎么定他们的位置的--索引
    #索引：正序---从左往右 0 1 2 3 4...; 反序--从右往左 -1 -2 -3 -4...
    #字符串里取值是根据索引来取值的
    #取值方式： 字符串名[索引值]
#print=(p[4])


    #字符串切片：字符串变量名[m:n:k]
    #m：索引的起始位置 n：索引结束位置+1  k:步长
    #K的默认值是1  从2开始每次+1
p_1="hello" #字符串
    #请把hello这个字符串里面的el两个字母输出到控制台
#print(p_1[1:3])  #取左不取右
#print(p_1[0:5:2]) #输出hlo   k的值是2 每次索引取值会+2 对应得索引是 0 2 4

    #反序  把p_1倒序输出
p_1='hello'
#print(P_1[6::-1])  #olleh

    #字符串进阶操作：python内置函数的调用
    #切换大小写
a='get'
a_1=a[1].upper()
print(a)    #只把get里的第一次字母变成大写 输出E

a=a.upper() #把英文字母全部变成大写字母
print(a_1)  #输出GET

b='BiG'
b_1=b.lower() #把英文字母大写变成小写
print(b_1)   #输出big

    #字符串查找  用法：字符串.find
lemon_1='lemon is best'
print(lemon_1.find('!'))
    #返回-1 说明查找的字符不存在
print(lemon_1.find('b'))
    #返回9 返回字符所在的索引; 空格也算1个索引
print(lemon_1.find('lemon'))
    #返回0 如果是字符串返回的是子字符串的第一个元素的索引(返回l的索引)
print(lemon_1.find('is'))
    #返回6 返回的是i的索引

lemon_1='blemon is best'
print(lemon_1.find('b'))
    #返回0  如果有相同的 就查找第一个


    #字符串替换  字符串变量名.replace(目标，替换的值，替换的次数)
s_4='hello python'
s_5=s_4.replace('o','66')  #替换之后要保存起来
    #不知道替换次数就全部替换
print(s_5) #输出hell66 pyth66n

    #能不能直接替换第二个？  只能先替换 在操作
s_6=s_5.replace('o','66',1)
print(s_6)





