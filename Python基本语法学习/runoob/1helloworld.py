#!/usr/bin/python3
print ("HGello World")


if True:
    print("True")
else:
    print("False")
    print("a")


import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

#---------列表[],元组()。集合{XXX}或set(),空字典{ }-----------------------------------------#
#列表
tup1 = [20]
tup1[0] = 1 #列表的值能修改

#元组 -- 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup2 = (20)
#tup2[0] = 1 #元组的值不能修改
print (type(tup2)) #<class 'int'>

tup3 = (20,)
print (type(tup3)) #<class 'tuple'>

#集合：使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

#字典：列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。


print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))


#!/usr/bin/python3
input("\n\n按下 enter 键后退出。")