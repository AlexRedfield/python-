# -*- coding: utf-8 -*-
import re
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y, L)

print(prod([3, 5, 7, 9]))
print(reduce(lambda x,y:x*y, [3, 5, 7, 9]))
#将字符串装换为浮点数
def str2float(L):
    def a(x,y):
        return x*10+y
    t=L.index('.')#.在L中位置
    #s1=list(map(int,L[:t]))
    #s2=list(map(int,L[t+1:]))
    #return reduce(a,s1)+reduce(a,s2)/10**len(s2)
    x=len(L[t+1:])
    l=L[:t]+L[t+1:]
    s = list(map(int, l))
    return reduce(a,s)/10**x
print(str2float('123.45678'))



test='bill.gates@microsoft.com'
print(re.match(r'^[0-9a-zA-Z\.\_]+\@\w+ft\.com$',test))
a=0
b=1
z=1
#斐波那契数列
'''while z<100:
    print(a,z)
    z+=1
    print(b,z)
    z+=1
    a+=b
    b+=a'''
#list操作
l=[]
l.append('x')
l.append(3)
l[1]='y'
l.insert(2,'z')
l.pop(-2)
#l=list(range(0,10))
print(l)
#tuple操作
t1=tuple(range(0,10,3))
t2=(0,3,6,9)
t3=('only one element',)
print (t1,t2,t3)
#dict操作,特点：没有顺序，不可重复，作为key的元素不可变（list不可作为key）
d={
    'A':95,
    'D':65
}
print(d['A'],d.get('D'))
d['S']=100
#dict遍历
print(d)
for key in d:
    print(key+':',d[key])
#set遍历
s=set([1,2,3])
print (1 in s,4in s)

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print( x[0]+':',x[1])
s.add('Alex')
s.remove(('Adam', 95))
print(s)
#sum()
L=[x**2 for x in range(0,101)]
print (sum(L))
#多个变量接受一个tuple
x,y=(0,1)
print(x,y)

#默认参数只能定义在必需参数的后面：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,3))
#定义可变参数
def average(*args):
    if(len(args)==0):
        return 0.0
    else:
        return sum(args)*1.0/len(args)
print(average(),average(1,2,3))
#对list切片
L = range(1, 101)

print (L[:10])
print (L[2::3])
print (L[4:50:5])
#首字母改成大写的函数
def firstCharUpper(s):
    return s[0].upper()+s[1:]
print (firstCharUpper('hello'))
#zip函数
L=['A','B','C','D']
for index,value in zip(range(1,5),L):
    print(index,'-',value)
#迭代dict的value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for i in d.values():
    sum+=i
print(sum/len(d))
print (d.items())
#条件过滤
print([x**2 for x in range(1,11) if x%2==0])
#多层表达式
print([x+y for x in'ABC' for y in'12'])