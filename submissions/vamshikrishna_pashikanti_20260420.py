# How  to  iterate  zip  object  in  differenet  ways  (Home  work)

import   time

a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']

b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']

z1 = zip(a , b)		#empty zip is created

print(type(z1))		#<class "zip">

print(z1)		#type and address

print(next(z1)

next(z)

print(z1.__next__())

print(z1.__next__())

for item in z:

    print(item)



for state, capital in z:

    print('State:', state)

    print('Capital:', capital)

    print('---')



print(states, capitals = zip(*z)

print(states)

print(capitals)



print()









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

('Empno', 25)

<1 sec>

('Emp Name', 'Rama  Rao')

<1 sec>

('Salary', 10000.0)

<1 sec>

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

('Telangana', 'Hyderabad', 50000000)

('Andhra  Pradesh', 'Amaravathi', 40000000)

('Karnataka', 'Banglore', 70000000)

('TamilNadu', 'Chennai', 60000000)

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









#  How  to  print  reversed  object  in  different  ways  (Home  work)

import   time

a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD

r1 = reversed(a)

print(type(r1))		#<class 'reversed'>

print(r1)		#DYH

print(next(r))

next(r)

print(__next__())

__next__()

print('Iterate  thru  reversed  object  with   for  loop')

How  to  iterate  reversed  object   with  for  loop

print('Unpack  reversed  object  : ' ,  ???)

print('List  of  chars  in  reverse  order  :  ' ,  ???)

print('Reverse  string   :   ' , ???)









# Find  outputs (Home  work)

# Find  outputs (Home  work)

a = 'HYD'

b = reversed(a)

print(type(b))#<class 'reversed'>

print(b)#<reversed object at 0x7884a26cdbd0>

print(id(b))#1000

print(*b)#D Y H

print(b[0])#errpr

print(b[1 : 3])#error

print(b * 2)#error

print(len(b))#error 









 # Can  tuple  be  reversed ?   (Home  work)

import   time

a = (25 , 10.8 , 'Hyd' , True)

b = reversed(a)

print(type(b))

for  x  in   b:

	print(x)

	time . sleep(1)

'''

<class 'reversed'>

True

Hyd

10.8

25

'''









#  Can  set  be  reversed  ?  (Home  work)

a = {10, 20, 15 , 18}

r = reversed(a)

#error set is not reversible









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

10'''





'''

Tricky  program

Write  a  program  to  reverse  a  dictionary ?



Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}

What  is  the  output  ?  ---> {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}



Hint :  Both  input  and  output  are  dictionaries

'''



d = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}



items=list(d.items())



rev_items=reversed(items)



rev_dict=dict(rev_items)



print(rev_dict)



# Find outputs

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



'''

Keys in reverse order

18

15

20

10



Values in reverse order

Kiran

Rajesh

Sita

Rama rao



Tuples in reverse order

(18, 'Kiran')

(15, 'Rajesh')

(20, 'Sita')

(10, 'Rama rao')



Elements of each tuple in reverse order

18 Kiran

15 Rajesh

20 Sita

10 Rama rao



Keys and values in reverse order

18 Kiran

15 Rajesh

20 Sita

10 Rama rao

'''`







# Find  outputs

a = 25

print(a)

for  x   in   a:

	print(x)

print(iter(a))

print(next(a))

'''

25

ERROR

'''
