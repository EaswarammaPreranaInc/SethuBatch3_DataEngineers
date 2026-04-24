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
print(type(z1))  # <class 'zip'>
disp(z1)  #  (0,10)
             (1,20)
             (2,30)
             (3,40)
z2 = zip_longest(range(7) , list)
print(type(z2))  <class 'itertools.zip_longest'>
disp(z2)
# (0,10)
  (1,20)
  (2,30)
  (3,40)
  (4,None)
  (5,None)
  (6,None)
  





#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')  # 1st  repeat  object
while   True:
	try:
		print(next(r))   #  25
                                    25
                                    25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')  # 2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)  # Hyd
                           Hyd
                           Hyd 
                           Infinite times



#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))   # <class 'itertools.cycle'>
while   True:
	print(next(c))  # 10
                          20
                          30
                          40
                          10
                          20
                          30
                          40
                          infinite times
	time . sleep(1)



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))  # 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))   
		time . sleep(1)
	except:
		break




# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))  #  0 1
		time . sleep(1)
	except:
		break



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))  # 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break



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
print('Different  Combinations')  # Different  Combinations
disp(c)  # (A , B , C),(A , B , D),(A , C , D),(B , C , D)
print('Different   Permutations')  #  Different   Permutations
p = permutations(list , 3)
disp(p) # (A , B , C),(A , C , B),(A , B , D),(A , D , B),(A , C , D),(A , D , C)
          (B , A , C),(B , C , A),(B , A , D),(B , D , A),(B , C , D),(B , D , C)
          (C , A , B),(C , B , D),(C , B , A),(C , D , B),(C , A , D),(C , D , A)
          (D , A , B),(D , B , A),(D , C , B),(D , B , C),(D , C , A),(D , A , C)



from  random  import  *
print(random())  # 0.9
print(randint(1 , 100))  # 90
print(uniform(1 , 100))  # 4.9
print(randrange(10))  # 9
print(randrange(1 , 11)) # 8
print(randrange(1 , 11 , 2))  # 10
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))   # 15
print(choice('RAJESH'))  # H
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # error



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import time
import random 
ch = input("Enter any charachter : ")
for i in range(11):
    print(random.choice(ch))
    time.sleep(1)
print()


'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
import time
import random
for i in range(10):
    pwd = ''
    for j in range(6):
        if j%2==0:
            pwd += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            pwd += str(random.randrange(10))
    print(pwd)
    time.sleep(1)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import time
import random 
lst = eval(input("Enter lst : "))
for i in range(10):
    print(random.choice(lst))
    time.sleep(1)


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import time
import random
for i in range(10):
    otp = ''
    for j in range(6):
        otp += str(random.randrange(10))
    print(otp)
    time.sleep(1)


'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''


import time
import random
import webbrowser
list = ['https://www.google.com', 'https://www.rediff.com', 
         'https://gmail.com', 'https://www.amazon.com', 
         'https://www.netflix.com'] 
for i in list:
    webbrowser.open(i)
    t=random.randrange(5, 21)
    time.sleep(t)


'''
(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''




'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''




# Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('py  test.py')



'''
test.py  file  of  cwd  contains
-----------------------------------
print('Hyd')
print('Sec')
print('Cyb')
'''




'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''



'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''



