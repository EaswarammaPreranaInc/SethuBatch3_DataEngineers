# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
#How  to   iterate  thru  zip  object  with  next()  function
print(next(z1))
print(next(z1))
print(next(z1))
print(next(z1))
print('Iterate  thru  zip  object  with  __next__()  method')
z_iter = iter(z1)   # get iterator
while True:
    try:
        print(z_iter.__next__())   # or next(z_iter)
        time.sleep(1)
    except StopIteration:
        break
#How  to   iterate  thru  zip  object  with  __next__()  method
print('Iterate  thru  zip  object  with   for  loop')
for i in z1:
  print(i)
#How  to   iterate  thru  zip  object  with  for  loop
print('Elements  of  each  tuple  in  zip  object')
for i in z1:
  for j in i:
    print(j)
#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , *(z1))
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(z1))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z1))
#################################################################################################
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
z = zip(a , b)
while   True:
	try:
		print(next(z))#('Empno', 25)
                  #('Emp Name', 'Rama  Rao')
                  #('Salary', 10000.0)
		time . sleep(1)
	except  StopIteration:
		break

#################################################################################################
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
---output---
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
#################################################################################################
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) #5 7 9 
	time . sleep(1)
#################################################################################################
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
---output---
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)
#################################################################################################
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))#[[0,1,2,3,4],[20,21,22,23,24]]
a = [ [x , y]  for  x , y   in   z]  
print(a)#(0,20) (1,21) (2,22) (3,23) (4,24)
#################################################################################################
import time

a = input('Enter any string : ')   # Example: HYD

r1 = reversed(a)

print(type(r1))
print(r1)

print('Iterate thru reversed object with next function')
   # first element

# Iterate remaining using next()
print('Iterate thru reversed object with next() function')
try:
    while True:
        print(next(r1))
        time.sleep(1)
except StopIteration:
    pass

# Create again (because iterator is exhausted)
r2 = reversed(a)

print('Iterate thru reversed object with __next__ method')
try:
    while True:
        print(r2.__next__())
        time.sleep(1)
except StopIteration:
    pass

# Create again
r3 = reversed(a)

print('Iterate thru reversed object with for loop')
for ch in r3:
    print(ch)
    time.sleep(1)

# Create again
r4 = reversed(a)

# Unpacking
print('Unpack reversed object : ', *r4)

# Create again
r5 = reversed(a)

# List conversion
print('List of chars in reverse order : ', list(r5))

# Reverse string
print('Reverse string : ', ''.join(reversed(a)))
#################################################################################################
# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)#'D' 'Y' 'H'
print(type(b))#<class 'reversed'>
print(b)#'<reversed object at 0x000001BCCC4013F0>
print(id(b))#id of b
print(*b)#D Y H
print(b[0])#error
print(b[1 : 3])#error
print(b * 2)#error
print(len(b))#error
#################################################################################################
# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
#################################################################################################
import time

lst = [25, 10.8, 'Hyd', True]

r1 = reversed(lst)
print(type(r1))
print(r1)

print('next() function iterates thru list_reverseiterator object')
try:
    while True:
        print(next(r1))
        time.sleep(1)
except StopIteration:
    pass


# recreate iterator
r1 = reversed(lst)

print('__next__() method iterates thru list_reverseiterator object')
try:
    while True:
        print(r1.__next__())
        time.sleep(1)
except StopIteration:
    pass


# recreate iterator
r1 = reversed(lst)

print('for loop iterates thru list_reverseiterator object')
for i in r1:
    print(i)


# recreate iterator
r1 = reversed(lst)

print('Unpack list_reverseiterator object : ', *list(r1))


# recreate iterator
r1 = reversed(lst)

print('Reverse list : ', list(r1))
#################################################################################################
#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a)
#################################################################################################
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
disp(r1)#18 15  20  10
r2 = reversed(a . values())
disp(r2)#'Amar' 'Kiran' 'Sita'  'Rama'
r3 = reversed(a . items())
disp(r3)#(18, 'Amar') (15, 'Kiran') (20, 'Sita')  (10, 'Rama')
r4 = reversed(a)
disp(r4)#18 15  20  10
#################################################################################################
'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint :  Both  input  and  output  are  dictionaries
'''
a={'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
b=reversed(a.items())
c={}
for i,j in b:
  c[i]=j
print(c)
#################################################################################################
import time

a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}

print('Keys in reverse order')
for i in reversed(list(a.keys())):
    print(i)


print('Values in reverse order')
for i in reversed(list(a.values())):
    print(i)


print('Tuples in reverse order')
for i in reversed(list(a.items())):
    print(i)


print('Elements of each tuple in reverse order')
for k, v in reversed(list(a.items())):
    print(v, k)


print('Keys and values in reverse order')
for k in reversed(list(a)):
    print(k, a[k])
##########################################################################################
import time

lst = [10, 20, 15, 18]

print('Iterate list with for loop')
for i in lst:
    print(i)
    time.sleep(1)


# Create iterator
list_itr1 = iter(lst)

print(type(list_itr1))
print(list_itr1)


print('Iterate thru list_iterator with next() function')
try:
    while True:
        print(next(list_itr1))
        time.sleep(1)
except StopIteration:
    pass


# recreate iterator
list_itr1 = iter(lst)

print('Iterate thru list_iterator with __next__() method')
try:
    while True:
        print(list_itr1.__next__())
        time.sleep(1)
except StopIteration:
    pass


# recreate iterator
list_itr1 = iter(lst)

print('Iterate thru list_iterator with for loop')
for i in list_itr1:
    print(i)
    time.sleep(1)


# unpack
print('Unpacks List_iterator : ', *lst)
##########################################################################################
# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
##########################################################################################