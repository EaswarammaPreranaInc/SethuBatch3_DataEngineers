1) Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
#import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

for _ in range(10):
    password = ""
    for i in range(6):
        if i % 2 == 0:
            password += random.choice(letters)
        else:
            password += random.choice(digits)
    print(password)

2) Write  a  program  to  print  random  element  of  the  list  ten  times   
#import random

lst = eval(input("Enter a List: "))

for _ in range(10):
    print(random.choice(lst))

3) Write  a  program  to  generate  ten  six-digit  OTP's 
#import random

for _ in range(10):
    otp = random.randint(100000, 999999)
    print(otp)

4) Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
#import webbrowser
import time
import random

lst = ['https://google.com', 'https://rediff.com', 'https://gmail.com', 'https://amazon.com', 'https://netflix.com']

for site in lst:
    webbrowser.open(site)
    t = random.randint(5, 20)
    time.sleep(t)

5) Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''
#import random

while True:
    print("\nWhat do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): ", end="")
    user = int(input())

    a = ["Rock", "Paper", "Scissors"]
    computer = random.randint(0, 2)

    print("User     :", a[user])
    print("Computer :", a[computer])

    if user == computer:
        print("Draw")

    elif (computer == 1 and user == 0):
        print("Computer wins because Paper dominates Rock")

    elif (computer == 2 and user == 1):
        print("Computer wins because Scissors dominates Paper")

    elif (computer == 0 and user == 2):
        print("Computer wins because Rock dominates Scissors")

    else:
        print("User wins")

    ch = input("Continue (y/n)? ")
    if ch.lower() != 'y':
        print("End of the game")
        break


6) Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
#import random

low = 1
high = 100000
num = random.randint(low, high)
count = 0

while True:
    print(f"Enter any number between {low} and {high} : ", end="")
    guess = int(input())
    count += 1

    if guess == num:
        print(f"Guessed {num} in {count} attempts")
        break
    elif guess < num:
        print("Too low , try again")
        low = guess + 1
    else:
        print("Too high , try again")
        high = guess - 1

7) outputs
import  os
os . system('dir')#path of current working directory
os . system('pause')#pause temporarily until any key is pressed
os . system('cls')#system clear the screen
os . system('py  test.py')# Hyd <nextline> Sec <nextline> Cyb


'''
test.py  file  of  cwd  contains
-----------------------------------
print('Hyd')
print('Sec')
print('Cyb')
'''

8) Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
#import os
s = input('Enter directory name (or) path : ')
try :
    os.mkdir(s)
    print(f'Directory {s} created ')
except FileExistsError:
	print(f'Directory {s} already exists')
except FileNotFoundError:
	print('Directory does not exist')

9) Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
#import os
s = input('Enter directory path : ')
try :
    os.makedirs(s)
    print(f'Directory (or) directories created ')
except FileExistsError:
	print(f'Directory (or) directories already exists ')

10) Outputs
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
disp(z1) # # (0 , 10) <nextline> (1 , 20) <nextline> (2 , 30) <nextline> (3 , 40)
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'itertools.zip_longest'>
disp(z2) # (0 , 10) <nextline> (1 , 20) <nextline> (2 , 30) <nextline> (3 , 40) <nextline> (4 , None) <nextline> (5 , None) <nextline> (6 , None) 

11) Outputs
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object') # 1st  repeat  object
while   True:
	try:
		print(next(r)) # 25 <nextline> 25 <nextline> 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object') # 2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r)) # Infinite times Hyd is printed which results in infinite loop
	time . sleep(1)

12) Outputs
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c)) # 10 <nextline> 20 <nextline> 30 <nextline> 40 this is printed infinite times which results in infinite loop
	time . sleep(1)

13) Outputs
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))# 0 <nextline> 1 <nextline> 4 <nextline> 9 <nextline> 16 <nextline> 25 <nextline> 36 <nextline> 49 <nextline> 64 <nextline> 81  
		time . sleep(1)
	except:
		break
14) Outputs
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))#0
		time . sleep(1)
	except:
		break
15) Outputs
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))# 1 <nextline> 1
		time . sleep(1)
	except:
		break

16) Outputs
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))#1 <nextline> 2 <nextline> 4 <nextline> 8 <nextline> 16 <nextline>32 <nextline> 64 <nextline> 128 <nextline> 512 
		time . sleep(1)
	except:
		break

17) Outputs
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
print('Different  Combinations')#Different  Combinations
disp(c)#('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
print('Different   Permutations')#Different   Permutations
p = permutations(list , 3)
disp(p)#('A', 'B', 'C')
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

18) from  random  import  *
print(random()) # Any float value between 0 and 1 excluding them
print(randint(1 , 100)) # Any int value between 1 and 100 including them
print(uniform(1 , 100)) # Any float value between 1 and 100 including them
print(randrange(10)) # Any int value between 0 and 9
print(randrange(1 , 11)) # Any int value between 1 and 10 
print(randrange(1 , 11 , 2)) # Any int value between 1 and 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # Any element from the list
print(choice('RAJESH')) # Any character from the word 'RAJESH'
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # Error set cannot be passed as a argument to choice() function

19) Write  a  program  to  print  random  character  of  the  string  10  times
#from random import *
s = input('Enter any string : ')
for i in range(10):
    print(choice(s))
