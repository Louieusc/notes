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