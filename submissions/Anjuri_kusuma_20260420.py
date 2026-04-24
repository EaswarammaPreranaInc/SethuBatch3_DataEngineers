 # How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
print(next(z1))  #How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  _next_()  method')
print(z1.__next__())  #How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
for x in z1:  #How  to   iterate  thru  zip  object  with  for  loop
	print(x)
print('Elements  of  each  tuple  in  zip  object')
#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , ???)
print()
print('zip   object  in  the  form  of   list  :  ' ,  ???)
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  ???)
--------------------------------------------------------------------------------------------
 #  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z)) (Empno,25)/n(Emp Name,Rama Rao)/n(Salary,10000.0)
		time . sleep(1)
	except  StopIteration:
		break
--------------------------------------------------------------------------------------------
 #  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)        
	time . sleep(1)
(Telangana,Hyderabad,50000000)
(Andhra Pradesh,Amaravathi,40000000)
(Karnataka,Banglore,70000000)
(TamilNadu,Chennai,60000000)
(Maharastra,Mumbai,30000000)
--------------------------------------------------------------------------------------------
 # Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)     #5 /n 7 /n 9
	time . sleep(1)
---------------------------------------------------------------------------------------------
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
disp(z1)            #(10,1) /n (20,3) /n (30,5)
z2 = zip(a , b . values())
disp(z2)            #(10,2) /n (20,4) /n (30,6)
z3 = zip(a , b . items())
disp(z3)            #(10,(1,2)) /n (20,(3,4)) /n (30,(5,6))
z4 = zip(a , b)
disp(z4)            #(10,1) /n (20,3) /n (30,5)
z5 = zip(a)
disp(z5)             #(10,) /n (20,) /n (30,)
z6 = zip(b)
disp(z6)             #(1,) /n (3,) /n (5,)
z7 = zip()
disp(z7)             #Nothing gets printed
-----------------------------------------------------------------------------------------------
 # Find  outputs  (Home  work)        range(5)=(0,1,2,3,4)
z = zip(range(5) , range(20 , 25))    range(20,25)=(20,21,22,23,24)
a = [ [x , y]  for  x , y   in   z]  
print(a)   #[0,20] /n [1,21] /n [2,22] /n [3,23] /n [4,24]
----------------------------------------------------------------------------------------------
 #  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
print(next(r1))  #How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   _next_   method')
print(r1.__next__())  #How  to  iterate  reversed  object   with  _next_()   method
print('Iterate  thru  reversed  object  with   for  loop')
for x in r1: #How  to  iterate  reversed  object   with  for  loop
	print(x)
print('Unpack  reversed  object  : ' ,  *r1)
print('List  of  chars  in  reverse  order  :  ' ,  list(reversed(a))
print('Reverse  string   :   ' , a[::-1])
--------------------------------------------------------------------------------------------
 # Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))  #<class'reversed'>
print(b)       #type and add
print(id(b))   #some add
print(*b)      #D,Y,H
print(b[0])    #error
print(b[1 : 3]) #error
print(b * 2)    #error
print(len(b))   #error
-------------------------------------------------------------------------------------------
# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))   #<class'reversed'>
for  x  in   b:
	print(x)   #True ,Hyd, 10.8, 25
	time . sleep(1)
--------------------------------------------------------------------------------------------
 #  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)
print('next()   function  iterates   thru  list_reverseiterator  object')
print(next(r1))  #How  to  iterate   list_reverseiterator  object  with   next()   function
print('_next_()   method  iterates   thru  list_reverseiterator  object')
print(r1.__next__())  #How  to  iterate   list_reverseiterator  object  with   _next_()   method
print('for  loop  iterates  thru  list_reverseiterator  object')
for x in r1:  #How  to  iterate   list_reverseiterator  object  with   for  loop
	print(x)
print('Unpack  list_reverseiterator  object  :  ' ,  *r1)
print('Reverse  list  :  '  ,  ???)
------------------------------------------------------------------------------------------
 #  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)   #No because it is unordered
------------------------------------------------------------------------------------------
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
disp(r1)           #(18,16,20,10)
r2 = reversed(a . values())
disp(r2)           #(Amar,Kiran,Sita,Rama)
r3 = reversed(a . items())
disp(r3)        #((18,Amar),(15,Kiran),(20,Sita),(10,Rama))
r4 = reversed(a)
disp(r4)       #(18,16,20,10)
--------------------------------------------------------------------------------------------
 '''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries

d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}

rev = dict(reversed(list(d.items())))
print(rev)
----------------------------------------------------------------------------------------
 # Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for x in reversed(list(a.keys)):  Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
for x in reversed(list(a.values)):   #Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
for x in reversed(list(a.items)):    #Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
for x,y in reversed(list(a.items)):    #Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
----------------------------------------------------------------------------------------
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
print('Iterate  thru  list_iterator  with   _next_()  method')
How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  ???)
----------------------------------------------------------------------------------------
# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))