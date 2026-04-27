'''
1) # Find outputs (Home work)
from itertools import zip_longest
import time
def disp(z):
	while True:
		try:
			print(next(z))
			time.sleep(1)
		except:
			break
# End of the function
list = [10 , 20 , 30 , 40]
z1 = zip(range(7) , list)
print(type(z1)) # <class 'zip'>
disp(z1) # (0, 10) <nextline> (1, 20) <nextline> (2, 30) <nextline> (3, 40)
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'itertools.zip_longest'>
disp(z2) # (0, 10) <nextline> (1, 20) <nextline> (2, 30) <nextline> (3, 40) <nextline> (4, None) <nextline> (5, None) <nextline> (6, None)
'''
'''
2) # Find outputs (Home work)
import time
from itertools import repeat
r = repeat(25 , times = 3)
print('1st repeat object')
while True:
	try:
		print(next(r)) # 25 <nextline> 25 <nextline> 25
		time.sleep(1)
	except:
		break
print('2nd repeat object')
r = repeat('Hyd')
while True:
	print(next(r)) # infinite repetition of Hyd
	time.sleep(1)
'''
'''
3) # Find outputs (Home work)
import time
from itertools import cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) # <class 'itertools.cycle'>
while True:
	print(next(c)) # 10 <nextline> # 20 <nextline> 30  <nextline> 40
	time.sleep(1)
'''
'''
4) # Find outputs (Home work)
import time
from itertools import repeat
m = map(pow , range(10) , repeat(2))
while True:
	try:
		print(next(m)) # 0 <nextline> # 1 <nextline> # 4 <nextline> 9 <nextline> 6 <nextline> 16 <nextline> 25 <nextline> 36 <nextline> 49 <nextline> 64 <nextline> 81
		time.sleep(1)
	except:
		break
'''
'''
5) # Find outputs (Home work)
import time
from itertools import repeat
m = map(pow , range(10) , range(2 , 3))
while True:
	try:
		print(next(m)) # 1 <nextline> 2 <nextline> 4 <nextline> 8 <nextline> 16 <nextline> 32 <nextline> 64 <nextline> 128 <nextline> 256 <nextline> 512 
		time.sleep(1)
	except:
		break # 1
'''
'''
6) # Find outputs (Home work)
import time
from itertools import repeat
m = map(pow , range(10) , range(2))
while True:
	try:
		print(next(m)) # 1 <nextline> 1
		time.sleep(1)
	except:
		break
'''
'''
7) # Find outputs (Home work)
import time
from itertools import repeat
m = map(pow , repeat(2) , range(10))
while True:
	try:
		print(next(m)) # 1 <nextline> 2 <nextline> 4 <nextline> 8 <nextline> 16 <nextline> 32 <nextline> 64 <nextline> 128 <nextline> 256 <nextline> 512
		time.sleep(1)
	except:
		break
'''
'''
8) # Find outputs (Home work)
import time
def disp(itr):
	while True:
		try:
			print(next(itr))
			time.sleep(1)
		except:
			break
from itertools import combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different Combinations')
disp(c) # ('A', 'B', 'C') <nextline> ('A', 'B', 'D') <nextline> ('A', 'C', 'D') <nextline> ('B', 'C', 'D')
print('Different Permutations')
p = permutations(list , 3)
disp(p) # ('A', 'B', 'C') <nextline> ('A', 'B', 'D') <nextline> ('A', 'C', 'B') <nextline> ('A', 'C', 'D') <nextline> ('A', 'D', 'B') <nextline> ('A', 'D', 'C') <nextline> ('B', 'A', 'C') <nextline> ('B', 'A', 'D') <nextline> ('B', 'C', 'A') <nextline> ('B', 'C', 'D') <nextline> ('B', 'D', 'A') <nextline> ('B', 'D', 'C') <nextline> ('C', 'A', 'B') <nextline> ('C', 'A', 'D') <nextline> ('C', 'B', 'A') <nextline> ('C', 'B', 'D') <nextline> ('C', 'D', 'A') <nextline> ('C', 'D', 'B') <nextline> ('D', 'A', 'B') <nextline> ('D', 'A', 'C') <nextline> ('D', 'B', 'A') <nextline> ('D', 'B', 'C') <nextline> ('D', 'C', 'A') <nextline> ('D', 'C', 'B') \
'''
# 10) Write a program to print random character of the string 10 times (Home work)
from random import choice
a = input('Enter a string : ')
for i in range(10):
	print(choice(a))
'''
11)(Home work)
Write a program to generate 10 passwords each of 6 character length where
1st , 3rd , 5th characters are alphabets and 2nd , 4th , 6th characters are digits
'''
from random import choice
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
for i in range(10):
	p = ''
	p += choice(alphabets)
	p += choice(digits)
	p += choice(alphabets)
	p += choice(digits)
	p += choice(alphabets)
	p += choice(digits)
	print(p)
# 12) # Write a program to print random element of the list ten times (Home work)
from random import choice
a = [10 , 20 , 15 , 12 , 18]
for i in range(10):
	print(choice(a))

#13) # Write a program to generate ten six-digit OTP's (Home work)
from random import randint
for i in range(10):
	print(randint(100000 , 999999))
'''
#14) Write a program to open any website from gmail , google , rediff , ... with a time gap of 5 to 20 sec
1) What does open('http://google.com') do ? ---> Opens google.com website
2) Where is open() function defined ? ---> In webbrowser module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide a time gap of 5 to 20 sec between the websites
'''
import webbrowser
import time
from random import randint
sites = ['https://google.com' , 'https://rediff.com' , 'https://gmail.com' , 'https://amazon.com' , 'https://netflix.com']
for s in sites:
	webbrowser.open(s)
	time.sleep(randint(5 , 20))
'''
15) (Home work)
Write a program to implement Rock , paper and scissors game between user and computer
1) What is the result if user input and computer random number are same ? ---> Draw
2) What is the result if computer selects paper and user input is rock ? ---> Computer wins becoz paper dominates rock
3) What is the result if computer selects scissors and user input is paper ? ---> Computer wins becoz scissors dominates paper
4) What is the result if computer selects rock and user input is scissors ? ---> Computer wins becoz rock dominates scissors
5) What is the result in all other cases ? ---> User wins
'''
from random import randint
choices = {1 : 'Rock' , 2 : 'Paper' , 3 : 'Scissors'}
u = int(input('Enter 1-Rock 2-Paper 3-Scissors : '))
c = randint(1 , 3)
print('Computer : ' , choices[c])
print('User     : ' , choices[u])
if u == c:
	print('Draw')
elif (c == 2 and u == 1) or (c == 3 and u == 2) or (c == 1 and u == 3):
	print('Computer wins')
else:
	print('User wins')
'''
16) Write a program to guess a number between 1 and 100000.
1) Print Too low (or) Too high depending on input.
2) Print the number and number of attempts
'''
from random import randint
n = randint(1 , 100000)
count = 0
while True:
	g = int(input('Guess the number : '))
	count += 1
	if g < n:
		print('Too low')
	elif g > n:
		print('Too high')
	else:
		print('Correct')
		print('Number : ' , n)
		print('Attempts : ' , count)
		break
'''
'''
17) # Find outputs
import os
os.system('dir')
os.system('pause')
os.system('cls')
os.system('py test.py') # Output will depend on OS and current folder contents.
'''
'''
18) Write a program to create a directory.
Input is either directory name (or) path of the directory
'''
import os
path = input('Enter directory path : ')
os.mkdir(path)

'''
19) Write a program to create a group of directories.
Input : a/b/c
'''
import os
path = input('Enter directory path : ')
os.makedirs(path)