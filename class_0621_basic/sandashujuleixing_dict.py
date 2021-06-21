

    #字典
    #关键字 dict  标志：{}
    #值的特点是 键值对 key_value
    #a={} #空字典
a={'age':18,'name':'雅娜'}
    #元组 列表 都是有序的数据类
    #字典是无序的数据类
    #取值 就是按照key取值   字典名[key]
print(a['age'])

    #所有的值 dict.values()
    #print(a.values())

    #所有的值 dict.keys()
print(a.keys())


a={'age':18,'name':'雅娜'}
    #dictkey增删改吗?
    #新增值  a[新key]=value
a['score']=99.87
print(a)
    #修改值 a[已存在的key]=value
a['age']=20

    #删除值 dirct.pop(key)
a.pop('name')
print(a)



    #key是唯一的  value可以不唯一

a={'age':18,'name':'雅娜','score':{'ch':99,'en':100,'math':101}}

print(a['score']['math'])