#How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import time
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Tamilnadu']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai']
z1 = zip(a, b)      
print(type(z1))
print(z1)  
print('Iterate thru zip object with next() function')
print(next(z1))
print('Iterate thru zip object with __next__() method')
print(z1.__next__())
print('Iterate thru zip object with for loop')
for item in z1:
    print(item)
print('Elements of each tuple in zip object')
for state, city in zip(a, b):
    print(f'State: {state}, City: {city}')
print('Unpacks zip object with * operator : ', list(zip(*z1)))
print() 
print('zip object in the form of list : ', list(zip(a, b)))
print()
print('zip object in the form of dictionary : ', dict(zip(a, b)))

#Find  outputs  (Home  work)
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
Output:
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
'''

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  
	time . sleep(1)

'''
Output:
5
7
9
'''
# Find outputs  (Home  work)
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
Output:
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
'''
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]  
print(a)

'''
Output:
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]] '''


#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
print(next(r1))
print('Iterate  thru  reversed  object  with   __next__   method')
print(r1.__next__())
print('Iterate  thru  reversed  object  with   for  loop')
for char in r1:
    print(char)
print('Unpack  reversed  object  : ' , list(reversed(a)))
print('List  of  chars  in  reverse  order  :  ' , list(reversed(a)))
print('Reverse  string   :   ' , ''.join(reversed(a)))

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
#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) # Error 

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
Output:
18
15
20
10
Amar
Kiran
Sita
Rama
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
a = {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
reversed_dict = dict(reversed(list(a.items())))
print(reversed_dict)

# Find outputs
import time
a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print('Keys in reverse order')  
for key in reversed(a.keys()):
    print(key)
    time.sleep(0.5)
print('Values in reverse order')
for value in reversed(a.values()):
    print(value)
    time.sleep(0.5)
print('Tuples in reverse order')
for item in reversed(a.items()):
    print(item)
    time.sleep(0.5)
print('Elements of each tuple in reverse order')
for key, value in reversed(a.items()):
    print(f'Key: {key}, Value: {value}')
    time.sleep(0.5) 
print('Keys and values in reverse order')
for key, value in reversed(list(a.items())):
    print(f'Key: {key}, Value: {value}')
    time.sleep(0.5)
	

# How  to  iterate   list_iterator  in  different  ways
import time
list = [10, 20, 15, 18]
print('Iterate list with for loop')
for item in list:   
    print(item)
    time.sleep(0.5) 
list_itr1 = iter(list)
print(type(list_itr1))  
print(list_itr1)
print('Iterate thru list_iterator with next() function')
print(next(list_itr1))
print('Iterate thru list_iterator with __next__() method')
print(list_itr1.__next__())
print('Iterate thru list_iterator with for loop')
for item in list_itr1:
    print(item)
    time.sleep(0.5)
print('Unpacks List_iterator : ', list(list_itr1))

# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
'''
Output:
25
Error'''