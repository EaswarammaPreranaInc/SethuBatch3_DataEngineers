
#  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
# End  of  the  function

list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1))		
disp(z1)		
z2 = zip_longest(range(7) , list)
print(type(z2))
disp(z2)
'''
<class 'zip'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
<class 'itertools.zip_longest'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, None)
(5, None)
(6, None)
'''



 #  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
''
<class 'cycle'>
10
20
30
40
10
20....'''



#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)
'''
1st repeat object
25
25
25
2nd repeat object
Hyd
Hyd
Hyd'''''''
'''




# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
1
4
9
16
25
36
49
64
81
'''



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break  #0




# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
1
1
error
'''




# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
1
2
4
8
16
32
64
128
256
512
'''



#  Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)

'''
Different  Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
Different   Permutations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'D')
('C', 'D', 'A')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'A', 'C')
('D', 'B', 'A')
('D', 'B', 'C')
('D', 'C', 'A')
('D', 'C', 'B')
'''



from  random  import  *
print(random())		#0.5
print(randint(1 , 100)) #99
print(uniform(1 , 100)) #25
print(randrange(10))	#8
print(randrange(1 , 11))#4
print(randrange(1 , 11 , 2))#4
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))	#15
print(choice('RAJESH')) #J
set  =  {10 , 20 , 30 , 40}
print(choice(set))	#error ,set object is not subscriptable




# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random
s="program"
for i in range(11):
	print(random.choice(s))



'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''






# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import random
s=[1,2,3,4,5]
for i in range(11):
	print(random.choice(s))




# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)




'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website
2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import webbrowser
import random
import time

websites=['http://google.com', 'http://rediff.com', 'http://gmail.com', 'http://amazon.com', 'http://netflix.com']

for i in websites:
	webbrowser.open(i)
	delay=random.randint(5,20)
	time.sleep(delay)





