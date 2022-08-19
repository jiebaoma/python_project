#!/usr/bin/env python
#__*__ coding:utf-8 __*__

print(""" hello,I'm yjzhai hahah ''' """)

#换行
print('\n')
#转义后输出\n
print('\\n')

print('\\\n')
#输出:\\n(第一个反斜杠转移了第二个反斜杠，第三个反斜杠转义了\n)
print('\\\\n')


#1.算术运算符
#数字与布尔型相加:True十进制为1，FALSE为0
print(1+True)
print(1+False)

#5.成员运算符:字典针对key
a=5
b={'lemon':5}
print(a in b)
a='lemon'
print(a in b)

#6.身份运算符
a=1
b=1
print(a is b)
#查看内存地址
print(id(a))
print(id(b))

#值类型是不变的（int string tuple），引用类型是可变的(list dict set)
a=1
b=a
print(a,b)
a=[1,2,3]
b=a
a[0]=4
print(a,b)

x=[1,2,3,4]
print(tuple(x))