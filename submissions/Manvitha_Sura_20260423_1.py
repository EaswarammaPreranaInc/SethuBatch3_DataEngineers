from  random  import  *
print(random())  #random float num between 0 and 1
print(randint(1 , 100))  #random integer between 1 and 100
print(uniform(1 , 100))  #random float value between 1 and 100
print(randrange(10)) #random integer between 0 and 9
print(randrange(1 , 11)) #random integer between 1 and 10
print(randrange(1 , 11 , 2)) #random integer between 1 and 10 in steps of 2 i. 2 1,3,5,7,9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))  #random number from list
print(choice('RAJESH'))  #random character from string
set  =  {10 , 20 , 30 , 40}
print(choice(set))  #error-since it is not indexed




# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
a=input('Enter any string : ')
for x in range(10):
    print(random.choice(a))



'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

from random import choice
a=[]
for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    a.append(x)
b=[1,2,3,4,5,6,7,8,9]
for x in range(10):
    print(f'{choice(a)}{choice(b)}{choice(a)}{choice(b)}{choice(a)}{choice(b)}')


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

from random import choice
a=eval(input('enter a list: '))
for i in range(10):
    print(choice(a))




# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

from random import choice
b=[1,2,3,4,5,6,7,8,9]
for i in range(10):
    print(f'{choice(b)}{choice(b)}{choice(b)}{choice(b)}{choice(b)}{choice(b)}')


'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

import time,webbrowser
from random import choice,uniform
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(5):
    webbrowser.open(choice(list))
    time.sleep(uniform(5,20))




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

from random import choice
while True:
    a=int(input('What do you want to select(0-rock,1-paper,2-scissors): '))
    if a==0:
        user='rock'
    elif a==1:
        user='paper'
    elif a==2:
        user='scissors'
    print('User :',user)
    op=['rock','paper','scissors']
    comp=choice(op)
    print('Computer :',comp)
    if user==comp:
        print('Draw')
        con=input('Continue(y/n) ? ')
        if con=='y':
            continue
        if con=='n':
            print('End of the game')
            break
    elif comp=='paper' and user=='rock':
        print('Computer wins')
        con=input('Continue(y/n) ? ')
        if con=='y':
            continue
        if con=='n':
            print('End of the game')
            break
    elif comp=='scissors' and user=='paper':
        print('Computer wins')
        con=input('Continue(y/n) ? ')
        if con=='y':
            continue
        if con=='n':
            print('End of the game')
            break
    elif comp=='rock' and user=='scissors':
        print('Computer wins')
        con=input('Continue(y/n) ? ')
        if con=='y':
            continue
        if con=='n':
            print('End of the game')
            break
    else:
        print('User wins')
        con=input('Continue(y/n) ? ')
        if con=='y':
            continue
        if con=='n':
            print('End of the game')
            break





'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
import random
a=int(input('Enter any number between 1 and 10000 '))
b=random.randrange(1,10001)
c=0
e=1
d=10000
while True:
    c+=1
    if a==b:
        print(f'Guessed {b} in {c} times')
        break
    elif a>b:
        print('Too high !try again')
        d=a-1
        a=int(input(f'Enter any number between {e} and {d} '))
        continue
    elif a<b:
        print('Too low !try again')
        e=a+1
        a=int(input(f'Enter any number between {e} and {d}' ))
        continue


# Find  outputs
import  os
os . system('dir')  #prints sub directories of cwd
os . system('pause')  #stops execution until user strikes a key
os . system('cls') #clears the screen
os . system('py  test.py')  

'''runs test.py  i.e Hyd
                     Sec
                     Cyb'''


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
try: 
	a=os.mkdir(input('Enter directory name or path'))
	print(f'Directory {a} created')
except FileExistsError:
	print(f'Directory {a} already exists')
except FileNotFoundError:
	print('Directory does not exist')



'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
try: 
	a=os.mkdir(input('Enter directory name or path'))
	print(f'Directory (or) Directories created')
except FileExistsError:
	print(f'Directory already exists')




