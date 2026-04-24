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
print(type(z1))# <class 'zip'>
disp(z1)#(0,10) (1,20) (2,30) (3,40)
z2 = zip_longest(range(7) , list)
print(type(z2))# <class 'zip_longest'>
disp(z2)#(0,10) (1,20) (2,30) (3,40) (4,None) (5,None) (6,None)

### Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
# infinite loop 10 20 30 40 
###
#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))#25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))#25 25 25 .........
	time . sleep(1)
###
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))#1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break
###
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
###
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))#1 1<0 1 2 3 4 5 6 7 8 9<0 1 
while   True:
	try:
		print(next(m))#1 1
		time . sleep(1)
	except:
		break
###
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))#2^0 2^1 2^2...2^9<==0 1 2 3 4 5 6 7 8 9
while   True:
	try:
		print(next(m))#1 2 4 8 16 32 64 128 256 512
		time . sleep(1)
	except:
		break
###
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
disp(c)#'''('A', 'B', 'C') ('A', 'B', 'D')('A', 'C', 'D')('B', 'C', 'D')'''
print('Different   Permutations')
p = permutations(list , 3)
disp(p)#('A', 'B', 'C')
'''('A', 'B', 'D')
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
('D', 'C', 'B')'''
###
from  random  import  *
print(random())#random decimal nbr between 0 and 1
print(randint(1 , 100))#random integer nbe between 1-100
print(uniform(1 , 100))#random decimal nbr between 1-100
print(randrange(10))#random nbr in the ranfe of 10
print(randrange(1 , 11))#random nbr in the range between 1-11
print(randrange(1 , 11 , 2))##random nbr in the range between 1-11 in steps of 11 i.e 1,3,5,7,9,11
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))#any random object from the list
print(choice('RAJESH'))#any random character from the string
set  =  {10 , 20 , 30 , 40}
#print(choice(set))#error
###
# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
import time
a=input("enter the srting:")
for i in range(10):
        print(choice(a))
        time.sleep(1)
###
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
a=[]
for i in range(97, 123):
    a.append(chr(i).upper())    
    #print(chr(i).upper(), end=" ")
from random import *
import time
#print(a)
for i in range(10):
        pwd=choice(a)+str(randint(1,10))+choice(a)+str(randint(1,10))+choice(a)+str(randint(1,10))
        print(pwd)
        time.sleep(1)
        
###
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import time
from random import *
a=eval(input("enter the list elemnts:"))
for i in range(10):
        print(choice(a))
###
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import time
from random import *
a=range(100000,999999)
for i in range(10):
        print(choice(a))
        time.sleep(1)
###
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser
import time
from random import *
a= ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(5):
        site=choice(a)
        print(webbrowser.open(site))        
        time.sleep(5)
###
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

items = ['Rock', 'Paper', 'Scissors']

while True:
    user = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : "))

    if user not in [0, 1, 2]:
        print("Invalid input")
        continue

    computer = choice(items)

    print("User  :", items[user])
    print("Computer  :", computer)

    # Draw
    if items[user] == computer:
        print("Draw")

    # User wins
    elif (items[user] == 'Rock' and computer == 'Scissors') or \
         (items[user] == 'Paper' and computer == 'Rock') or \
         (items[user] == 'Scissors' and computer == 'Paper'):
        print("User wins")

    # Computer wins
    else:
        print("Computer wins")

    ch = input("Continue ( y / n ) ? ")
    if ch.lower() != 'y':
        print("End of the game")
        break
###
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
###
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
###
'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
###
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''