
    #字符串进阶操作
str_1='hello,python,kk'
    #split() 根据传入的指定的字符进行切割
#res=str_1.split(',') #返回的是列表数据的类型  默认全部切割
res=str_1.split('k',2) #指定字符 指定切割次数  与replace类似
    #列表里面的元素 都是字符串
#str_1='hello python kk'
#res=str_1.split() #默认切割空格
print(res)

    #去除指定元素 strip() 去除头和尾
str_1='hello,python,kk'
res=str_1.strip() #不传任何字符时 去除空格
    #如果传了字符 就去除指定的字符
res=str_1.strip('h')
print(res)