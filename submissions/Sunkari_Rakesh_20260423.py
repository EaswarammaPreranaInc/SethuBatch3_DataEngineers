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
disp(z1) # # (0 , 10) <nextline> (1 , 20) <nextline> (2 , 30) <nextline> (3 , 40)
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'itertools.zip_longest'>
disp(z2) # (0 , 10) <nextline> (1 , 20) <nextline> (2 , 30) <nextline> (3 , 40) <nextline> (4 , None) <nextline> (5 , None) <nextline> (6 , None) 

#  Find  outputs  (Home  work)
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

#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c)) # 10 <nextline> 20 <nextline> 30 <nextline> 40 this is printed infinite times which results in infinite loop
	time . sleep(1)

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
Output
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
		print(next(m)) # 0
		time . sleep(1)
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m)) # 1 <nextline> 1
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
Output
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
Outputs
Different  Combinations
('A' , 'B' , 'C')
('A' , 'C' , 'D')
('B' , 'C' , 'D')
('A' , 'B' , 'D')

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

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
# Code :
from random import *
s = input('Enter any string : ')
for i in range(10):
    print(choice(s))

''' 
Output
Enter any string : Hyderabad
d
r
a
b
a
r
a
H
a
r
'''
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
# Code:
from random import *
for i in range(10):
    pwd = ''
    for i in range(3):
        letter = randint(65,90)
        pwd+=chr(letter)
        num = randint(49,57)
        pwd+=chr(num)
    print(pwd)

'''
Output
U8M2R8
X9V8H8
F9Q7T4
G5T3U7
E9M1X8
Y1D6H3
C7V5F7
D6V1L9
A1R2T8
Q9K4E2
'''
# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
# Code :
from random import *
list = eval(input("Enter a List : "))
for i in range(10):
    print(choices(list))

'''
 Output 
Enter a List : [25,10.8,'Hyd',True,3+4j,None]
(3+4j)
10.8
(3+4j)
None
25
10.8
(3+4j)
None
None
None
'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
# Code :
from random import *
for i in range(10):
    otp=''
    for i in range(6):
        num = randint(49,57)
        otp+= chr(num)
    print(otp)
''' 
Output
858924
873151
425493
988768
796964
319122
182192
158679
922587
589431
'''

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
# Code :
from webbrowser import *
from random import *
import time
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(10):
    open(choices(list))
    t = randint(5,20)
    time.sleep(t)
	
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
# Code :
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from random import *
def getVal(n):
    val = ''
    if n == 0 :
        val = 'Rock'
    elif n == 1 :
        val = 'Paper'
    elif n == 2 : 
        val = 'Scissors'
    return val
    
while True :
    n = int(input('What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors : '))
    user = getVal(n)
    print('User : ',user)
    comp = getVal(randint(0,2))
    print('Computer : ',comp)
    if user == comp:
        print('Draw')
    elif (comp == 'Paper' and user == 'Rock') or(comp == 'Scissors' and user == 'Paper') or (comp == 'Rock' and user == 'Scissors') :
        print('Computer Wins')
    else :
        print('User Wins')
    res = input('Continue ( y / n ) : ')
    if res != 'y':
        break
print('End of the game')
 
'''
Output
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors : 2
User :  Scissors
Computer :  Paper
User Wins
Continue ( y / n ) : y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors : 1
User :  Paper
Computer :  Scissors
Computer Wins
Continue ( y / n ) : y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors : 0
User :  Rock
Computer :  Scissors
User Wins
Continue ( y / n ) : y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors : 2
User :  Scissors
Computer :  Scissors
Draw
Continue ( y / n ) : n
End of the game

'''

'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
# Code :
from random import * 
num = randint(1,100000)
count = 0
low = 1
high = 100000
while True :
    n = int(input(f'Enter any number between {low} and {high} : '))
    if n == num :
        break
    if n < num:
        print('Too low , try again')
        low = n
    elif n > num :
        print('Too high , try again')
        high = n
    count+=1
print(f'Guessed {num} in {count} attempts')

''' Output:
Enter any number between 1 and 100000 : 50001
Too high , try again
Enter any number between 1 and 50001 : 25001
Too high , try again
Enter any number between 1 and 25001 : 12501
Too high , try again
Enter any number between 1 and 12501 : 6250
Too low , try again
Enter any number between 6250 and 12501 : 9500
Too high , try again
Enter any number between 6250 and 9500 : 7250
Too low , try again
Enter any number between 7250 and 9500 : 8250
Too high , try again
Enter any number between 7250 and 8250 : 7750
Too low , try again
Enter any number between 7750 and 8250 : 8000
Too low , try again
Enter any number between 8000 and 8250 : 8125
Too high , try again
Enter any number between 8000 and 8125 : 8075
Too high , try again
Enter any number between 8000 and 8075 : 8030
Too high , try again
Enter any number between 8000 and 8030 : 8015
Too low , try again
Enter any number between 8015 and 8030 : 8023
Too high , try again
Enter any number between 8015 and 8023 : 8019
Too low , try again
Enter any number between 8019 and 8023 : 8021
Guessed 8021 in 15 attempts

'''
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

''' 
Output
Enter directory path : \a\b\c
Directory (or) directories created 

Enter directory path : \a\b\c
Directory (or) directories already exists 

Enter directory path : \ssdc\x\y
Directory (or) directories created

'''