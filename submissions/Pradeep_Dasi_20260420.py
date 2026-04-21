# How  to  iterate  zip  object  in  different  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) --> <class 'zip'>
print(z1) --> zip object address
print('Iterate  thru  zip  object  with   next()   function')
How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  __next__()  method')
How  to   iterate  thru  zip  object  with  __next__()  method
print('Iterate  thru  zip  object  with   for  loop')
How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')
How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , ???)
print()
print('zip   object  in  the  form  of   list  :  ' ,  ???)
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  ???)

z1 = zip(a, b)   # recreate (IMPORTANT: zip is iterator)
while True:
    try:
        print(next(z1))
    except StopIteration:
        break

print('\nIterate thru zip object with __next__() method')

z1 = zip(a, b)
while True:
    try:
        print(z1.__next__())
    except StopIteration:
        break
z1 = zip(a, b)
for item in z1:
    print(item)

print('\nElements of each tuple in zip object')

z1 = zip(a, b)
for x, y in z1:
    print(x, "->", y)

print('\nUnpacks zip object with * operator : ', list(zip(*zip(a, b))))

print('\nzip object in the form of list : ', list(zip(a, b)))

print('\nzip object in the form of dictionary : ', dict(zip(a, b)))





#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))
		time . sleep(1)
	except  StopIteration:
		break
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)



#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)




# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  
	time . sleep(1)
5
7
9



# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1) --> (10, 1)
	     (20, 3)
	     (30, 5)
z2 = zip(a , b . values())
disp(z2) --> (10, 2)
	     (20, 4)
	     (30, 6)
z3 = zip(a , b . items())
disp(z3) --> (10, (1, 2))
	     (20, (3, 4))
	     (30, (5, 6))
z4 = zip(a , b)
disp(z4) --> (10, 1)
	     (20, 3)
	     (30, 5)
z5 = zip(a)
disp(z5) --> (10,)
	     (20,)
             (30,)
z6 = zip(b)
disp(z6) --> (1,)
	     (3,)
   	     (5,)
z7 = zip()
disp(z7) --> here nothing will be printed



# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a) --> [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]




#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1)) -->  <class 'reversed'>
print(r1) --> reversed object
print('Iterate  thru  reversed  object  with   next   function') --> 
How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
How  to  iterate  reversed  object   with  __next__()   method
print('Iterate  thru  reversed  object  with   for  loop')
How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' ,  ???)
print('List  of  chars  in  reverse  order  :  ' ,  ???)
print('Reverse  string   :   ' , ???)

print('\nIterate thru reversed object with next function')
r1 = reversed(a)
while True:
  try:
     print(next(r1))
  except StopIteration:
      break
print('\nIterate thru reversed object with __next__ method')

r1 = reversed(a)
while True:
    try:
        print(r1.__next__())
    except StopIteration:
        break
print('\nIterate thru reversed object with for loop')

r1 = reversed(a)
for ch in r1:
    print(ch)
print('\nUnpack reversed object : ', list(reversed(a)))

print('List of chars in reverse order : ', list(reversed(a)))

print('Reverse string : ', ''.join(reversed(a)))



# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) --> <class 'reversed'>
print(b) --> <reversed object at 0x78a1ef629bd0>
print(id(b)) --> 2248845
print(*b) --> H Y D
print(b[0]) --> Error
print(b[1 : 3]) --> Error
print(b * 2) --> Error
print(len(b)) --> Error



# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) --> <class 'reversed'>
for  x  in   b:
	print(x)
	time . sleep(1)
-> True
-> Hyd
-> 10.8
-> 25



#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   next()   function
print('__next__()   method  iterates   thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   __next__()   method
print('for  loop  iterates  thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' ,  ???)
print('Reverse  list  :  '  ,  ???)

print(type(r1))   # <class 'list_reverseiterator'>
print(r1)

print('\nnext() function iterates thru list_reverseiterator object')
r1 = reversed(lst)
while True:
    try:
        print(next(r1))
    except StopIteration:
        break

print('\n__next__() method iterates thru list_reverseiterator object')

r1 = reversed(lst)
while True:
    try:
        print(r1.__next__())
    except StopIteration:
        break

print('\nfor loop iterates thru list_reverseiterator object')

r1 = reversed(lst)
for item in r1:
    print(item)

print('\nUnpack list_reverseiterator object : ', list(reversed(lst)))

print('Reverse list : ', list(reversed(lst)))



#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
--> No  (if you want reversed a set you have to convert it into list then we convert reversed)




# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(0.5)
		except  StopIteration:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a . keys())
disp(r1) --> 18
	     15
	     20
	     10
r2 = reversed(a . values()) 
disp(r2) --> Amar
	     Kiran
	     Sita
	     Rama
r3 = reversed(a . items())
disp(r3) -> (18, 'Amar')
	    (15, 'Kiran')
	    (20, 'Sita')
	    (10, 'Rama')
r4 = reversed(a)
disp(r4) --> 18
	     15
	     20
	     10



'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''

A dictionary itself cannot be reversed directly like a list.

d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}

rev_d = dict(reversed(list(d.items())))

print(rev_d)




# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary

import time
a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print('Keys in reverse order')
for k in reversed(list(a.keys())):
    print(k)

print('\nValues in reverse order')
for v in reversed(list(a.values())):
    print(v)

print('\nTuples in reverse order')
for item in reversed(list(a.items())):
    print(item)

print('\nElements of each tuple in reverse order')
for k, v in reversed(list(a.items())):
    print(v, k)   # reversed elements inside tuple

print('\nKeys and values in reverse order')
for k, v in reversed(list(a.items())):
    print(k, '->', v)






# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
How  to  iterate  list  with  for  loop
print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   __next__()  method')
How  to  iterate  list_iterator  with   __next__  method
print('Iterate   thru  list_iterator  with   for    loop')
How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  ???)

import time

lst = [10, 20, 15, 18]
print('Iterate list with for loop')
for x in lst:
    print(x)

list_itr1 = iter(lst)

print(type(list_itr1))   # <class 'list_iterator'>
print(list_itr1)

print('\nIterate thru list_iterator with next() function')

list_itr1 = iter(lst)
while True:
    try:
        print(next(list_itr1))
    except StopIteration:
        break

print('\nIterate thru list_iterator with __next__() method')

list_itr1 = iter(lst)
while True:
    try:
        print(list_itr1.__next__())
    except StopIteration:
        break

print('\nIterate thru list_iterator with for loop')

list_itr1 = iter(lst)
for x in list_itr1:
    print(x)
print(list(iter(lst)))




# Find  outputs
a = 25
print(a) --> 25
for  x   in   a:
	print(x)
print(iter(a)) -> Error
print(next(a)) -> Error
(here int is a non-sequence it cannot be iterable)



