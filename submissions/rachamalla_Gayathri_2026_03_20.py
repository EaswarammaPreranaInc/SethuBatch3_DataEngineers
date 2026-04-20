# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)#('Telangana','Hyderabad')
(' 'Andhra Pradesh' , 'Amaravathi')
('Karnataka ','Bangalore')
('Tamilnadu', 'Chennai')
print(type(z1))#<class 'zip'>
print(z1)#address and object
print('Iterate  thru  zip  object  with   next()   function')
z1=zip(a,b)
print(z1.__next__())
How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  _next_()  method')
z1=zip(a,b)
foir x in z1:
print(x)
How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
#z1zip(a,b)
for x,y in z1:
print(x,"->",y)
How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')

How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , ???)
print()

z1=zip(a,b)
print(*z1)
print('zip   object  in  the  form  of   list  :  ' , z1)
print()
print('zip   object  in  the  form  of   dictionary :  ' , z1)
#  Find  outputs  (Home  work)
import   time
a = [ 'Em pno', 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
#('Em pno',25)
('Emp Name','Rama  Rao')
('Salary',10000.0)
while   True:
	try:
		print(next(z))
		time . sleep(1)
	except  StopIteration:
		break
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

#('Telangana' ,['Hyderabad',50000000)
('Andhra  Pradesh','Amaravathi' ,40000000)
('Karnataka','Karnataka',70000000)
('TamilNadu', 'Chennai',60000000 )
('Maharastra','Mumbai',30000000)

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  #(5,7,9)
	time . sleep(1)
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
disp(z1)#(10,1)(20,3)(30,5)
z2 = zip(a , b . values())
disp(z2)#(10,2)(20,4)(30,6)
z3 = zip(a , b . items())
disp(z3)#(10,(1,2))(20,(3,4))(30,(5,6))
z4 = zip(a , b)
disp(z4)#(10,1)(20,3)(30,5)
z5 = zip(a)
disp(z5)#(10,)(20,)(30,)
z6 = zip(b)
disp(z6)#(1,)(3,)(5,)
z7 = zip()
disp(z7)#empt
 # Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)

#[[0,20],[1,21],[2,22],[3,22],[4,24]]
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))#reverseiterator
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
# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)#error
print(type(b))#<class str'>
print(b)# 'dyh'
print(id(b))#
print(*b)
print(b[0])
print(b[1 : 3])
print(b * 2)
print(len(b))
# Can  tuple  be  reversed ?   (Home  work)#yes
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
[1:04 pm, 20/04/2026] SRINIVAS Sir Maths: #  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
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
[1:04 pm, 20/04/2026] SRINIVAS Sir Maths: #  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
[1:04 pm, 20/04/2026] SRINIVAS Sir Maths: # Can  dictionary  be  reversed  ? (Home  work)
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
r2 = reversed(a . values())
disp(r2)
r3 = reversed(a . items())
disp(r3)
r4 = reversed(a)
disp(r4)
[1:05 pm, 20/04/2026] SRINIVAS Sir Maths: '''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
[1:05 pm, 20/04/2026] SRINIVAS Sir Maths: # Find outputs
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
[1:15 pm, 20/04/2026] SRINIVAS Sir Maths: # How  to  iterate   list_iterator  in  different  ways
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
 # Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))#error