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
print(type(z1))# <class zip>
disp(z1)#(10,0)(20,1)(30,2)(40,3)
z2 = zip_longest(range(7) , list)
print(type(z2))#<class itertools.zip_longest>
disp(z2)#(10,0)(20,1)(30,2)(40,3)(None,4)(None,5)(None,6)


#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')#1st  repeat  object
while   True:
	try:
		print(next(r))# 25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')#2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r))# Hyd HYd Hyd ....infinite times
	time . sleep(1)

#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))# <class itertools.cycle>
while   True:
	print(next(c))# 10 20 30 40 10 20 30 40 10 20 30......cycling infinite times
	time . sleep(1)

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))# 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))# 0
		time . sleep(1)
	except:
		break


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))# 1 1
		time . sleep(1)
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))# 1 2 4 8 16 32 64 128 256 512
		time . sleep(1)
	except:
		break

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
print('Different  Combinations')#Different  Combinations
disp(c)# [A,B,C] [A,C,D] [A,B,D] [B,C,D ] 
print('Different   Permutations')#Different   Permutations
p = permutations(list , 3)
disp(p)
#('A', 'B', 'C')('A', 'B', 'D')('A', 'C', 'B')('A', 'C', 'D')('A', 'D', 'B')('A', 'D', 'C')('B', 'A', 'C')
#('B', 'A', 'D')('B', 'C', 'A')('B', 'C', 'D')('B', 'D', 'A'('B', 'D', 'C')('C', 'A', 'B')('C', 'A', 'D')
##('D', 'B', 'C')('D', 'C', 'A')('D', 'C', 'B')

from  random  import  *
print(random())# random value btw 0 and 1, 0and 1 are not included
print(randint(1 , 100))# random value btw 1 and 100 include 1 and 100
print(uniform(1 , 100))# random value btw 1 and 100 exclude 1 and 100
print(randrange(10))# random value btw 0 to 9 , 10 not included
print(randrange(1 , 11))# random value btw 1 to 10, 11 not included
print(randrange(1 , 11 , 2))# random value btw 1 3 5 7 9 , 11 not included
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))# random element from list
print(choice('RAJESH'))# random character in string
set  =  {10 , 20 , 30 , 40}
#print(choice(set))# Error

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
str=input("Enter string : ")
for i in range(10):
    print(choice(str))

#Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
from random import *
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits='0123456789'
for i in range(10):
    pwd=''
    for j in range(1,7):
        if j%2==1:
            pwd+=choice(alphabets)
        else:
            pwd+=choice(digits)
    print(pwd)


# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
list=eval(input("Enter list of elements : "))
for i in range(10):
    print(choice(list))

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from random import *
digits='0123456789'
for i in range(10):
    otp=''
    for j in range(6):
        otp+=choice(digits)
    print(otp)


#Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
from webbrowser import *
from random import *
import time
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(5):
    open(choice(list))
    time.sleep(uniform(5,20))

#Write  a  program  to  implement  Rock , paper  and  scissors  game 
#  between  user  and  computer
from random import *
def game(user,computer):
    if user==computer:
        print("Draw")
    elif (user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1):
        print("Computer wins")
    else:
        print("User wins")
user=int(input("Enter R is 1, P is 2, S is 3  : "))
computer=randint(1,3)
game(user,computer)
onemoretime=input("Do you want to continue(y / n) : ")
while onemoretime=='y':
    user=int(input("Enter R is 1, P is 2, S is 3  : "))
    computer=randint(1,3)  
    game(user,computer)
    onemoretime=input("Do you want to continue(y / n) : ")


#Write  a  program  to  guess  a  number  between   1  and  100000.
#1) Print  Too  low  (or)  Too  high  depending  on  input.
#2) Print  the  number  and  number  of  attempts
from random import *
number = randint(1, 100000)
attempts = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 100000: "))
        attempts += 1
        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    except:
            print("Please enter a valid number!")


# Find  outputs
import  os
os . system('dir')# all directories of current working module
os . system('pause')# executes cwd and paused until user press any key
os . system('cls')# executes cls cmd to clear the screen
os . system('py  test.py')# Hyd Sec Cyb


#Write  a  program  to  create  a  directory.
#Input  is  either  directory  name  (or)  path  of  the  directory
import os
direc=input("Enter directory name to create")
try:
    os.mk.dir(direc)
    print(f'Directory {direc} is created')
except FileExistsError:
    print(f'{direc} already exist')
except FileNotFoundError:
    print(f'{direc} already exist')

#Write  a  program  to  create  a  group  of  directories.
import os
grpofdirs=input("Enter group of dirs")
try:
    os.makedirs(grpofdirs)
    print(f'Directories created')
except FileExistsError:
    print(f'Directories{grpofdirs} already exists')
except FileNotFoundError:
    print(f'Directories{grpofdirs} already exists')





