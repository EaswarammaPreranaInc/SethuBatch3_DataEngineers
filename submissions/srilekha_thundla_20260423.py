#  Find  outputs  (Home  work)
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
# print(type(z1))
# disp(z1)#(10,0)\n(20,1)\n(30,2)
# z2 = zip_longest(range(7) , list)
# print(type(z2))
# disp(z2)#(0,10)\n(1,20)\n(2,30)\n(3,40)\n(4,none)\n(5,none)\n(6,none)

#  Find  outputs  (Home  work)
# import   time
# from    itertools    import  cycle
# list = [10 , 20 , 30 , 40]
# c = cycle(list)
# print(type(c))
# while   True:
# 	print(next(c))#infinite loop of list
# 	time . sleep(1)


#  Find  outputs  (Home  work)
# import  time
# from  itertools  import  repeat
# r = repeat(25 , times = 3)
# print('1st  repeat  object')#1st repeat object
# while   True:
# 	try:
# 		print(next(r))#25\n 25 \n 25
# 		time . sleep(1)
# 	except:
# 		break
# print('2nd  repeat  object')#2nd repeat object
# r  =  repeat('Hyd')
# while   True:
# 	print(next(r))#infinite HYD
# 	time . sleep(1)



# Find  outputs  (Home  work)
# import  time
# from  itertools  import  repeat
# m = map(pow , range(10) ,  repeat(2))
# while   True:
# 	try:
# 		print(next(m))#0 \n 1 \n 4 \n 16 \n 25 \n 35 \n 49 \n 64 \n 81
# 		time . sleep(1)
# 	except:
# 		break

# Find  outputs  (Home  work)
# import  time
# from  itertools  import  repeat
# m = map(pow , range(10) ,  range(2 , 3))
# while   True:
# 	try:
# 		print(next(m))
		
# 		time . sleep(1)
# 	except:
# 		break


#  Find  outputs (Home  work)
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
# print('Different  Combinations')#Different  Combinations
# disp(c)#('A','B','C')\n ('A', 'B', 'D') \n ('A', 'C', 'D') \n ('B', 'C', 'D')

# print('Different   Permutations')#Different   Permutations
# p = permutations(list , 3)
# disp(p)
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
# print(random())
# print(randint(1 , 100))# any int number from range of 1 to 100
# print(uniform(1 , 100))#any float number from range of 1 to 100
# print(randrange(10))#any int  number from range of 0 to 10
# print(randrange(1 , 11))#any int  number from range of 1 to 11
# print(randrange(1 , 11 , 2))# chooses 1 number from (1,3,5,7,9)
# list = [10 , 20 , 15 , 12 , 18]
# print(choice(list))#selects 1 element from list
# print(choice('RAJESH'))#selects i charecter from string
# set  =  {10 , 20 , 30 , 40}
# # print(choice(set))#error

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
# string = input("enter a string : ")
# from  random  import  *
# import time
# for i in range(10):
#     print(choice(string))
#     time.sleep(1)

'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
# from random import *
# from  itertools  import  repeat
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digi= '0123456789'
# for i in range(10):
#     password = choice(alpha)+choice(digi)+choice(alpha)+choice(digi)+choice(alpha)+choice(digi) 
#     print(password)

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
# import webbrowser
# import time

# sites = ['http://google.com', 'http://rediff.com', 'http://gmail.com', 'http://amazon.com', 'http://netflix.com']
# for i in sites:
#     webbrowser.open(i)
#     time.sleep(5)   

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
'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
# from random import*
# comp = randrange(1,100001)
# # from itertools import repeat
# i = 1
# while True:
#     number = int(input("Enter any number between 1 to 100000 : "))
#     if number> comp:
#         print("Too high , try again")
#         i+=1
#     elif number< comp:
#         print("Too low , try again")
#         i+=1
#     else:
#         print(f'Guessed comp in {i} attempts')
#         break



