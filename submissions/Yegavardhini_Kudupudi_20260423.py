#  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))#
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
Output:
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
Output:
1st  repeat  object
25
25
25
2nd  repeat  object
Hyd
Hyd
Hyd
Hyd
Hyd
repeats until the loop is true
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
Output:
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

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))#0
		time . sleep(1)
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))# 1 \n 1
		time . sleep(1)
	except:
		break

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
Output:
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
Output:
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
print(random())#
print(randint(1 , 100))#9
print(uniform(1 , 100))#
print(randrange(10))#5
print(randrange(1 , 11))#7
print(randrange(1 , 11 , 2))#9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))#18
print(choice('RAJESH'))#R
set  =  {10 , 20 , 30 , 40}
print(choice(set))#error as set is unordered

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

import random
s = input('Enter any string : ')
for i in range(10):
    ch = random.choice(s)
    print(ch)


'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

import random
lst = eval(input("Enter list: "))
for _ in range(10):
    print(random.choice(lst))

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random
for _ in range(10):
    otp = random.randint(100000, 999999)
    print(otp)

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

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
choices = ["Rock", "Paper", "Scissors"]
while True:
    user_input = int(input("What do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): "))
    if user_input not in [0, 1, 2]:
        print("Invalid choice")
        continue
    user = choices[user_input]
    computer = random.choice(choices)
    print("User     :", user)
    print("Computer :", computer)
    # Conditions
    if user == computer:
        print("Draw")
    elif (computer == "Paper" and user == "Rock") or \
         (computer == "Scissors" and user == "Paper") or \
         (computer == "Rock" and user == "Scissors"):
        print("Computer wins")
    else:
        print("User wins")
    # Continue option
    ch = input("Continue (y/n)? ").lower()
    if ch != 'y':
        print("End of the game")
        break

'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
low = 1
high = 100000
import random
secret = random.randint(low, high)
while True:
    print(f"Enter any number between {low} and {high}:", end=" ")
    guess = int(input())
    if guess == secret:
        print("Correct! You guessed the number ")
        break
    elif guess < secret:
        print("Too low, try again")
        low = guess + 1   # update lower bound
    else:
        print("Too high, try again")
        high = guess - 1  # update upper bound

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
import os
path = input("Enter directory path: ")
try:
    os.makedirs(path, exist_ok=True)
    print("Directory (or) directories created")
except Exception as e:
    print("Error:", e)
