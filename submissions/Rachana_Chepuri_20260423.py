'''Find  outputs  (Home  work)'''
# from  itertools  import  zip_longest
# import   time
# def  disp(z):
# 	while   True:
# 		try:
# 			print(next(z)) 
# 			time . sleep(1)
# 		except:
# 			break
# # End  of  the  function
# list = [10 , 20 , 30 , 40]
# z1  =  zip(range(7) , list)
# print(type(z1)) # 
# disp(z1)
# z2 = zip_longest(range(7) , list)
# print(type(z2))
# disp(z2)
'''output'''
#<class 'zip'>
# (0,10) 
# (1,20)
# (2,30)
# (4, 40)
#<class 'itertools.zip_longest'>
# (0,10) 
# (1,20)
# (2,30)
# (4, 40)
# (5, None)
# (6, None)
'''Find  outputs  (Home  work)'''
# import   time
# from    itertools    import  cycle
# list = [10 , 20 , 30 , 40]
# c = cycle(list)
# print(type(c))
# while   True:
# 	print(next(c))
# 	time . sleep(1)
'''output'''	
#<class 'itertools.cycle'>
# 10
# 20
# 30
# 40
# 10
# 20
# 30
# 40
# ......
'''Find  outputs  (Home  work)'''
# import  time
# from  itertools  import  repeat
# r = repeat(25 , times = 3)
# print('1st  repeat  object')
# while   True:
# 	try:
# 		print(next(r))
# 		time . sleep(1)
# 	except:
# 		break
# print('2nd  repeat  object')
# r  =  repeat('Hyd')
# while   True:
# 	print(next(r))
# 	time . sleep(1)
'''output'''
#1st  repeat  object
# 25
# 25
# 25
#2nd  repeat  object
# Hyd
# Hyd
# Hyd
# Hyd
# Hyd...
'''Find  outputs  (Home  work)'''
# import  time
# from  itertools  import  repeat
# m = map(pow , range(10) ,  repeat(2))
# while   True:
# 	try:
# 		print(next(m))
# 		time . sleep(1)
# 	except:
# 		break
'''output'''	
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
'''Find  outputs  (Home  work)'''
# import  time
# from  itertools  import  repeat
# m = map(pow , range(10) ,  range(2 , 3))
# while   True:
# 	try:
# 		print(next(m)) # 0
# 		time . sleep(1)
# 	except:
# 		break
'''Find  outputs  (Home  work)'''
# import  time
# from  itertools  import  repeat
# m = map(pow , range(10) ,  range(2))
# while   True:
# 	try:
# 		print(next(m))
# 		time . sleep(1)
# 	except:
# 		break
'''output'''	
# 0
# 1
'''Find  outputs  (Home  work)'''
# import  time
# from  itertools  import  repeat
# m = map(pow , repeat(2) ,  range(10))
# while   True:
# 	try:
# 		print(next(m))
# 		time . sleep(1)
# 	except:
# 		break
'''output'''	
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512
'''Find  outputs (Home  work)'''
# import  time
# def  disp(itr):
# 	while  True:
# 		try:
# 			print(next(itr))
# 			time . sleep(1)
# 		except:
# 			break
# from  itertools  import  combinations,permutations
# list = ['A' , 'B' , 'C' , 'D']
# c = combinations(list , 3)
# print('Different  Combinations')
# disp(c)
# print('Different   Permutations')
# p = permutations(list , 3)
# disp(p)
'''output'''
# Different  Combinations
# ('A', 'B', 'C')
# ('A', 'B', 'D')
# ('A', 'C', 'D')
# ('B', 'C', 'D')
# Different   Permutations
# ('A', 'B', 'C')
# ('A', 'B', 'D')
# ('A', 'C', 'B')
# ('A', 'C', 'D')
# ('A', 'D', 'B')
# ('A', 'D', 'C')
# ('B', 'A', 'C')
# ('B', 'A', 'D')
# ('B', 'C', 'A')
# ('B', 'C', 'D')
# ('B', 'D', 'A')
# ('B', 'D', 'C')
# ('C', 'A', 'B')
# ('C', 'A', 'D')
# ('C', 'B', 'A')
# ('C', 'B', 'D')
# ('C', 'D', 'A')
# ('C', 'D', 'B')
# ('D', 'A', 'B')
# ('D', 'A', 'C')
# ('D', 'B', 'A')
# ('D', 'B', 'C')
# ('D', 'C', 'A')
# ('D', 'C', 'B')


# from  random  import  *
# print(random()) # 0.5
# print(randint(1 , 100)) # 2
# print(uniform(1 , 100)) # 50.5
# print(randrange(10)) #  9
# print(randrange(1 , 11)) # 1 
# print(randrange(1 , 11 , 2)) # 1 
# list = [10 , 20 , 15 , 12 , 18]
# print(choice(list)) # 18
# print(choice('RAJESH')) # R
# set  =  {10 , 20 , 30 , 40}
# #print(choice(set)) # Error---set is unordered and not indexed
''' Write  a  program  to  print  random  character  of  the  string  10  times (Home  work'''
# from random import choice
# s = eval(input('Enter String : '))
# for x in range(10):
#     print(choice(s))
'''Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits '''
# from random import choice
# import string
# for x in range(10):
#     password = "" 
#     for i in range(3): 
#         password += choice(string.ascii_letters) 
#         password += choice(string.digits)         
#     print(password)
'''Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)'''
# from random import choice
# lst = [ 25 ,10.8,'Hyd' ,True, 3+4j , None]
# for x in range(10):
#     print(choice(lst)) 

'''Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)'''
# from random import randint
# for x in range(10):
#     print(randint(100000, 999999))

'''Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website
2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites'''
# import webbrowser
# import time
# from random import randint
# lst = ['https://www.google.com',
#        'https://www.rediff.com',
#        'https://www.gmail.com',
#        'https://www.amazon.com',
#        'https://www.netflix.com']
# for site in lst:
#     webbrowser.open(site)
#     time.sleep(randint(5, 20))
'''(Home  work)
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
# import random
# choices = ["Rock", "Paper", "Scissors"]
# while True:
#     print("\nWhat do you want to select (0 - Rock, 1 - Paper, 2 - Scissors): ", end="")
#     user_choice = int(input())
#     user = choices[user_choice]
#     computer = random.choice(choices)
#     print("User     :", user)
#     print("Computer :", computer)
#     if user == computer:
#         print("Result   : Draw")
#     elif (user == "Rock" and computer == "Scissors") or \
#          (user == "Scissors" and computer == "Paper") or \
#          (user == "Paper" and computer == "Rock"):
#         print("Result   : User wins")
#     else:
#         print("Result   : Computer wins")
#     choice = input("Continue (y / n) ? ").lower()
#     if choice != 'y':
#         print("End of the game")
#         break

# import random
# low = 1
# high = 100000
# attempts = 0
# secret = random.randint(1, 100000)
# while True:
#     guess = int(input(f"Enter any number between {low} and {high} : "))
#     attempts += 1
#     if guess < low or guess > high:
#         print("Out of range, try again")
#         continue
#     if guess < secret:
#         print("Too low , try again")
#         low = guess + 1
#     elif guess > secret:
#         print("Too high , try again")
#         high = guess - 1
#     else:
#         print("Correct number!")
#         print("Number:", secret)
#         print("Attempts:", attempts)
#         break

'''Find  outputs'''
# import  os
# os . system('dir')
# os . system('pause')
# os . system('cls')
# os . system('py  test.py')
'''
test.py  file  of  cwd  contains
-----------------------------------
print('Hyd')
print('Sec')
print('Cyb')
'''
'''Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory'''
# import os
# path = input("Enter directory name or full path: ")
# try:
#     os.mkdir(path)
#     print("Directory created successfully")
# except FileExistsError:
#     print("Directory already exists")
# except Exception as e:
#     print("Error:", e)


import os
path = input("Enter directory path (e.g., a/b/c): ")
os.makedirs(path, exist_ok=True)
print("Directories created successfully!")

