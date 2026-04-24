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
print(type(z1))     #<class 'zip'>
disp(z1)            #(0, 10) (1, 20) (2, 30) (3, 40)
z2 = zip_longest(range(7) , list)
print(type(z2))     #<class 'zip_longest'>
disp(z2)            #(0, 10) (1, 20) (2, 30) (3, 40) (4, None) (5, None) (6, None)



#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))      #>class 'cycle' from itertools>
while   True:
	print(next(c))  #infinity rotation of 10, 20, 30, 40,....
	time . sleep(1)
	


#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')    # 1st repeat  object
while   True:
	try:
		print(next(r))      #25 25 25 repeats only 3 times
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')    # 2nd repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r))      #Hyd Hyd Hyd HYd ...... repeats infinity times
	time . sleep(1)
	



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))      #0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break
	


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))      #0
		time . sleep(1)
	except:
		break
	


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))      #1  1
		time . sleep(1)
	except:
		break


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))      #1 2 4 8 16 32 64 128 256 512
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
print('Different  Combinations')    #Different  Combinations
disp(c)                             #('A','B','C') ('A','B','D') ('A','C','D') ('B','C','D')
print('Different   Permutations')   #Different   Permutations
p = permutations(list , 3)
disp(p)         #('A','B','C') ('A','B','D') ('A','C','B') ('A','C','D') ('A','D','B') ('A','D','C')     
                #('B','A','C') ('B','A','D') ('B','C','A') ('B','C','D') ('B','D','A') ('B','D','C')
				#('C','A','B') ('C','A','D') ('C','B','A') ('C','B','D') ('C','D','A') ('C','D','B')
				#('D','A','B') ('D','A','C') ('D','B','A') ('D','B','C') ('D','C','A') ('D','C','B')




from  random  import  *
print(random())     #0.1650851255487959
print(randint(1 , 100))     #75  any random integer between 1 to 100
print(uniform(1 , 100))     #25.88 any random float between 1 to 100
print(randrange(10))        #4 any random integer between 0 to 9
print(randrange(1 , 11))    #8 any random integer between 1 to 10
print(randrange(1 , 11 , 2))    #1 any random odd integer between 1 to 10
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))     #15 any random element from the list
print(choice('RAJESH'))     #S any random character from the string
set  =  {10 , 20 , 30 , 40}
print(choice(set))      #Error due to 'set' object is not subscriptable



# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from  random  import  *
s = input('Enter  a  string : ')
for  i  in  range(10):
    print(choice(s))



'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
from  random  import  *
for  i  in  range(10):
    password = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + choice('0123456789') + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + choice('0123456789') + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + choice('0123456789')
    print(password)




# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from  random  import  *
list = [10 , 20 , 15 , 12 , 18]
for  i  in  range(10):
    print(choice(list))




# # Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
from  random  import  *
for  i  in  range(10):
    otp = int(randint(100000 , 999999))
    print(otp)





'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
def  open_websites(websites):
    import  webbrowser
    import  time
    from  random  import  randint
    for  website  in  websites:
        webbrowser . open('http://google.com' + website)
        time . sleep(randint(5 , 20))



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
import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()





'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.
2) Print  the  number  and  number  of  attempts
'''
from  random  import  *
number = randint(1 , 100000)
attempts = 0
while  True:
    user_input = int(input('Guess  a  number  between  1  and  100000 : '))
    attempts += 1
    if user_input < number:
        print('Too low')
    elif user_input > number:
        print('Too high')
    else:
        print(f'Congratulations! You guessed the number {number} in {attempts} attempts.')
        break




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
#Directory of F:\SSSSD\Pradeep_Dasi_20260423.py



'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
from  os  import  *
dir_name = input('Enter  a  directory  name  or  path : ')
try:
    mkdir(dir_name)
    print(f'Directory "{dir_name}" created successfully.')
except FileExistsError:
    print(f'Directory "{dir_name}" already exists.')
except Exception as e:
    print(f'An error occurred: {e}')




'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
from  os  import  *
dir_path = input('Enter  a  group  of  directories  (e.g., a/b/c) : ')
try:
    makedirs(dir_path)
    print(f'Group of directories "{dir_path}" created successfully.')   
except FileExistsError:
    print(f'Group of directories "{dir_path}" already exists.')
except Exception as e:
    print(f'An error occurred: {e}')