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

z1  =  zip(range(7) , list)  #creates empty zip object z1

print(type(z1))		#<class 'zip'>

disp(z1)		#(0,10) <next> (1,20) <next> (2,30) <next> (3,40) 

z2 = zip_longest(range(7) , list)	#creates empty zip object z2

print(type(z2))		#<class 'itertools.zip_longest'>

disp(z2)		#(0,10) <next> (1,20) <next> (2,30) <next> (3,40) <next> (4,40) <next> (5,None) <next> (6,None) <next> (7,None)









#  Find  outputs  (Home  work)

import  time

from  itertools  import  repeat

r = repeat(25 , times = 3)

print('1st  repeat  object')  #1st repeat object

while   True:

	try:

		print(next(r))  #25 <next> 25 <next> 25 

		time . sleep(1)

	except:

		break

print('2nd  repeat  object')    #2nd repeat objecct

r  =  repeat('Hyd')

while   True:

	print(next(r))		#Hyd <next> Hyd <next> Hyd

	time . sleep(1)







#  Find  outputs  (Home  work)

import   time

from    itertools    import  cycle

list = [10 , 20 , 30 , 40]

c = cycle(list)

print(type(c))	     #<class 'itertools.cycle'>

while   True:

	print(next(c))	#10 <next> 20 <next> 30 <next> 40 cycle repeats upto infinite 

	time . sleep(1)







# Find  outputs  (Home  work)

import  time

from  itertools  import  repeat

m = map(pow , range(10) ,  repeat(2))

while   True:

	try:

		print(next(m))	#0 <next> 1 <next> 4 <next> 9 <next> 16 <next> 25 <next> 36 <next> 49 <next> 64 <next> 81 

		time . sleep(1)

	except:

		break







# Find  outputs  (Home  work)

import  time

from  itertools  import  repeat

m = map(pow , range(10) ,  range(2 , 3))

while   True:

	try:

		print(next(m))		#0  range(2,3) is exhausted so it fetches only one value 0

		time . sleep(1)

	except:

		break







# Find  outputs  (Home  work)

import  time

from  itertools  import  repeat

m = map(pow , range(10) ,  range(2))  #pow(x,y) it executes only 2 times range(2) exhauststed

while   True:

	try:

		print(next(m))    #1 1

		time . sleep(1)

	except:

		break





# Find  outputs  (Home  work)

import  time

from  itertools  import  repeat

m = map(pow , repeat(2) ,  range(10))

while   True:

	try:

		print(next(m))	#2^0 <next> 2^1 <next> 2^3 <next> 2^4 <next> 2^5 <next> 2^6 <next> 2^7 <next> 2^8 <next> 2^9  

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

c = combinations(list , 3)	#creates combination object c

print('Different  Combinations')  #Different combinations

disp(c)				#('A','B','C') <next> ('A','B','D') <next> ('A','C','D') <next> ('B','C','D') 

print('Different   Permutations')	#Different permutations

p = permutations(list , 3)	#creates empty permutations object p

disp(p)				#prints all the possible combinations with the given alphabets in tuple of 3 elements











from  random  import  *

print(random())		#returns a float between 0 and 1

print(randint(1 , 100))	#returns an integer between 1 and 100(inclusive)

print(uniform(1 , 100))	#returns a float between 1 and 100

print(randrange(10))	#returns a random value from range 0 to 9

print(randrange(1 , 11)) #returns a random value from range 1 to 10

print(randrange(1 , 11 , 2))  #returns a random value from range 1 to 10 in steps of 2

list = [10 , 20 , 15 , 12 , 18]

print(choice(list))	#Random element from the list

print(choice('RAJESH'))	#Random element from the 'RAJESH'

set  =  {10 , 20 , 30 , 40}

print(choice(set))	#error because set is not indexed









from random import choice



s = input("Enter the string: ")



for i in range(10):

    print(choice(s))







from random import choice

from string import ascii_letters, digits



for i in range(10):

    password = ""

    

    password += choice(ascii_letters)  # 1st letter

    password += choice(digits)         # 2nd digit

    password += choice(ascii_letters)  # 3rd letter

    password += choice(digits)         # 4th digit

    password += choice(ascii_letters)  # 5th letter

    password += choice(digits)         # 6th digit

    

    print(password)













from random import choice



list1 = [10, 20, 30, 40, 50]



for i in range(10):

    print(choice(list1))







from random import randint



for i in range(10):

    otp = randint(100000, 999999)

    print(otp)









import webbrowser

import time

from random import randint



sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']



for site in sites:

    webbrowser.open('http://' + site)

    

    # time gap between 5 to 20 seconds

    t = randint(5, 20)

    print(f"Opening {site}, waiting for {t} seconds...")

    

    time.sleep(t)









from random import choice



options = ["rock", "paper", "scissors"]



computer = choice(options)

user = input("Enter rock, paper or scissors: ").lower()



print("Computer choice:", computer)

print("User choice:", user)



if user == computer:

    print("Result: Draw")



elif (computer == "paper" and user == "rock") or \

     (computer == "scissors" and user == "paper") or \

     (computer == "rock" and user == "scissors"):

    print("Result: Computer wins")



else:

    print("Result: User wins")













low, high, attempts = 1, 100000, 0



print("Think of a number between 1 and 100000")



while True:

    guess = (low + high) // 2

    attempts += 1

    print("Guess:", guess)

    r = input("L/H/C: ").upper()



    if r == 'L':

        low = guess + 1

    elif r == 'H':

        high = guess - 1

    else:

        print("Number:", guess)

        print("Attempts:", attempts)

        break







# Find  outputs

import  os

os . system('dir')	#shows files in folder

os . system('pause')	#stops program execution temporarily waits for key press 

os . system('cls')	#clears screen

os . system('py  test.py')	#Hyd <next> Sec <next> Cyb









import os



path = input("Enter directory name or path: ")



try:

    os.mkdir(path)

    print("Directory created successfully")

except FileExistsError:

    print("Directory already exists")

except Exception as e:

    print("Error:", e)











import os



path = input("Enter directory path (e.g., a/b/c): ")

os.makedirs(path, exist_ok=True)



print("Directories created successfully")


