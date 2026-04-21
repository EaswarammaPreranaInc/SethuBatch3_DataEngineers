# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1) # <class 'zip' object at 0x7f8c9c1e5d00>
print('Iterate  thru  zip  object  with   next()   function') # Iterate  thru  zip  object  with   next()   function
# How  to   iterate  thru  zip  object  with  next()  function

print(next(z1)) # ('Telangana', 'Hyderabad')
print(next(z1)) # ('Andhra Pradesh', 'Amaravathi')
print(next(z1)) # ('Karnataka ', 'Bangalore')
print(next(z1)) # ('Tamilnadu', 'Chennai')
print('Iterate  thru  zip  object  with  __next__()  method') # Iterate  thru  zip  object  with  __next__()  method
# How  to   iterate  thru  zip  object  with  __next__()  method
z2 = zip(a , b)
print(z2.__next__()) # ('Telangana', 'Hyderabad')
print(z2.__next__()) # ('Andhra Pradesh', 'Amaravathi')
print(z2.__next__()) # ('Karnataka ', 'Bangalore')
print(z2.__next__()) # ('Tamilnadu', 'Chennai')
print('Iterate  thru  zip  object  with   for  loop') # Iterate  thru  zip  object  with   for  loop
# How  to   iterate  thru  zip  object  with  for  loop
z3 = zip(a , b)
for x in z3:
    print(x)
print('Elements  of  each  tuple  in  zip  object') # Elements  of  each  tuple  in  zip  object
# How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
for x , y in zip(a , b):
	print(x , '----->' , y)
z5 = zip(a , b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()
z6 = zip(a , b)
print('zip   object  in  the  form  of   list  :  ' ,  list(z6))
print()
z7 = zip(a , b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z7))

#  Find  outputs  
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z)) # ('Empno' , 25) 1sec \n ('Emp Name', 'Rama Rao') 1sec \n ('Salary', 10000.0)
		time . sleep(1)
	except  StopIteration:
		break

#  Find  outputs 
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x) # ('Telangana', 'Hyderabad', 50000000) 1sec \n ('Andhra  Pradesh', 'Amaravathi', 40000000) 1sec \n ('Karnataka', 'Banglore', 70000000) 1sec \n ('TamilNadu', 'Chennai', 60000000) 1sec \n ('Maharastra', 'Mumbai', 30000000)
	time . sleep(1)

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) # 5 1sec \n 7 1sec \n 9 1sec
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
disp(z1) # (10, 1) (20, 3) (30, 5)
z2 = zip(a , b . values()) 
disp(z2) # (10, 2) (20, 4) (30, 6)
z3 = zip(a , b . items())
disp(z3) # (10, (1, 2)) (20, (3, 4)) (30, (5, 6))
z4 = zip(a , b)
disp(z4) # (10, 1) (20, 3) (30, 5)
z5 = zip(a)
disp(z5) # (10,) (20,) (30,)
z6 = zip(b)
disp(z6) # (1,) (3,) (5,)
z7 = zip()
disp(z7) # stop iteration error in next() because zip() returns an empty iterator

# Find  outputs  
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)  
print(type(r1)) # <class 'reversed'>  #  reversed  object
print(r1) # <reversed object at 0x7f8c8c8c8c8c> 
print('Iterate  thru  reversed  object  with   next   function') # Iterate  thru  reversed  object  with   next   function
# How  to  iterate  reversed  object  'r'  with  next()  function
next(r1) # D
next(r1) # Y
next(r1) # H
print('Iterate  thru  reversed  object  with   __next__   method') # Iterate  thru  reversed  object  with   __next__   method
# How  to  iterate  reversed  object   with  __next__()   method
r2 = reversed(a)
print(r2.__next__())# D
print(r2.__next__())# Y
print(r2.__next__())# H
print('Iterate  thru  reversed  object  with   for  loop') # Iterate  thru  reversed  object  with   for  loop
# How  to  iterate  reversed  object   with  for  loop
r3 = reversed(a)
for x in r3:
    print(x) # D Y H
r4 = reversed(a)
print('Unpack  reversed  object  : ' ,  *r4) # d y H
r5 = reversed(a)
print('List  of  chars  in  reverse  order  :  ',  list(r5)) # ['d', 'Y', 'H']
print('Reverse  string   :   ' , ''.join(reversed(a))) # DYH

# Find  outputs a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # <reversed object at 0x7f8c8c8c8c8>
print(id(b)) # 140123456789012
print(*b) # DYH
# print(b[0]) # reversed object is not suscriptable
# print(b[1 : 3]) # index error
# print(b * 2) # DYH DYH
print(len(b)) # TypeError: object of type 'reversed' has no len()

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))  #<class 'reversed'>
for  x  in   b:
	print(x)
	time . sleep(1)

'''
True
'Hyd'
10.8
25
'''

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))  #<class 'reversed'>
print(r1)  #Type and address
print('next()   function  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(next(r1))
    except:
        break
r2=reversed(lst)    
print('__next__()   method  iterates   thru  list_reverseiterator  object')
while True:
    try:
        print(r1.__next__())
    except:
        break
r3=reversed(lst)
print('for  loop  iterates  thru  list_reverseiterator  object')
for x in r3:
    print(x)
r4=reversed(lst)
print('Unpack  list_reverseiterator  object  :  ' ,  *r4)
print('Reverse  list  :  '  ,  lst[::-1])

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)

'''
error
'''

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
r2 = reversed(a . values())
disp(r2)
r3 = reversed(a . items())
disp(r3)
r4 = reversed(a)
disp(r4)

'''
18 
15 
20 
10
'Amar' 
'Kiran' 
'Sita' 
'Rama'
(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')
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
'''

a=eval(input('Enter a dictionary: '))
b=reversed(a)
c={}
for x in b:
    c[x]=a[x]
print('Reversed dictionary: ',c)

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
b=reversed(a)
print('Keys  in   reverse   order')
for x in b:
    print(x)
    c=reversed(a)
c=reversed(a.values())
for x in c:
    print(x)
print('Tuples  in   reverse  order')
d=reversed(a.items())
for x in d:
    print(x)
print('Elements  of  each   tuple  in  reverse  order')
e=reversed(a.items())
for x,y in e:
    print(x,y)
print('Keys  and  values  in   reverse   order')
f=reversed(a)
for x in f:
    print(x,a[x])

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:
    print(x)
print(next(list))  #error-next() fun argument must be iterator
list_itr1 = iter(list)
print(type(list_itr1))  #<class 'list_iterator'>
print(list_itr1)  #Type and address
print('Iterate   thru  list_iterator  with  next()  function')
while True:
	try:
		print(next(list_itr1))
	except:
		break
print('Iterate  thru  list_iterator  with   __next__()  method')
list_itr2 = iter(list)
while True:
	try:
		print(list_itr2.__next__())
	except:
		break
print('Iterate   thru  list_iterator  with   for    loop')
list_itr3=iter(list)
for x in list_itr3:
	print(x)
list_itr4=iter(list)
print('Unpacks  List_iterator   :    ' ,  *list_itr4)

# Find  outputs
a = 25
print(a)  #25
for  x   in   a:   #error-non seq cannot be iterated
	print(x)  
print(iter(a)) #error-argument must be sequeence
print(next(a))  #error-argument must be a iterator