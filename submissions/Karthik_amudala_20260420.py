# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) # <class 'zip'>
print(z1) # type and address of object 'z1'
print('Iterate  thru  zip  object  with   next()   function')
print(next(z1)) # How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  _next_()  method')
print(z1.__next__()) # How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
for x in z1:
    print(x) # How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')
z1 = zip(a, b)
for s,c in z1:
    print(s, c) # How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , *(zip(a, b)))
print()
print('zip   object  in  the  form  of   list  :  ' , list(zip(a, b)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(zip(a, b))) 
'''
Iterate thru zip object with next() function
('Telangana', 'Hyderabad')

Iterate thru zip object with __next__() method
('Andhra Pradesh', 'Amaravathi')

Iterate thru zip object with for loop
('Karnataka', 'Bangalore')
('Tamilnadu', 'Chennai')

Elements of each tuple in zip object
Telangana Hyderabad
Andhra Pradesh Amaravathi
Karnataka Bangalore
Tamilnadu Chennai

Unpacks zip object with * operator :  ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka', 'Bangalore') ('Tamilnadu', 'Chennai')

zip object in the form of list :  [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip object in the form of dictionary :  {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka': 'Bangalore', 'Tamilnadu': 'Chennai'}
'''
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
'''
('Empno', 25)
('Emp Name', 'Rama Rao')
('Salary', 10000.0)
'''
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''
('Telangana', 'Hyderabad', 50000000)
('Andhra Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  
	time . sleep(1)
'''
5
7
9
'''
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
disp(z1)
'''
(10, 1)
(20, 3)
(30, 5)
'''
z2 = zip(a , b . values())
disp(z2)
'''
(10, 2)
(20, 4)
(30, 6)
'''
z3 = zip(a , b . items())
disp(z3)
'''
(10, (1, 2))
(20, (3, 4))
(30, (5, 6))
'''
z4 = zip(a , b)
disp(z4)
'''
(10, 1)
(20, 3)
(30, 5)
'''
z5 = zip(a)
disp(z5)
'''
(10,)
(20,)
(30,)
'''
z6 = zip(b)
disp(z6)
'''
(1,)
(3,)
(5,)
'''
z7 = zip()
disp(z7) # stop iteration error
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)
'''
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1)) # <class 'reversed'>
print(r1) # type and address of object 'r1'
print('Iterate  thru  reversed  object  with   next   function')
r1 = reversed(a)
print(next(r1))
print(next(r1))
print(next(r1)) # How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   _next_   method')
r1 = reversed(a)
print(r1.__next__()) # How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
r1 = reversed(a)
for x in r1:
    print(x) # How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' ,  *(reversed(a)))
print('List  of  chars  in  reverse  order  :  ' , list(reversed(a)))
print('Reverse  string   :   ' , "".join(reversed(a)))
'''
Iterate thru reversed object with next function
D
Y
H

Iterate thru reversed object with __next__ method
D
Y
H

Iterate thru reversed object with for loop
D
Y
H

Unpack reversed object :  D Y H
List of chars in reverse order :  ['D', 'Y', 'H']
Reverse string :  DYH
'''   
# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # type and address of oject 'b'
print(id(b)) # address of object 'b'
print(*b) # Y D H
print(b[0])  # ERROR because no indexing for iterator
print(b[1 : 3]) # ERROR because no slicing because no indexing for iterator
print(b * 2) # ERROR because no repetation for iterator
print(len(b)) # ERROR because len() expects sequence as argument

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x)
	time . sleep(1)
'''
True
Hyd
10.8
25
'''
#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1)) # <class 'list_reverseiterator'>
print(r1) # Type and address of object 'r1'
print('next()   function  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst) 
print(next(r1)) # How  to  iterate   list_reverseiterator  object  with   next()   function
print('_next_()   method  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
print(r1.__next__()) # How  to  iterate   list_reverseiterator  object  with   _next_()   method
print('for  loop  iterates  thru  list_reverseiterator  object')
r1 = reversed(lst)
for x in r1:
    print(x)
    time.sleep(1) # How  to  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' , *(reversed(lst)))
print('Reverse  list  :  '  ,  list(reversed(lst)))
'''
next() function iterates thru list_reverseiterator object
True
Hyd
10.8
25

__next__() method iterates thru list_reverseiterator object
True
Hyd
10.8
25

for loop iterates thru list_reverseiterator object
True
Hyd
10.8
25

Unpack list_reverseiterator object :  True Hyd 10.8 25
Reverse list :  [True, 'Hyd', 10.8, 25]
'''
#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # ERROR because set can't be reversed

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
disp(r1)
'''
18
15
20
10
'''
r2 = reversed(a . values())
disp(r2)
'''
Amar
Kiran
Sita
Rama
'''
r3 = reversed(a . items())
disp(r3)
'''
(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')
'''
r4 = reversed(a)
disp(r4)
'''
18
15
20
10
'''

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?
Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}
Hint :  Both  input  and  output  are  dictionaries

Sample output:
Enter a dictionary :
{'Empno' : 25 'Emp Name' : 'Rama Rao' 'Sal' 10000.0} 
Reverse dictionary : {'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}
'''
d = eval(input('Enter a dictionary : '))
rev_d = {}
for k, v in reversed(list(d.items())):
    rev_d[k] = v
print('Reverse dictionary :', rev_d)

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for k in reversed(list(a.keys())):
    print(k) # Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
for v in reversed(list(a.values())):
    print(v) # Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
for t in reversed(list(a.items())):
    print(t) # Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
for k, v in reversed(list(a.items())):
    print((v, k)) # Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
for k in reversed(list(a.keys())):
    print(k, a[k]) # Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
'''
Keys in reverse order
18
15
20
10

Values in reverse order
Kiran
Rajesh
Sita
Rama rao

Tuples in reverse order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')

Elements of each tuple in reverse order
('Kiran', 18)
('Rajesh', 15)
('Sita', 20)
('Rama rao', 10)

Keys and values in reverse order
18 Kiran
15 Rajesh
20 Sita
10 Rama rao
'''
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for i in lst:
    print(i) # How  to  iterate  list  with  for  loop
print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
list_itr1 = iter(lst)
print(next(list_itr1))
print(next(list_itr1))
print(next(list_itr1))
print(next(list_itr1)) # How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
list_itr1 = iter(lst)
print(list_itr1.__next__())
print(list_itr1.__next__())
print(list_itr1.__next__())
print(list_itr1.__next__())  # How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
list_itr1 = iter(lst)
for i in list_itr1:
    print(i) # How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  *iter(lst))
'''
Iterate list with for loop
10
20
15
18

<class 'list_iterator'>
<list_iterator object at ...>

Iterate thru list_iterator with next() function
10
20
15
18

Iterate thru list_iterator with __next__() method
10
20
15
18

Iterate thru list_iterator with for loop
10
20
15
18

Unpacks List_iterator : 10 20 15 18
'''
# Find  outputs
a = 25
print(a) # 25
for  x   in   a:
	print(x) # Error because 25 is integer which is not iterable
print(iter(a)) # Error
print(next(a)) # Error