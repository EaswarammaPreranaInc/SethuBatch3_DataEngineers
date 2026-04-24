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
disp(z1)
'''
(0, 10)
(1, 20)
(2, 30)
(3, 40)
'''
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'itertools.zip_longest'>
disp(z2)
'''
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
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c))
	time . sleep(1)
'''
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
...Infinite loop
'''






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
Hyd
Hyd
Hyd
Hyd
...Infinite loop
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
		print(next(m))
		time . sleep(1)
	except:
		break
'''
pow(0, 2) = 0
'''










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
pow(0,0) = 1
pow(1,1) = 1
'''








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
'''
Different  Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
'''
print('Different   Permutations')
p = permutations(list , 3)
disp(p)
'''
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







#
from  random  import  *
print(random()) # 0.5
print(randint(1 , 100)) # 25
print(uniform(1 , 100)) # 26.06
print(randrange(10)) # 2
print(randrange(1 , 11)) # 7
print(randrange(1 , 11 , 2)) # 7
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # 20
print(choice('RAJESH')) # S
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # ERROR because set is not indexed






# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

from random import choice
s = input('Enter any string : ')
for i in range(10):
    print(choice(s))

'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from random import choice
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
for i in range(10):
    password = ''    
    password += choice(alphabets)  
    password += choice(digits)     
    password += choice(alphabets)  
    password += choice(digits)     
    password += choice(alphabets)  
    password += choice(digits)         
    print(password)







# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

from random import choice
lst = eval(input('Enter a List : '))
for i in range(10):
    print(choice(lst))





# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

from random import randint
for i in range(10):
    otp = ''
    for j in range(6):
        otp += str(randint(0, 9))
    print(otp)






'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website
2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser
import time
from random import randint
lst= ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

for x in lst:
    webbrowser.open('http://' + x)   
    
    delay = randint(5, 20)              
    print('Waiting for', delay, 'seconds...')
    time.sleep(delay)






'''
(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw
2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  ---> Computer  wins  becoz  parer  dominates  rock																								
3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  ---> Computer  wins  becoz  scissors  dominates  paper																										
4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  ---> Computer  wins  becoz  rock  dominates  scissors
5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
Sample output:
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 0
User  :  Rock
Computer  :  Rock
Draw
Continue ( y / n ) ? y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 2
User  :  Scissors
Computer  :  Paper
User wins
Continue ( y / n ) ? y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 1
User  :  Paper
Computer  :  Scissors
Computer wins
Continue ( y / n ) ? n
End of the game
'''
from random import choice

options = ['Rock', 'Paper', 'Scissors']
while True:
    user = int(input('What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : '))
    user_choice = options[user]

    comp_choice = choice(options)

    print('User :', user_choice)
    print('Computer :', comp_choice)

    if user_choice == comp_choice:
        print('Draw')
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        print('User wins')
    else:
        print('Computer wins')

    ch = input("Continue ( y / n ) ? ")
    if ch.lower() == 'n':
        print('\nEnd of the game')
        break






'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.
2) Print  the  number  and  number  of  attempts
'''
from random import randint

low = 1
high = 100000
num = randint(low, high)
count = 0
while True:
    guess = int(input(F'Enter any number between {low} and {high} : '))
    count += 1

    if guess < num:
        print('Too low , try again')
        low = guess + 1

    elif guess > num:
        print('Too high , try again')
        high = guess - 1

    else:
        print(F'Guessed {num} in {count} attempts')
        break







# Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls') # Clears the screen
os . system('py  test.py')
'''
Hyd
Sec
Cyb
'''

'''
test.py  file  of  cwd  contains
print('Hyd')
print('Sec')
print('Cyb')
'''




'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory

Sample output:
Enter directory name (or) path : Sec
Directory Sec created
Press any key to continue . . .
Enter directory name (or) path : Sec
Directory Sec already exists
Press any key to continue . . .
Enter directory name (or) path : kavya\student
Directory kavya\student created
Press any key to continue . . .
Enter directory name (or) path : asia/australia
Directory does not exist
Press any key to continue . . .
'''
import os

path = input('Enter directory name (or) path : ')
if os.path.exists(path):
    print(F'Directory {path} already exists')
else:
    try:
        os.makedirs(path)
        print(F'Directory {path} created')
    except:
        print('Directory does not exist')





'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c

Sample output:
Enter directory path : a/b/c
Directory (or) directories created


Enter directory path : a/b/d
Directory (or) directories created

Enter directory path : a/b/c
Directory (or) directories already exists
'''
import os

path = input("Enter directory path : ")

if os.path.exists(path):
    print('Directory (or) directories already exists')
else:
    os.makedirs(path)
    print('Directory (or) directories created')