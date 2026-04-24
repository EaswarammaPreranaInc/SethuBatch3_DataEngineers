# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) #<class 'zip'>
print(z1) # class 'zip' at 0x   
print('Iterate  thru  zip  object  with   next()   function')
while True:
    try:
        print(next(z1))
    except:
        break
print('Iterate  thru  zip  object  with  _next_()  method')
while True:
    try:
        print(z1.__next__())
    except:
        break
print('Iterate  thru  zip  object  with   for  loop')
for i in z1:
    print(i)
print('Elements  of  each  tuple  in  zip  object')
for i,j in z1:
    print(i)
print('Unpacks  zip  object  with   *  operator  :  ' , *z1)
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(z1))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z1))

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
(Empno, 25)
(Emp Name, Rama Rao) 
(Salary, 10000.0)
'''
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
	
"""
('Telangana','Hyderabad',50000000)
('Andhra  Pradesh','Amaravathi'40000000)
('Karnataka','Banglore',70000000)
('TamilNadu','Chennai',60000000)
('Maharastra','Mumbai',30000000)
"""

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
9'''

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

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)
[[0,20],[1,21],[2,22],[3,23],[4,24]]

#  How  to  print  reversed  object  in  different  ways  (Home  work)
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
[12:58 pm, 20/04/2026] Srinivas Sir SSDP: # Find  outputs (Home  work)
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

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
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

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) #error No

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
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''