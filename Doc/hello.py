#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from tkinter import N


from cmath import e
from tkinter import E


print ('hello, world!')
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

10 % 3
10 // 3
10 / 3

n = 123
print (n)
f = 456.789
print (f)
s1 = "Hello, \'Adam\'"
print (s1)
s3 = 'Hello, "Bart"'
print (s3)
s4 = 'Hello, \nLisa!'
print (s4)

ord('中')
'中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8')
len('abcdefg')
len('中文算')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

y = {"type": "apple", "size": "large"}
print (type(y))

x = 1e2
print (type(x))

x = 1.5
a = int (x)
print (a)

import random
print (random.randrange(0, 100))

x = "Hello, world!"
print (len(x))

x = "The best things in life are free!"
print("c" in x)

x = "The best things in life are free!"
print("c" not in x)

x = "The best things in life are free!"
if "b" in x:
    print('Great!')
else:
    print('Ah-oh!')

a = "Hello, World!"
print(a.upper())

a = "    Hello, World!"
print(a.strip())

a = "Hello, World!"
print(a.replace("Hello", "Hi"))

a = "Hello, World, is, the, best!"
print(a.split(","))

a = "Hello"
b = "World"
c = a + ' ' + b
print(c)

age = 30
txt = "My name is John, I am {}" 
print(txt.format(age))

age = '30'
txt = "My name is John, I am " + age
print(txt)

quantity = 3
itemno = 567
price = 49.99
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

x = "Hi,this is a best world louie!"
print(x.count("i"))

x = "Hello, world!"
print(x.swapcase())

x = "Hello, louie!"
print(x.title())

print(10<9)

x = 10
y = 90
if x>y:
    print('x is greater than y')
else:
    print('x is less than y')

bool()

thelist = ['pear', 'apple', 'cherry']
#print(thelist)
#print(len(thelist))
#print(type(thelist))
print(thelist[0])