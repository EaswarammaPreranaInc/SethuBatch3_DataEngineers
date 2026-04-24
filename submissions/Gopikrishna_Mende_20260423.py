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
print(type(z1)) # <class 'zip'>
disp(z1) # (0, 10) (1, 20) (2, 30) (3, 40)
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'zip_longest'>
disp(z2) # (0, 10) (1, 20) (2, 30) (3, 40) (4, None) (5, None) (6, None)

# ================================================================

#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c)) # 10 20 30 40 10 20 30 40 .....
	time . sleep(1)

# ================================================================

#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object') #1st  repeat  object
while   True:
	try:
		print(next(r)) # 25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object') #2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r)) # Hyd Hyd Hyd Hyd .....
	time . sleep(1)

# ===============================================================

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

# ==============================================================

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

# ==============================================================

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

# ==============================================================

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

# ==============================================================

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
disp(c) # ('A', 'B', 'C') ('A', 'B', 'D') ('A', 'C', 'D') ('B', 'C', 'D')
print('Different   Permutations') # Different   Permutations
p = permutations(list , 3)
disp(p) # ('A', 'B', 'C') ('A', 'B', 'D') ('A', 'C', 'B') ('A', 'C', 'D') ('A', 'D', 'B') ('A', 'D', 'C') ('B', 'A', 'C') ('B', 'A', 'D') ('B', 'C', 'A') ('B', 'C', 'D') ('B', 'D', 'A') ('B', 'D', 'C') ('C', 'A', 'B') ('C', 'A', 'D') ('C', 'B', 'A') ('C', 'B', 'D') ('C', 'D', 'A') ('C', 'D', 'B') ('D', 'A', 'B') ('D', 'A', 'C') ('D', 'B', 'A') ('D', 'B', 'C') ('D', 'C', 'A') ('D', 'C', 'B')

# ==============================================================

from  random  import  *
print(random()) # 0.8444218515250481
print(randint(1 , 100)) # 18
print(uniform(1 , 100)) # 63.942679845788376
print(randrange(10)) # 0    
print(randrange(1 , 11)) # 1
print(randrange(1 , 11 , 2)) # 1
list = [10 , 20 , 15 , 12 , 18] 
print(choice(list)) # 12
print(choice('RAJESH')) # R
set  =  {10 , 20 , 30 , 40}
print(choice(set)) #  ERRO

# ==============================================================

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from  random  import  choice
from secrets import choice
a=input('Enter  a  string : ') # HYDERABAD
for  i  in  range(10):
    print(choice(a)) #  D A E R A B H D A A

# ==============================================================

'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from  random  import  choice
from  string  import  ascii_letters , digits
for  i  in  range(10):
    password = choice(ascii_letters) + choice(digits) + choice(ascii_letters) + choice(digits) + choice(ascii_letters) + choice(digits)
    print(password) # a7C8e3  D2a5B9  E6f1G4  b9H2c7  F3d8A1  g4J6h0  K1e9L5  m0N3i2  O7j4M8  p5Q0k6

# ==============================================================

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from  random  import  choice, random
list = eval(input('Enter  a  list : ')) # [10 , 20 , 30 , 40]
for  i  in  range(10):
    print(choice(list)) # 30 20 40 10 20 30 30 10 40 20

# ==============================================================
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from  random  import  randint
for  i  in  range(10):
    otp = randint(100000 , 999999)
    print(otp) #  548913  123456  987654  654321  111111  222222  333333  444444  555555  666666  

# ==============================================================

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import  time
import  webbrowser
from  random  import  choice , randint
list = ['http://google.com' , 'http://rediff.com' , 'http://gmail.com' , 'http://amazon.com' , 'http://netflix.com']
for  i  in  range(10):
    webbrowser.open(choice(list))
    time . sleep(randint(5 , 20))

# ==============================================================

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

rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

while True:
    user = input("Enter (rock/paper/scissors): ").lower()

    if user not in rules:
        print("Invalid input!")
        continue

    computer = random.choice(list(rules.keys()))

    print("User     :", user)
    print("Computer :", computer)

    if user == computer:
        print("Draw")

    elif rules[user] == computer:
        print("User wins")

    else:
        print("Computer wins")

    if input("Continue (y/n)? ").lower() != 'y':
        break

    # ==============================================================

'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''




import random

number = random.randint(1, 100000)

low = 1
high = 100000
attempts = 0

while True:
    guess = int(input(f"Enter any number between {low} and {high} : "))
    attempts += 1

    if guess < number:
        print("Too low , try again")
        low = guess + 1

    elif guess > number:
        print("Too high , try again")
        high = guess - 1

    else:
        print(f"\nCorrect! The number is {number}")
        print(f"Number of attempts: {attempts}")
        break

# ==============================================================

# Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('py  test.py') # Hyd <nextline> Sec <nextline> Cyb



'''
test.py  file  of  cwd  contains
-----------------------------------
print('Hyd')
print('Sec')
print('Cyb')
'''
# =================================================================	

'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
# Code :
import os
s = input('Enter directory name (or) path : ')
try :
    os.mkdir(s)
    print(f'Directory {s} created ')
except FileExistsError:
	print(f'Directory {s} already exists')
except FileNotFoundError:
	print('Directory does not exist')

''' Output:
Enter directory name (or) path : Sec
Directory Sec created 

Enter directory name (or) path : Sec
Directory Sec already exists

Enter directory name (or) path : \sssdc\sairam
Directory \sssdc\sairam created 

Enter directory name (or) path : \pak\hyd
Directory does not exist
'''
# ==============================================================

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
# Code :
import os
s = input('Enter directory path : ')
try :
    os.makedirs(s)
    print(f'Directory (or) directories created ')
except FileExistsError:
	print(f'Directory (or) directories already exists ')

''' Output:
Enter directory path : \a\b\c
Directory (or) directories created 

Enter directory path : \a\b\c
Directory (or) directories already exists 

Enter directory path : \ssdc\x\y
Directory (or) directories created

'''

