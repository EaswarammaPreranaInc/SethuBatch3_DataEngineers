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
print(type(z1))#<class 'zip'>
disp(z1)#
z2 = zip_longest(range(7) , list)
print(type(z2))#<class 'zip'>
disp(z2)

# <class 'zip'>
# 0 10
# 1 20
# 2 30
# 3 40
# <class 'iterable zip_longest'>
# 0 10
# 1 20
# 2 30
# 3 40
# 4 None
# 5 None
# 6 None

#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)

# 10
# 20
# 30
# 40
# 50
# 60
# .
# .
# .
 
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
 
#  1st  repeat  object
# 25
# 25
# 25
# 2nd  repeat  object
# Hyd
# Hyd
# Hyd
# Hyd
# Hyd
# ...

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
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
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
#0

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
# 1
# 1

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
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512

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

# Different   Permutations
# ('A', 'B', 'C')
# ('A', 'B', 'D')
# ('A', 'C', 'B')
# ('A', 'C', 'D')
# ('A', 'D', 'B')
# ('A', 'D', 'C')

# ('B', 'A', 'C')
# ('B', 'A', 'D')
# ('B', 'C', 'A')
# ('B', 'C', 'D')
# ('B', 'D', 'A')
# ('B', 'D', 'C')

# ('C', 'A', 'B')
# ('C', 'A', 'D')
# ('C', 'B', 'A')
# ('C', 'B', 'D')
# ('C', 'D', 'A')
# ('C', 'D', 'B')

# ('D', 'A', 'B')
# ('D', 'A', 'C')
# ('D', 'B', 'A')
# ('D', 'B', 'C')
# ('D', 'C', 'A')
# ('D', 'C', 'B')
from  random  import  *
print(random())
print(randint(1 , 100))
print(uniform(1 , 100))
print(randrange(10))
print(randrange(1 , 11))
print(randrange(1 , 11 , 2))
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))
print(choice('RAJESH'))
set  =  {10 , 20 , 30 , 40}
print(choice(set))

error 

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
s = input('Enter a string =')
for i in range(10):
    print(choice(s))

'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
import random
import string

for i in range(10):
    password = ""
    
    for j in range(6):
        if j % 2 == 0:   # 0,2,4 → alphabets (1st,3rd,5th)
            password += random.choice(string.ascii_letters)
        else:            # 1,3,5 → digits (2nd,4th,6th)
            password += random.choice(string.digits)
    
    print(password)

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import choice
lst = [10, 20, 30, 40, 50]

for i in range(10):
    print(choice(lst))

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random

for i in range(10):
    otp = random.randint(100000, 999999)
    print(otp)

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser
import time
import random

sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

for site in sites:
    webbrowser.open('http://' + site)
    
    gap = random.randint(5, 20)   # random delay between 5 to 20 seconds
    print(f"Opened {site} → waiting {gap} seconds...")
    
    time.sleep(gap)

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

# User input
user = input("Enter rock, paper or scissors: ").lower()

# Computer choice
computer = random.choice(choices)

print("User choice     :", user)
print("Computer choice :", computer)

# Game logic
if user == computer:
    print("Result: Draw")

elif computer == 'paper' and user == 'rock':
    print("Result: Computer wins (paper beats rock)")

elif computer == 'scissors' and user == 'paper':
    print("Result: Computer wins (scissors beats paper)")

elif computer == 'rock' and user == 'scissors':
    print("Result: Computer wins (rock beats scissors)")

else:
    print("Result: User wins")
    

'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
import os

path = input("Enter directory name or full path: ")

try:
    os.makedirs(path)   # creates directory (and parent dirs if needed)
    print("Directory created successfully")
except FileExistsError:
    print("Directory already exists")
except Exception as e:
    print("Error:", e)

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os

path = input("Enter directory path (e.g., a/b/c): ")

try:
    os.makedirs(path)
    print("Directories created successfully")
except FileExistsError:
    print("Directories already exist")
except Exception as e:
    print("Error:", e)   



