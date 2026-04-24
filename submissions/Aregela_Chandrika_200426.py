# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)  #   intially empty zip object created
print(type(z1))   #   <class 'zip'>

print(z1)           # Address

print('Iterate  thru  zip  object  with   next()   function')
z1 = zip(a,b)     #How  to   iterate  thru  zip  object  with  next()  function

print('Iterate  thru  zip  object  with  __next__()  method')
How  to   iterate  thru  zip  object  with  __next__()  method

print('Iterate  thru  zip  object  with   for  loop')
z1.__next__()#How  to   iterate  thru  zip  object  with  for  loop

print('Elements  of  each  tuple  in  zip  object')
for state, capital in z1: #How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
    print(state,capital)

print('Unpacks  zip  object  with   *  operator  :  ' , *zip(a,b)))
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(zip(a,b)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(zip(a,b)))


----------------------------------------------------------------

#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))
		time . sleep(1)  # ('Empno', 25) <nextline> ('Emp Name', 'Rama Rao')  <nextline>  ('Salary', 10000.0) <nextline> StopIteration
	except  StopIteration:
		break


-------------------------------------------------------

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
    
------------------------------------------------------------

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  # 5 <nextline> 7 <nextline> 9
	time . sleep(1)
    
----------------------------------------------------------------


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
z2 = zip(a , b . values())
disp(z2)
z3 = zip(a , b . items())
disp(z3)
z4 = zip(a , b)
disp(z4)
z5 = zip(a)
disp(z5)
z6 = zip(b)
disp(z6)
z7 = zip()
disp(z7)


'''
z1 returns --> (10, 1) <nextline> (20, 3) <nextline> (30, 5)
z2 returns --> (10, 2) <nextline> (20, 4) <nextline> (30, 6)
z3 returns --> (10, (1, 2)) <nextline> (20, (3, 4)) <nextline> (30, (5, 6))
z4 returns --> (10, 1) <nextline> (20, 3) <nextline> (30, 5)
z5 returns -->  (10,) <nextline> (20,) <nextline> (30,)
z6 returns --> (1,) <nextline> (3,) <nextline> (5,)
z7 returns --> returns nothing '''
----------------------------------------------------------------

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]   
print(a) # (0,20),(1,21),(2,22),(3,23),(4,24)

# range(5) ---> 0,1,2,3,4
# range(20,25) ---> 20,21,22,23,24


---------------------------------------------------------------

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a) # Empty reversed object is created
print(type(r1)) # <class 'reversed'>
print(r1) 

print('Iterate  thru  reversed  object  with   next   function')
r1 = reversed(a)   #How  to  iterate  reversed  object  'r'  with  next()  function
while True:
    try:
        print(r1.__next__())
    except StopIteration:
        break

print('Iterate  thru  reversed  object  with   __next__   method')
r1.__next__()     #How  to  iterate  reversed  object   with  __next__()   method

print('Iterate  thru  reversed  object  with   for  loop')
for ch in r1: #How  to  iterate  reversed  object   with  for  loop
    print(ch)


print('Unpack  reversed  object  : ' ,  *reversed(a))
print('List  of  chars  in  reverse  order  :  ' ,  list(reversed(a)))
print('Reverse  string   :   ' , ''.join(reversed(a)))



----------------------------------------------------------------


# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a) # 
print(type(b)) # <class 'reversed'>
print(b)  # Address
print(id(b)) # Addrss
print(*b) # D Y H
print(b[0]) # Error 
print(b[1 : 3]) # Error
print(b * 2) # Error
print(len(b)) # error


-----------------------------------------------------------------


# Can  tuple  be  reversed ?  YES
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x) # True <nl> Hyd <nl> 10.8 <nl> 25
	time . sleep(1)
    
    
------------------------------------------------------------------

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1)) # <class 'list_reverseiterator'>
print(r1)

print('next()   function  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
while True:
    try:
        print(next(r1))
        time.sleep(0.5)
    except StopIteration:
        break      
print('__next__()   method  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
while True:
    try:
        print(r1.__next__())
    except StopIteration:
        break
        
print('for  loop  iterates  thru  list_reverseiterator  object')
for x in r1:
    print(x)

print('Unpack  list_reverseiterator  object  :  ' ,  *reversed(lst)))
print('Reverse  list  :  '  ,  list(reversed(lst)))



---------------------------------------------------------------------

#  Can  set  be  reversed  ?  No
a = {10, 20, 15 , 18}
r = reversed(a)


--------------------------------------------------------------------

# Can  dictionary  be  reversed  ? 
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
r1 returns ---> 18 <nl> 15 <nl> 20 <nl> 10
r2 returns ---> Rama <nl> sita <nl> kiran <nl> Amar
r3 returns ---> (18, 'Amar') <nl> (15, 'Kiran') <nl> (20, 'Sita')  <nl> (10, 'Rama')
r4 returns --->  Error
'''


-----------------------------------------------------------------------



'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''

a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
rev = dict(reversed(a.items()))
print(rev)

--------------------------------------------------------------------------



# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
#Write  for  loop  to  reverse  keys  of  dictionary
for k in reversed(a.keys()):
    print(k)
    time.sleep(1)

print('Values  in  reverse  order')
for v in reversed(a.values()):
    print(v)
    time.sleep(0.5)


print('Tuples  in   reverse  order')
for t in reversed(a.items()):
    print(t)
    time.sleep(0.5)

print('Elements  of  each   tuple  in  reverse  order')
for k, v in reversed(a.items()):
    print(v, k)
    time.sleep(0.5)


print('Keys  and  values  in   reverse   order')
for k, v in reversed(a.items()):
    print(k, '->', v)
    time.sleep(0.5)


---------------------------------------------------------------------------


# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]

print('Iterate  list  with  for  loop')
for x in lst:
    print(x)
    time.sleep(0.5)
    
 
print(next(list))
list_itr1 = iter(list) 

print(type(list_itr1)) #  <class 'list_iterator'>
print(list_itr1)

print('Iterate   thru  list_iterator  with  next()  function')
list_itr1 = iter(lst)
while True:
    try:
        print(next(list_itr1))
        time.sleep(0.5)
    except StopIteration:
        break

print('Iterate  thru  list_iterator  with   __next__()  method')
list_itr1 = iter(lst)
while True:
    try:
        print(list_itr1.__next__())
    except StopIteration:
        break

print('Iterate   thru  list_iterator  with   for    loop')
list_itr1 = iter(lst)
for x in list_itr1:
    print(x)
print('Unpacks  List_iterator   :    ' ,  *iter(lst))


-----------------------------------------------------------------------------


# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x) # 25
print(iter(a)) # error 
print(next(a)) # error