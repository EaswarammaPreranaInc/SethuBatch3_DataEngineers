# Program 1
# How to iterate zip object in different ways (Home work)
import time
a = ['Telangana', 'Andhra Pradesh', 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai']
z1 = zip(a, b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
# How to iterate thru zip object with next() function
print('Iterate  thru  zip  object  with  __next__()  method')
# How to iterate thru zip object with __next__() method
print('Iterate  thru  zip  object  with   for  loop')
# How to iterate thru zip object with for loop
print('Elements  of  each  tuple  in  zip  object')
# How to iterate thru elements of each tuple of zip object with for loop
print('Unpacks  zip  object  with   *  operator  :  ', ???)
print()
print('zip   object  in  the  form  of   list  :  ', ???)
print()
print('zip   object  in  the  form  of   dictionary :  ', ???)
'''
Output:
<class 'zip'>
<zip object at 0x...>
Iterate  thru  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with  __next__()  method
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Elements  of  each  tuple  in  zip  object
Telangana Hyderabad
Andhra Pradesh Amaravathi
Karnataka  Bangalore
Tamilnadu Chennai
Unpacks  zip  object  with   *  operator  :   ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}
'''


# Program 2
# Find outputs (Home work)
import time
a = ['Empno', 'Emp Name', 'Salary']
b = [25, 'Rama  Rao', 10000.0, 'Male', True]
z = zip(a, b)
while True:
    try:
        print(next(z))
        time.sleep(1)
    except StopIteration:
        break
'''
Output:
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
'''


# Program 3
# Find outputs (Home work)
import time
a = ['Telangana', 'Andhra  Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Banglore', 'Chennai', 'Mumbai']
c = [50000000, 40000000, 70000000, 60000000, 30000000]
for x in zip(a, b, c):
    print(x)
    time.sleep(1)
'''
Output:
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''


# Program 4
# Find outputs (Home work)
import time
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
for x, y in zip(a, b):
    print(x + y)
    time.sleep(1)
'''
Output:
5
7
9
'''


# Program 5
# Find outputs (Home work)
import time
def disp(z):
    while True:
        try:
            print(next(z))
            time.sleep(1)
        except:
            break
    print()
a = [10, 20, 30]
b = {1: 2, 3: 4, 5: 6}
z1 = zip(a, b.keys())
disp(z1)
z2 = zip(a, b.values())
disp(z2)
z3 = zip(a, b.items())
disp(z3)
z4 = zip(a, b)
disp(z4)
z5 = zip(a)
disp(z5)
z6 = zip(b)
disp(z6)
z7 = zip()
disp(z7)
'''
Output:
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)

'''


# Program 6
# Find outputs (Home work)
z = zip(range(5), range(20, 25))
a = [[x, y] for x, y in z]
print(a)
'''
Output:
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''


# Program 7
# How to print reversed object in different ways (Home work)
import time
a = input('Enter  any  string  :  ')  # Assume that input is HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
# How to iterate reversed object 'r' with next() function
print('Iterate  thru  reversed  object  with   __next__   method')
# How to iterate reversed object with __next__() method
print('Iterate  thru  reversed  object  with   for  loop')
# How to iterate reversed object with for loop
print('Unpack  reversed  object  :', ???)
print('List  of  chars  in  reverse  order  :  ', ???)
print('Reverse  string   :   ', ???)
'''
Output:
<class 'reversed'>
<reversed object at 0x...>
Iterate  thru  reversed  object  with   next   function
D
Y
H
Iterate  thru  reversed  object  with   __next__   method
D
Y
H
Iterate  thru  reversed  object  with   for  loop
D
Y
H
Unpack  reversed  object  :  D Y H
List  of  chars  in  reverse  order  :   ['D', 'Y', 'H']
Reverse  string   :    DYH
'''


# Program 8
# Find outputs (Home work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0])
print(b[1:3])
print(b * 2)
print(len(b))
'''
Output:
<class 'reversed'>
<reversed object at 0x...>
<some id value>
D Y H
TypeError: 'reversed' object is not subscriptable
TypeError: 'reversed' object is not subscriptable
TypeError: unsupported operand type(s) for *: 'reversed' and 'int'
TypeError: object of type 'reversed' has no len()
'''


# Program 9
# Can tuple be reversed? (Home work)
import time
a = (25, 10.8, 'Hyd', True)
b = reversed(a)
print(type(b))
for x in b:
    print(x)
    time.sleep(1)
'''
Output:
<class 'reversed'>
True
Hyd
10.8
25
'''


# Program 10
# How to print list_reverseiterator object in different ways (Home work)
import time
lst = [25, 10.8, 'Hyd', True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
# How to iterate list_reverseiterator object with next() function
print('__next__()   method  iterates   thru  list_reverseiterator  object')
# How to iterate list_reverseiterator object with __next__() method
print('for  loop  iterates  thru  list_reverseiterator  object')
# How to iterate list_reverseiterator object with for loop
print('Unpack  list_reverseiterator  object  :  ', ???)
print('Reverse  list  :  ', ???)
'''
Output:
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x...>
next()   function  iterates   thru  list_reverseiterator  object
True
Hyd
10.8
25
__next__()   method  iterates   thru  list_reverseiterator  object
True
Hyd
10.8
25
for  loop  iterates  thru  list_reverseiterator  object
True
Hyd
10.8
25
Unpack  list_reverseiterator  object  :   True Hyd 10.8 25
Reverse  list  :   [True, 'Hyd', 10.8, 25]
'''


# Program 11
# Can set be reversed? (Home work)
a = {10, 20, 15, 18}
r = reversed(a)
'''
Output:
TypeError: 'set' object is not reversible
'''


# Program 12
# Can dictionary be reversed? (Home work)
import time
def disp(r):
    while True:
        try:
            print(next(r))
            time.sleep(0.5)
        except StopIteration:
            break
a = {10: 'Rama', 20: 'Sita', 15: 'Kiran', 18: 'Amar'}
r1 = reversed(a.keys())
disp(r1)
r2 = reversed(a.values())
disp(r2)
r3 = reversed(a.items())
disp(r3)
r4 = reversed(a)
disp(r4)
'''
Output:
18
15
20
10
Amar
Kiran
Sita
Rama
(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')
18
15
20
10
'''


# Program 13
# Tricky program - Write a program to reverse a dictionary
# Input:  {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
# Hint: Both input and output are dictionaries
d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
reversed_d = dict(reversed(list(d.items())))
print(reversed_d)
'''
Output:
{'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}
'''


# Program 14
# Find outputs
import time
a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print('Keys  in   reverse   order')
# Write for loop to reverse keys of dictionary
print('Values  in  reverse  order')
# Write for loop to reverse values of dictionary
print('Tuples  in   reverse  order')
# Write for loop to reverse tuples of dictionary
print('Elements  of  each   tuple  in  reverse  order')
# Write for loop to reverse elements of each tuple of dictionary
print('Keys  and  values  in   reverse   order')
# Write for loop to reverse keys and corresponding values of dictionary
'''
Output:
Keys  in   reverse   order
18
15
20
10
Values  in  reverse  order
Kiran
Rajesh
Sita
Rama rao
Tuples  in   reverse  order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements  of  each   tuple  in  reverse  order
Kiran 18
Rajesh 15
Sita 20
Rama rao 10
Keys  and  values  in   reverse   order
18 Kiran
15 Rajesh
20 Sita
10 Rama rao
'''


# Program 15
# How to iterate list_iterator in different ways
import time
list = [10, 20, 15, 18]
print('Iterate  list  with  for  loop')
# How to iterate list with for loop
print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
# How to iterate list_iterator with next() function
print('Iterate  thru  list_iterator  with   __next__()  method')
# How to iterate list_iterator with __next__ method
print('Iterate   thru  list_iterator  with   for    loop')
# How to iterate list_iterator with for loop
print('Unpacks  List_iterator   :    ', ???)
'''
Output:
Iterate  list  with  for  loop
10
20
15
18
TypeError: 'list' object is not an iterator
<class 'list_iterator'>
<list_iterator object at 0x...>
Iterate   thru  list_iterator  with  next()  function
10
20
15
18
Iterate  thru  list_iterator  with   __next__()  method
10
20
15
18
Iterate   thru  list_iterator  with   for    loop
10
20
15
18
Unpacks  List_iterator   :     10 20 15 18
'''


# Program 16
# Find outputs
a = 25
print(a)
for x in a:
    print(x)
print(iter(a))
print(next(a))
'''
Output:
25
TypeError: 'int' object is not iterable
TypeError: 'int' object is not iterable
TypeError: 'int' object is not an iterator
'''
