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


#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
	
10
20
30
40
10
20
30
40

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
	break
	
1st  repeat  object
25
25
25
2nd  repeat  object
Hyd	

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
0		

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
1
1

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

0.43347492004100374
99
40.335958181597675
7
9
7
18


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

0.7055213983960957
23
44.47787694406572
6
3
1
10
S
ERROR!


Write  a  python program  to  print  random  character  of  the  string  10  times

import random

def print_random_chars(text, times=10):
    """Print random characters from the given string."""
    for _ in range(times):
        char = random.choice(text)
        print(char)
user_string = input("Enter a string: ")
print_random_chars(user_string)


Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import random
import string

def generate_passwords(count=10, length=6):
    passwords = []
    for _ in range(count):
        password = ""
        for i in range(length):
            if i % 2 == 0:  
                password += random.choice(string.ascii_letters)
            else:         
                password += random.choice(string.digits)
        passwords.append(password)
    return passwords
for pwd in generate_passwords():
    print(pwd)

Write  a  program  to  print  random  element  of  the  list  ten  times
import random

def print_random_elements(my_list, times=10):
    """Print random elements from the list."""
    for _ in range(times):
        print(random.choice(my_list))
user_input = input("Enter elements of the list : ")
user_list = user_input.split()
print_random_elements(user_list)


Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

import webbrowser
import time
import random

def open_websites():
    websites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']
    
    for site in websites:
        webbrowser.open(f'http://{site}')
        print(f"Opened {site}")
        delay = random.randint(5, 20)
        print(f"Waiting {delay} seconds before opening next site...")
        time.sleep(delay)
open_websites()


Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Result: Draw")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Result: Computer wins (paper dominates rock)")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Result: Computer wins (scissors dominate paper)")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Result: Computer wins (rock dominates scissors)")
    else:
        print("Result: User wins")
rock_paper_scissors()


Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts

import random
def guess_number_game():
    number = random.randint(1, 100000)
    attempts = 0
    print("Guess a number between 1 and 100000")
    while True:
        attempts += 1
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
guess_number_game()


Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory

import os

def create_directory():
    dir_name = input("Enter directory name or full path: ")
    
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")
create_directory()

Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

import os

def create_directories():
    path = input("Enter directory path (e.g., a/b/c): ")
    
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directories '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating directories: {e}")
create_directories()


