# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
print(next(z1))#How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  __next__()  method')
print(z1.__next__())#How  to   iterate  thru  zip  object  with  __next__()  method
print('Iterate  thru  zip  object  with   for  loop')
for i in z1:#How  to   iterate  thru  zip  object  with  for  loop
    print(i)
print('Elements  of  each  tuple  in  zip  object')
for state, city in zip(a,b):#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
    print(f'{state} ... {city}')
print('Unpacks  zip  object  with   *  operator  :  ' , list(z1(*z1)))
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(zip(a,b)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(zip(a,b)))
'''
<class 'zip'>
<zip object at 0x000001A3CF07FD00>
Iterate  thru  zip  object  with   next()   function
('Telangana', 'Hyderabad')
Iterate  thru  zip  object  with  __next__()  method
('Andhra Pradesh', 'Amaravathi')
Iterate  thru  zip  object  with   for  loop
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Elements  of  each  tuple  in  zip  object
Telangana ... Hyderabad
Andhra Pradesh ... Amaravathi
Karnataka  ... Bangalore
Tamilnadu ... Chennai
Error

zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}
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
(Empno 25)
(Empname Rama Rao)
(Salary 10000.0)
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
('Telangana','Hyderabad'50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai' 60000000)
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
disp(z1) # (10, 1) <next line> (20, 3) <next line> (30, 5)
z2 = zip(a , b . values())
disp(z2) # (10, 2) <next line> (20, 4) <next line> (30, 6)
z3 = zip(a , b . items())
disp(z3) # (10, (1, 2))<next line>(20, (3,4))<next line>(30(5,6))
z4 = zip(a , b)
disp(z4) # (10, 1) <next line> (20, 3) <next line> (30, 5)
z5 = zip(a)
disp(z5) # (10,) <nextline> (20,) <nextline> (30,)
z6 = zip(b)
disp(z6) # (1,) <nextline> (3,) <nextline>(5,)
z7 = zip()
disp(z7) # empty

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]] '''

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
print(next(r1))
print('Iterate  thru  reversed  object  with   _next_   method')
print(r1._next_()) # Error
print('Iterate  thru  reversed  object  with   for  loop')
for char in r1:
    print(char)
print('Unpack  reversed  object  : ' , list(reversed(a)))
print('List  of  chars  in  reverse  order  :  ' , list(reversed(a)))
print('Reverse  string   :   ' , ''.join(reversed(a)))
'''
<class 'reversed'>
<reversed object at 0x000001A745C294E0>
Iterate  thru  reversed  object  with   next   function
D
Iterate  thru  reversed  object  with   _next_   method
Iterate  thru  reversed  object  with   for  loop
Y
H
Unpack  reversed  object  :  ['D', 'Y', 'H']
List  of  chars  in  reverse  order  :   ['D', 'Y', 'H']
Reverse  string   :    DYH
'''
      
# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0])
print(b[1 : 3])
print(b * 2)
print(len(b))
'''
Output:
<class 'reversed'>
<reversed object at 0x7f8c8c8c8c8
140737488355328>
DYH
Error 
'''

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
'''
Output:
True
Hyd
10.8
25
'''

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
while True: #How  to  iterate   list_reverseiterator  object  with   next()   function
    try:
        print(next(r1))
    except StopIteration:
        break
print('__next__()   method  iterates   thru  list_reverseiterator  object')
while True: #How  to  iterate   list_reverseiterator  object  with   __next__()   method
    try:
        print(r1.__next__())
    except StopIteration:
        break
print('for  loop  iterates  thru  list_reverseiterator  object')
print('Unpack  list_reverseiterator  object  :  ' ,  list(reversed(lst)))
print('Reverse  list  :  '  ,  list(reversed(lst)))
'''
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x0000021D861F9690>
next()   function  iterates   thru  list_reverseiterator  object
True
Hyd
10.8
25
__next__()   method  iterates   thru  list_reverseiterator  object
for  loop  iterates  thru  list_reverseiterator  object
Unpack  list_reverseiterator  object  :   [True, 'Hyd', 10.8, 25]
Reverse  list  :   [True, 'Hyd', 10.8, 25]
'''
#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # error

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
disp(r1) # 18<next line>15<next line>20<next line>10
r2 = reversed(a . values())
disp(r2) # Amar<next line>kiran<next line>Sita<next line>Rama
r3 = reversed(a . items())
disp(r3) # (18, Amar) <next line> (15, kiran) <next line> (20 sita) <next line> (10, Rama)
r4 = reversed(a)
disp(r4) # 18<next line>15<next line>20<next line>10

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
a = {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
reversed_dict = dict(reversed(list(a.items())))
print(reversed_dict)

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for keys in reversed(a.keys()):#Write  for  loop  to  reverse  keys  of  dictionary
    print(keys)
    time.sleep(1)
print('Values  in  reverse  order')
for values in reversed(a.values()): #Write  for  loop  to  reverse  values  of  dictionary
    print(values)
    time.sleep(1)
print('Tuples  in   reverse  order')
for items in reversed(a.items()): #Write  for  loop  to  reverse   tuples   of  dictionary
    print(items)
print('Elements  of  each   tuple  in  reverse  order')
for  keys, values in reversed(a.items()) : #Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
    print(f'{keys}, {values}')
    time.sleep(1)
print('Keys  and  values  in   reverse   order')
for keys, values in (list(a.items())):#Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
    print(keys, values)
    time.sleep(1)
'''
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
18, Kiran
15, Rajesh
20, Sita
10, Rama rao
Keys  and  values  in   reverse   order
10 Rama rao
20 Sita
15 Rajesh
18 Kiran
'''

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for i in list : #How  to  iterate  list  with  for  loop
    print(i)
    time.sleep(1)
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
print(next(list_itr1))#How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   __next__()  method')
print(list_itr1.__next__())#How  to  iterate  list_iterator  with   __next__  method
print('Iterate   thru  list_iterator  with   for    loop')
for items in list_itr1: #How  to  iterate  list_iterator  with  for  loop
    print(items)
    time.sleep(1)
print('Unpacks  List_iterator   :    ' ,  list(list_itr1))
'''
Iterate  list  with  for  loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x000001F747BD0580>
Iterate   thru  list_iterator  with  next()  function
10
Iterate  thru  list_iterator  with   __next__()  method
20
Iterate   thru  list_iterator  with   for    loop
15
18
Error
'''
      
# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a)) 
print(next(a)) 
'''
Error 
25 
Error
'''