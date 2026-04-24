1.
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
z2 = zip_longest(range(7) , list , fillvalue="Not Available" )
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



2.
# #  Find  outputs  (Home  work)
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
2nd  repeat  object
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
repeatedly  until  the  program  is  stopped
'''


3.
#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
'''
<class 'itertools.cycle'>
10
20
30
40
10
20
30
40
10
20
30
40
10
20
30
40
repeatedly cycle  until  the  program  is  stopped
'''


4.
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
0
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



5.
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
	
'''
0
'''


6.
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
'''


7.
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


8.
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



9.
# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random

s = input('Enter any string: ')

for i in range(10):
    ch = random.choice(s)
    print(ch)


10.
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

import random
import string

def generate_password():
    pwd = ""
    for i in range(6):
        if i % 2 == 0:   # 0,2,4 → alphabets
            pwd += random.choice(string.ascii_letters)
        else:            # 1,3,5 → digits
            pwd += random.choice(string.digits)
    return pwd

for _ in range(10):
    print(generate_password())



11.
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import random

lst = [10, 20, 30, 40, 50]

for _ in range(10):
    print(random.choice(lst))



12.
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random

for _ in range(10):
    otp = random.randint(100000, 999999)
    print(otp)



13.
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

sites = [
    'https://www.google.com',
    'https://www.rediff.com',
    'https://www.gmail.com',
    'https://www.amazon.com',
    'https://www.netflix.com'
]

for site in sites:
    print(f"Opening: {site}")
    webbrowser.open(site)

    gap = random.randint(5, 20)
    print(f"Waiting for {gap} seconds...\n")
    time.sleep(gap)



14.
'''''
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

choices = ["rock", "paper", "scissors"]

user = input("Enter rock / paper / scissors: ").lower()
computer = random.choice(choices)

print(f"Computer selected: {computer}")

if user not in choices:
    print("Invalid input! Please enter rock, paper, or scissors.")

elif user == computer:
    print("Result: Draw")

elif computer == "paper" and user == "rock":
    print("Result: Computer wins (Paper beats Rock)")

elif computer == "scissors" and user == "paper":
    print("Result: Computer wins (Scissors beats Paper)")

elif computer == "rock" and user == "scissors":
    print("Result: Computer wins (Rock beats Scissors)")

else:
    print("Result: User wins 🎉")



15.
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''

import random

secret_number = random.randint(1, 100000)
attempts = 0

print("Guess the number between 1 and 100000")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("\n🎉 Correct Guess!")
        print(f"The number is: {secret_number}")
        print(f"Number of attempts: {attempts}")
        break




16.
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



17.
''''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''

import os

path = input("Enter directory name or full path: ").strip()

try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory created successfully at: {os.path.abspath(path)}")
except Exception as e:
    print("Error creating directory:", e)


18.
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''

import os

path = input("Enter group of directories (e.g., a/b/c): ").strip()

try:
    os.makedirs(path, exist_ok=True)
    print("Directories created successfully!")
    print("Full path:", os.path.abspath(path))
except Exception as e:
    print("Error:", e)