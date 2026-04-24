from  random  import  *
print(random()) # random number between 0 to 1 (both not included)
print(randint(1 , 100)) # random integer between 1 to 100 (both included)
print(uniform(1 , 100)) # random float number between 1 to 100 (both not included)
print(randrange(10)) # random integer between 0 to 9
print(randrange(1 , 11)) # random integer between 1 to 10 in steps of 1
print(randrange(1 , 11 , 2)) # random integer between 0 to 10 in steps of 2
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # random element of the list
print(choice('RAJESH')) # random element of the string 'RAJESH'
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # error , set is not a valid argument because it is not indexed



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import choice
s = input('Enter a string:')

for i in range(10):
    print(choice(s))



#1
'''  
(Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from random import randint , choice

for i in range(6):
    password = ''
    for i in range(3):
        password += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        password += str(randint(0 , 9))
    print(password)



# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import choice
list = eval(input('Enter a list:'))

for i in range(10):
    print(choice(list))


# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import randint

for i in range(10):
    otp = ''
    for i in range(6):
        otp += str(randint(0 , 9))
    print(otp)


#2
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import time
from webbrowser import open
from random import choice , randint

list = ['google.com' , 'youtube.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

for i in range(len(list)):
    open(choice(list))
    time . sleep (randint(5 , 20))


#3
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
from random import randint
def rps(x):
    l = ['Rock' , 'Paper' , 'Scissors']
    c = randint(0 , 2)
    if x == c:
        print(f'Computer Chose: {l[c]}')
        print(f'User Chose: {l[x]}')
        print(f'Draw as both the Computer and User chose {l[x]}')
    elif c == 0 and x == 2:
        print(f'Computer Chose: {l[c]}')
        print(f'User Chose: {l[x]}')
        print(f'Computer wins as {l[c]} wins over {l[x]}')
    elif c == 1 and x == 0:
        print(f'Computer Chose: {l[c]}')
        print(f'User Chose: {l[x]}')
        print(f'Computer wins as {l[c]} wins over {l[x]}')
    elif c == 2 and x == 1:
        print(f'Computer Chose: {l[c]}')
        print(f'User Chose: {l[x]}')
        print(f'Computer wins as {l[c]} wins over {l[x]}')
    else:
        print(f'Computer Chose: {l[c]}')
        print(f'User Chose: {l[x]}')
        print(f'User wins as {l[x]} wins over {l[c]}')


x = int(input('What do you want to select? (0 - Rock , 1 - Paper , 2 - Scissors):'))
rps(x)

while True:
    gc = input('Do you want to continue the game? [Y / N]:')
    if gc.upper() == 'Y':
        x = int(input('What do you want to select? (0 - Rock , 1 - Paper , 2 - Scissors):'))
        rps(x)
    else:
        print('End of Game')
        break


#4
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
from random import randint

r = randint(1 , 100000)
low = 1
high = 100000
ctr = 0

while True:
    x = int(input(f'Enter any number between {low} and {high}:'))
    ctr += 1
    
    if x == r:
        print(f'{r} found in {ctr} attempts')
        break
    elif x < r:
        print('Too low! Try a higher number.')
        low = x + 1
    else:
        print('Too high! Try a lower number.')
        high = x - 1





# Find  outputs
import  os
os . system('dir') # prints all directories and sub directories of current working directory
os . system('pause') # suspends the program until user enters a key
os . system('cls') # clears screen
os . system('py  test.py') # runs test.py

'''
test.py  file  of  cwd  contains
-----------------------------------
print('Hyd')
print('Sec')
print('Cyb')
'''
'''
Hyd
Sec
Cyb
'''



#5
'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
from os import mkdir

x = input('Enter the name of the directory you want to create:')

try:
    mkdir(x)
    print(f'Created {x} Directory!')
except FileExistsError:
    print(f'Directory {x} already exists.')


#6
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
from os import makedirs
x = input('Enter the names of the directories you want to create (in the format(A/B/C)):')

try:
    makedirs(x)
    print('Directory (or) Directories Created!')
except FileExistsError:
    print(f'All the directories {x} already exists')
except FileNotFoundError:
    y = x.split('/')
    print(f'Directory{y[0]} does not exist.')