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
#-----------------------------------------------------------------------------
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
1st  repeat  object
25
25
25
2nd  repeat  object
Hyd 
infinte loop - while condition is always true
'''
#=====================================================================================================
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
infinity loop - while condition is always true and cycle prints the loop continously
'''


#====================================================================================================
	
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
#============================================================================================================	
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3)) # it stops due to the range(2,3) -> having only single digit
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
0
'''

#======================================================

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


#========================================================

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
#=====================================================================
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
#========================================================================================================
from  random  import  *
print(random()) # #returns random number between 0 to 1(excluding 0 and 1)
print(randint(1 , 100)) # #random integer between 1 and 100(incuding 1 and 100)
print(uniform(1 , 100)) # #float number between 1 and 100(excluding 1 and 100)
print(randrange(10)) # 	returns random integer number between 0 and 9 (including 0 and 9)
print(randrange(1 , 11)) #returns random integer between 1 and 10(both inclusive) in steps of 1
print(randrange(1 , 11 , 2)) #returns a random integer number between 1 and 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # #returns random element of list sequence
print(choice('RAJESH')) #returns random element of string sequence
set  =  {10 , 20 , 30 , 40} 
print(choice(set)) # #error- Set itself is unordered 


#===============================================================================
# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import  random
from  itertools  import  repeat
a=input("Enter the input:")
for i in range(10):
    print(random.choice(a)) 



#======================================================================================
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

import random
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
for j in range(10):
    c =""
    for i in range(6):
        if i%2 == 0:
            c += random.choice(letter)
        else:
            c += str(random.choice(digit))

    print(c)
#=================================================================================================
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
list1 = eval(input("Enter the list: "))
for i in range(10):
    print(random.choice(list1))


#==============================================================================

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for i in range(10):
    print(random.randint(100000,999999))


#============================================================================
'''

Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''


#=============================================================================================
import webbrowser
import time 
import random
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in list:
    webbrowser.open(i)
    time.sleep(random.randint(5,20))

'''


#========================================================================================
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
def game():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    if user_input == computer_choice:
        print("It's a draw!")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'): 
        print("You win!")
    else:
        print("Computer wins!")
game()




#==========================================================================================
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
import random

def guess_number():
    low = 1
    high = 100000
    number_to_guess = random.randint(low, high)
    attempts = 0

    while True:
        try:
            print(f"Enter any number between {low} and {high}:", end=" ")
            user_input = int(input())
            attempts += 1

            if user_input < number_to_guess:
                print("Too low, try again")
                low = user_input + 1   # update lower bound

            elif user_input > number_to_guess:
                print("Too high, try again")
                high = user_input - 1  # update upper bound

            else:
                print(f"\nCorrect! The number is {number_to_guess}")
                print(f"Total attempts: {attempts}")
                break

        except ValueError:
            print("Please enter a valid integer.")

if _name_ == "_main_":
    guess_number()

# Find  outputs
import  os
os . system('dir') # it runs dir of dos 
os . system('pause') # it runs pause of dos
os . system('cls') # it runs cls of dos
os . system('py  test.py') # it runs test.py of python

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

def create_directories(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Directories created successfully: {directory_path}")
    except Exception as e:
        print(f"Error occurred while creating directories: {e}")

if _name_ == "_main_":
    path = input("Enter the path for the group of directories: ")
    create_directories(path)

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os

def create_directories(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Directories created successfully: {directory_path}")
    except Exception as e:
        print(f"Error occurred while creating directories: {e}")

if _name_ == "_main_":
    path = input("Enter the path for the group of directories: ")
    create_directories(path)