#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')#1st repeat object
while   True:
	try:
		print(next(r))# 25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')#2nd repeat object
r  =  repeat('Hyd')
while   True:
	print(next(r))#hyd hyd hyd....
	time . sleep(1)
 #  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))#<class 'itertools.cycle'>
while   True:
	print(next(c))# 10 20 30 40 10 20 30 40......
	time . sleep(1) # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
[12:34 pm, 23/04/2026] SRINIVAS Sir Maths: # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))#(0,2)
		time . sleep(1)
	except:
		break
 # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))#(0,0)(1,1)
		time . sleep(1)
	except:
		break
[12:34 pm, 23/04/2026] SRINIVAS Sir Maths: # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))#(2,0),(2,1),(2,2)....,(2,9)
		time . sleep(1)
	except:
		break
[12:40 pm, 23/04/2026] SRINIVAS Sir Maths: #  Find  outputs (Home  work)
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
('A','B','C')
('A','B','D')
('A','C','D')
('B','C','D')
print('Different  Combinations')
disp(c)
print('Different   Permutations')
('A','B','C')
('A','C','B')
('B','A','C')
...
p = permutations(list , 3)
disp(p)
 from  random  import  *
print(random())#0.21
print(randint(1 , 100))#57
print(uniform(1 , 100))#45.90
print(randrange(10))# 0 to 9
print(randrange(1 , 11))#1 to 10
print(randrange(1 , 11 , 2))#1,3,5,7,9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))
print(choice('RAJESH'))
set  =  {10 , 20 , 30 , 40}#error
print(choice(set))
 # Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
(Home  work)

from random import choice

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(10):
    print(choice(s))

Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from random import choice
import string

for i in range(10):
    pwd = ""
    pwd += choice(string.ascii_letters)  # 1st
    pwd += choice(string.digits)         # 2nd
    pwd += choice(string.ascii_letters)  # 3rd
    pwd += choice(string.digits)         # 4th
    pwd += choice(string.ascii_letters)  # 5th
    pwd += choice(string.digits)         # 6th
    print(pwd)

 # Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import choice

lst = [10, 20, 30, 40, 50]

for i in range(10):
    print(choice(lst))
 # Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import randint

for i in range(10):
    otp = randint(100000, 999999)
    print(otp)

Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

import webbrowser
import time
from random import randint

sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

for site in sites:
    webbrowser.open("http://" + site)
    time.sleep(randint(5, 20))

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


from random import choice

options = ['rock', 'paper', 'scissors']

user = input("Enter rock/paper/scissors: ").lower()
comp = choice(options)

print("Computer:", comp)

if user == comp:
    print("Draw")
elif (comp == 'paper' and user == 'rock') or \
     (comp == 'scissors' and user == 'paper') or \
     (comp == 'rock' and user == 'scissors'):
    print("Computer wins")
else:
    print("User wins")
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
from random import randint

num = randint(1, 100000)
count = 0

while True:
    guess = int(input("Enter number: "))
    count += 1

    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("Correct number:", num)
        print("Attempts:", count)
        break

: import  os
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
import os

name = input("Enter directory name or path: ")
os.mkdir(name)

print("Directory created")
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
import os

path = input("Enter path (like a/b/c): ")
os.makedirs(path)

print("Directories created")