1) How  to  iterate  zip  object  in  differenet  ways 
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
z2 = zip(a, b)
print(next(z2)) #How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  _next_()  method')
z3 = zip(a, b)
print(z3.__next__()) #How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
z4 = zip(a, b)
for item in z4:
    print(item) #How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')
z5 = zip(a, b)
for x, y in z5:
    print(x, '->', y) #How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , ???)
print()
print('zip   object  in  the  form  of   list  :  ' ,  ???)
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  ???)

2) outputs  
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
#('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
stopiteration error

3) outputs 
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
#('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
stopiteration error

4) outputs  
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  #5
		       7
		       9
		       stop iteration error
	time . sleep(1)

5) outputs 
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
#(10, 1)
(20, 3)
(30, 5)
stop iteration error
z2 = zip(a , b . values())
disp(z2)
#(10, 2)
(20, 4)
(30, 6)
stop iteration error
z3 = zip(a , b . items())
disp(z3)
#(10, (1, 2))
(20, (3, 4))
(30, (5, 6))
stop iteration error
z4 = zip(a , b)
disp(z4)
#(10, 1)
(20, 3)
(30, 5)
stop iteration error
z5 = zip(a)
disp(z5)
#(10,)
(20,)
(30,)
stop iteration error
z6 = zip(b)
disp(z6)
#(1,)
(3,)
(5,)
stop iteration error
z7 = zip()
disp(z7)
#stop iteration error at the start

6) outputs  
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]

7) How  to  print  reversed  object  in  different  way
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   _next_   method')
How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' ,  ???)
print('List  of  chars  in  reverse  order  :  ' ,  ???)
print('Reverse  string   :   ' , ???)

8) outputs 
a = 'HYD'
b = reversed(a)
print(type(b))#<class 'reversed'>
print(b)#Type and address of object b
print(id(b))#addres of object b
print(*b)#D Y H
print(b[0])#Error because str has no indexes
print(b[1 : 3])#No indexes no slicing
print(b * 2)#Not possible
print(len(b))#Not possible

9) Can  tuple  be  reversed ?  
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))#<class 'reversed'>
for  x  in   b:
	print(x)#True <nextline> Hyd <nextline> 10.8 <nextline> 25
	time . sleep(1)

10) How  to  print  list_reverseiterator  object  in  different  ways  
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   next()   function
print('_next_()   method  iterates   thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   _next_()   method
print('for  loop  iterates  thru  list_reverseiterator  object')
How  to  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' ,  ???)
print('Reverse  list  :  '  ,  ???)

11) Can  set  be  reversed  ?  
a = {10, 20, 15 , 18}
r = reversed(a)#Error because it is not permitted

12) Can  dictionary  be  reversed ?
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
#18
15
20
10
r2 = reversed(a . values())
disp(r2)
#Amar
Kiran
Sita
Rama
r3 = reversed(a . items())
disp(r3)
#(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')
r4 = reversed(a)
disp(r4)
#18
15
20
10

13) Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
#a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
rev = dict(reversed(list(a.items())))

print(rev)

14) outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for k in reversed(list(a.keys())):
    print(k) #Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
for v in reversed(list(a.values())):
    print(v) #Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
for item in reversed(list(a.items())):
    print(item) #Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
for k, v in reversed(list(a.items())):
    print((v, k)) #Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
for k, v in reversed(list(a.items())):
    print(k, v) #Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary

15) How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in lst:
    print(x) #How  to  iterate  list  with  for  loop
print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
print(next(list_itr1))
print(next(list_itr1)) #How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
print(list_itr2.__next__())
print(list_itr2.__next__()) #How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
for x in list_itr3:
    print(x) #How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  ???)

16) outputs
a = 25
print(a)
for  x   in   a:
	print(x)#25
print(iter(a))#int object is not iterable
print(next(a))