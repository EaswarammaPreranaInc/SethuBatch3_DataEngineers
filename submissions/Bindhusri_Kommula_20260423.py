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
z1  =  zip(range(7) , list) # empty object
print(type(z1)) # <class 'zip'>
disp(z1) # (0,10) (1,20) (2,30) (3,40) 
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'itertools.zip_longest'>
disp(z2) # (0,10) (1,20) (2,30) (3,40) (4,None) (5,None) (6,None)


#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list) 
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c)) # 10 20 30 40 10 20 30 40...
	time . sleep(1)


#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object') # 1st  repeat  object
while   True:
	try:
		print(next(r)) # 25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object') # 2nd  repeat  object
r  =  repeat('Hyd') 
while   True:
	print(next(r)) # Hyd Hyd Hyd Hyd...
	time . sleep(1)


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m)) # 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m)) # 0
		time . sleep(1)
	except:
		break


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m)) # 1 1
		time . sleep(1)
	except:
		break


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10)) 
while   True:
	try:
		print(next(m)) #  1 2 4 8 16 32 64 128 256 512
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
print('Different  Combinations') # Different  Combinations
disp(c) # ['A','B','C'] ['B','C','D']
print('Different   Permutations') # Different   Permutations
p = permutations(list , 3)
disp(p) # ('A', 'B', 'C')
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



from  random  import  *
print(random()) # 0.5
print(randint(1 , 100)) # 50
print(uniform(1 , 100)) # 50.0
print(randrange(10)) # 6
print(randrange(1 , 11)) # 5
print(randrange(1 , 11 , 2)) # 3
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # 15
print(choice('RAJESH')) # J
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # error


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

from random import choice
def count(s):
    print(choice(s))
    
s=input()
for i in range(10):
    count(s)


'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from random import choice
for i in range(10):
        res=""
        for j in range(6):
                
                if j%2==0:
                        res=res+choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                else:
                        res=res+(choice('123456789'))
        print(res)


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

from random import choice
def count(s):
    print(choice(s))
    

a=list(eval(input()))
for i in range(10):
    count(a)


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

from random import choice
for i in range(10):
        res=""
        for j in range(6):
                res=res+(choice('123456789'))
        print(res)


'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import webbrowser ,time,random

list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(len(list)):
        webbrowser.open(list[i])
        time.sleep(random.randint(5,20))


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

import random

choices = ['rock', 'paper', 'scissors']

s = int(input('What do you want to select (0-Rock, 1-Paper, 2-Scissors): '))
c = random.randint(0, 2)

user = choices[s]
computer = choices[c]

print('User      :', user)
print('Computer  :', computer)

if user == computer:
    print('Draw')
elif (computer == 'paper' and user == 'rock'):
    print('Computer wins')
elif (computer == 'scissors' and user == 'paper'):
    print('Computer wins')
elif (computer == 'rock' and user == 'scissors'):
    print('Computer wins')
else:
    print('User wins')



'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''

import random 
c=random.randint(1,100000)
count=0
while True:
        n=int(input('enter any number between 1 and 100000: '))
        count+=1
        if c==n:
            print('guessed in n numbers')
            break
        elif n<c:
            print('too low')
        else:
            print('too high')


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

import os

path = input("Enter directory name or path: ")
try:
    os.mkdir(path)
    print(f"Directory {path} created")
except FileExistsError:
    print(f"Directory {path} already exists")


'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os

path = input("Enter directory name or path: ")
try:
    os.makedirs(path)
    print("Directory or directories created")
except FileExistsError:
    print("Directory or directories  already exists")

