import os
import pickle
def otherTest():
    print('-------------------------------')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


otherTest()
print(factorial(5))
otherTest()


def fab(n):
    a1 = a2 = a3 = 1
    if n < -1:
        print('输入错误')
        return -1
    else:
        while(n-2) > 0:
            a3 = a1+a2
            a1 = a2
            a2 = a3
            n = n-1
        return a3


print(fab(3))
otherTest()


def fab1(n):
    if(n < 1):
        print('输入有误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab1(n-1)+fab1(n-2)


print(fab1(3))
otherTest()


def hanoi(n, x, y, z):
    global c
    if n == 1:
        c+=1
        print(x, '-->', z,',c=',c)
    else:
        hanoi(n-1, x, z, y)
        c+=1
        print(x, '-->', z,',c=',c)
        hanoi(n-1, y, x, z)

c=0
hanoi(1, 'X', 'Y', 'Z')
otherTest()
list1=[1,2,4,6,7,9,0]
print(set(list1))
print(list(set(list1)))

otherTest()

f=open('record.txt')
print(f)
#print(f.read())
#print(f.readline())
print(f.tell())
f.seek(0,0)
for e in f:
    print(e)

print(os.getcwd())
print(os.listdir('..'))
# print(os.system('calc'))

# li=[1,2,'fjlas','网咯']
# pf=open('E:\Python\Test\li.pkl','wb')
# pickle.dump(li,pf)
# pf.close()

pf=open('E:\Python\Test\li.pkl','rb')
li=pickle.load(pf)
print(li)

class C:
    def __init__(self):
        print('init')

    def __del__(self):
        print('del')
otherTest()
c1=C()
otherTest()
c2=c1
otherTest()
c3=c2
otherTest()
del c1
otherTest()
del c2
otherTest()
del c3
otherTest()

import time as t 
print(t.localtime())

def myGen():
    print('生成器被执行')
    yield 1
    yield 2

mygen=myGen()
print(next(mygen))
print(next(mygen))

import sys
otherTest()
print(sys.path)
