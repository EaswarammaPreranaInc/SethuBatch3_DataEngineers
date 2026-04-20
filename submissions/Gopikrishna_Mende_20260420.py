# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print(next (z1))
print("Iterate  thru  zip  object  with  next()  method")
z1 = zip(a , b)
print(next (z1))
print(next (z1))
print(next (z1))
print(next (z1))
print('Iterate  thru  zip  object  with  __next__()  method')
z1 = zip(a , b)
print(z1.__next__())
print(z1.__next__())
print(z1.__next__())
print(z1.__next__())

print('Iterate  thru  zip  object  with   for  loop')
z1 = zip(a , b)
for x, y in z1:
    print(x , '---->' , y)  

print('Elements  of  each  tuple  in  zip  object')
z1 = zip(a , b)
for x in z1:
    print(x)
print('Unpacks  zip  object  with   *  operator  :  ' , *z1)
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(z1))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z1))

# =========================================================
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z)) # ('Empno', 25) <next line> ('Emp Name', 'Rama Rao') <next line> ('Salary', 10000.0)
		time . sleep(1)
	except  StopIteration:
		break

# ========================================================
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x) # ('Telangana', 'Hyderabad', 50000000) <next line> ('Andhra Pradesh', 'Amaravathi', 40000000) <next line> ('Karnataka', 'Banglore', 70000000) <next line> ('TamilNadu',
	time . sleep(1)

# =========================================================
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  # 5 <next line> 7 <next line> 9 
	time . sleep(1)

# ===========================================================

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
disp(z3) # (10, (1, 2)) <next line> (20, (3, 4)) <next line> (30, (5, 6))
z4 = zip(a , b)
disp(z4) # (10, 1) <next line> (20, 3) <next line> (30, 5)
z5 = zip(a)
disp(z5) # (10,) <next line> (20,) <next line> (30,)
z6 = zip(b)
disp(z6) # (1,) <next line> (3,) <next line> (5,)
z7 = zip()
disp(z7) # nothing

# ========================================================  

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]

# ========================================================

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)


print('Iterate  thru  reversed  object  with   next   function')
r1 = reversed(a)
print(next(r1)) # D <next line> Y <next line> H
print(next(r1)) # Y <next line> H
print(next(r1)) # H

print('Iterate  thru  reversed  object  with   __next__   method')
r1=reversed(a)
print(r1.__next__()) # D <next line> Y <next line> H
print(r1.__next__()) # Y <next line> H
print(r1.__next__()) # H

print('Iterate  thru  reversed  object  with   for  loop')
for char in reversed(a):
    print(char) # D <next line> Y <next line> H

print('Unpack  reversed  object  : ' ,  *reversed(a)) # D Y H

print('List  of  chars  in  reverse  order  :  ' , list(reversed(a))) # ['D', 'Y', 'H']

print('Reverse  string   :   ' , ''.join(reversed(a))) # DYH    



# =========================================================

 # Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) #< reversed object at address>
print(id(b)) # Address of the object
print(*b) # D Y H
print(b[0])# TypeError: 'reversed' object is not subscriptable
print(b[1 : 3]) # TypeError: 'reversed' object is not subscriptable
print(b * 2)   # TypeError: unsupported operand type(s) for *: 'reversed' and 'int'
print(len(b))# TypeError: object of type 'reversed' has no len()

# ========================================================

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x)# True <next line> Hyd <next line> 10.8 <next line> 25
	time . sleep(1)

# ========================================================

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
lst = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(lst)
print(type(r1))
print(r1)

print('next()   function  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
print(next(r1)) # True <next line> Hyd <next line> 10.8 <next line> 25  
print(next(r1)) # Hyd <next line> 10.8 <next line> 25
print(next(r1)) # 10.8 <next line> 25

print('__next__()   method  iterates   thru  list_reverseiterator  object')
r1 = reversed(lst)
print(r1.__next__()) # True <next line> Hyd <next line> 10.8 <next line> 25
print(r1.__next__()) # Hyd <next line> 10.8 <next line> 25
print(r1.__next__()) # 10.8 <next line> 25

print('for  loop  iterates  thru  list_reverseiterator  object')
r1 = reversed(lst)
for x in r1:
    print(x) # True <next line> Hyd <next line> 10.8 <next line> 25
    time . sleep(1)

print('Unpack  list_reverseiterator  object  :  ' ,  *reversed(lst))

print('Reverse  list  :  '  ,  list(reversed(lst)))


# ========================================================= 

# #  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # TypeError: 'set' object is not reversible

# ========================================================

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
disp(r1) # 18 <next line> 15 <next line> 20 <next line> 10
r2 = reversed(a . values())
disp(r2) # 'Amar' <next line> 'Kiran' <next line> 'Sita' <next line> 'Rama'
r3 = reversed(a . items())
disp(r3) # (18, 'Amar') <next line> (15, 'Kiran') <next line> (20, 'Sita') <next line> (10, 'Rama')
r4 = reversed(a)
disp(r4) # 18 <next line> 15 <next line> 20 <next line> 10


# ========================================================

'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
a= input('Enter  a  dictionary  :  ') # {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
d = eval(a)
reversed_dict = {v: k for k, v in d.items()}
print(reversed_dict) # {25: 'Empno', 'Rama  Rao': 'Emp Name', 10000.0: 'Sal'} 


# =========================================================

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
# Write  for  loop  to  reverse  keys  of  dictionary
for key in reversed(a):
    print(key) # 18 <next line> 15 <next line> 20 <next line> 10
    time . sleep(1)

print('Values  in  reverse  order')
# Write  for  loop  to  reverse  values  of  dictionary
for value in reversed(a.values()):
    print(value) # 'Kiran' <next line> 'Rajesh' <next line> 'Sita' <next line> 'Rama rao'
    time . sleep(1)

print('Tuples  in   reverse  order')
# Write  for  loop  to  reverse   tuples   of  dictionary
for item in reversed(a.items()):
    print(item) # (18, 'Kiran') <next line> (15, 'Rajesh') <next line> (20, 'Sita') <next line> (10, 'Rama rao')
    time . sleep(1)


print('Elements  of  each   tuple  in  reverse  order')
# Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
for key, value in reversed(a.items()):
    print(key, value) # 18 'Kiran' <next line> 15 'Rajesh' <next line> 20 'Sita' <next line> 10 'Rama rao'
    time . sleep(1)
print('Keys  and  values  in   reverse   order')
# Write  for  loop  to  reverse  keys  and  corresponding  values  of  dictionary
for key, value in reversed(a.items()):
    print(value, key) # 'Kiran' 18 <next line> 'Rajesh' 15 <next line> 'Sita' 20 <next line> 'Rama rao' 10
    time . sleep(1)

# ========================================================

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
# How  to  iterate  list  with  for  loop
for x in list:
    print(x) # 10 <next line> 20 <next line> 15 <next line> 18
    time . sleep(1)
# print(next(list)) # TypeError: 'list' object is not an iterator
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)

print('Iterate   thru  list_iterator  with  next()  function')
# How  to  iterate  list_iterator  with  next()  function
print(next(list_itr1)) # 10 <next line> 20 <next line> 15 <next line> 18

print('Iterate  thru  list_iterator  with   __next__()  method')
# How  to  iterate  list_iterator  with   __next__  method
list_itr2 = iter(list)
print(list_itr2.__next__()) # 10 <next line> 20 <next line> 15 <next line> 18

print('Iterate   thru  list_iterator  with   for    loop')
# How  to  iterate  list_iterator  with  for  loop
list_itr3 = iter(list)
for x in list_itr3:
    print(x) # 10 <next line> 20 <next line> 15 <next line> 18
    time . sleep(1) 
print('Unpacks  List_iterator   :    ' ,  *iter(list)) # 10 20 15 18

# ========================================================  

# Find  outputs
a = 25
print(a) # 25
for  x   in   a:
	print(x) # TypeError: 'int' object is not iterable
print(iter(a)) # TypeError: 'int' object is not iterable
print(next(a))# TypeError: 'int' object is not an iterator