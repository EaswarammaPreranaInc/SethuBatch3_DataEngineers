# Find  outputs  (Home  work)
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
print(type(z1))#<class 'zip'>
disp(z1)#(0,10)<nxt>(1,20)<nxt>(2,30)<nxt>(3,40)
z2 = zip_longest(range(7) , list)
print(type(z2))##<class 'itertools.zip_longest'>
disp(z2)#(0,10)<nxt>(1,20)<nxt>(2,30)<nxt>(3,40)<nxt>(4,None)<nxt>(5,None)<nxt>(6,None)


#Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')#1st  repeat  object
while   True:
	try:
		print(next(r))#25<nxt>25<nxt>25
		time . sleep(1)#1 sec delay for each yield 
	except:
		break
print('2nd  repeat  object')#2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r))#Hyd<nxt>HydHyd<nxt>Hyd......Hyd<nxt>Hyd.....Hyd<nxt>Hyd...
	time . sleep(1)#1 sec delay for each yield



#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)#empty object is created 
print(type(c))#<class 'cycle'>
while   True:
	print(next(c))#10<nxt>20<nxt>30<nxt>40<nxt>10<nxt>20<nxt>30<nxt>40<nxt>.......10<nxt>20<nxt>30<nxt>40<nxt>...
	time . sleep(1)#1 sec delay for each yield


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))#map(function,seq1,seq2)-->pow funtion demadns 2 args 
while   True:
	try:
		print(next(m))#0,1,4,9,16,25,36,49,64,81
		time . sleep(1)#1 sec delay for each yield
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))#map(function,seq1,seq2)-->pow funtion demadns 2 args 
while   True:
	try:
		print(next(m))##0
		time . sleep(1)#1 sec delay for each yield
	except:
		break

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))#map(function,seq(10 elmnts ),(seq 2 elmnts ))
while   True:
	try:
		print(next(m))##1<nxt>1
		time . sleep(1)#1 sec delay for each
	except:
		break
# 

# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))#map(fun,seq(2#repates always infinately),(seq of 10 elmnts from 0 to 1))
while   True:
	try:
		print(next(m))#1<nxt>2<nxt>4<nxt>8<nxt>16<nxt>32<nxt>64<nxt>128<nxt>256<nxt>512
		time . sleep(1)#delay of 1 sec for each yield
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
disp(c)#(A,B,C)<NXT>(A,B,D)<NXT>(A,C,D)<NXT>(B,C,D)
print('Different   Permutations')#Different   Permutations
p = permutations(list , 3)
disp(p)#(A,B,C)<NXT>(A,C,D)<NXT>(A,B,D)<NXT>(A,D,C)<NXT>(A,D,B)<NXT>(A,D,C)<NXT>(B,C,D)<NXT>(B,D,C)<NXT>(B,A,C)<NXT>(B,C,A)<NXT>(B,D,A)<NXT>(B,A,D)<NXT>(C,D,B)<NXT>(C,B,D)<NXT>(C,A,D)<NXT>(C,D,A)<NXT>(C,A,B)<NXT>(C,B,A)
# 


from  random  import  *
print(random())#RANDOM NUMBER BETWEEN 0 AND 1 WHERE 0 AND 1 ARE EXCLUDED MAY BE 0.5
print(randint(1 , 100))#ANY INTERGER NUMBER FORM 0 TO 1 AND 0,1 ARE INCLUDED HERE MAY BE 1 OR 100 OR ANY NUMBER BETWWEN 0-100
print(uniform(1 , 100))#ANY FLOAT  NUMBER FORM 0 TO 1 AND 0,1 ARE EXCLUDED HERE MAY BE 23.3
print(randrange(10))#any number from the range of 0 to 9 may be 6
print(randrange(1 , 11))##any number from the range of 1 to 10 may be 10 
print(randrange(1 , 11 , 2))#any number from the range of 1 to 10  in steps of 2 ie may be 7
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))# any random element of the list   may be 12
print(choice('RAJESH'))# any random element of the string may be r
set  =  {10 , 20 , 30 , 40}
print(choice(set))#error choice not takes set as argument as set is not indexed 

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import time 
import random
s=input("enter the string :")
for x in range(10):
    print(random.choice(s))
    time.sleep(0.5)
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''
import random
import time 
chr='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for i in range(10):
    print(random.choice(chr),end="")
    print(random.randint(0,9),end="")
    print(random.choice(chr),end="")
    print(random.randint(0,9),end="")
    print(random.choice(chr),end="")
    print(random.randint(0,9))
      time.sleep(1)

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
import time 
list=eval(input("enter a list:"))
for x in range(10):
    print(random.choice(list))
    time.sleep(1)

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
    
import random
import time 
for i in range(10):
    print(random.randint(0,9),end="")
    print(random.randint(0,9),end="")
    print(random.randint(0,9),end="")
    print(random.randint(0,9),end="")
    print(random.randint(0,9),end="")
    print(random.randint(0,9))
    time.sleep(1)

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website
2) Where  is  open()  function  defined  ?  --->  In  webbrowser  module
3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
import webbrowser
import time 
import random
list = list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for x in range(5):
    print(webbrowser.open(random.choice(list)))
    time.sleep(5)
    



'''
(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw
2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
    Computer  wins  becoz  parer  dominates  rock
3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
	Computer  wins  becoz  scissors  dominates  pap
4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
	Computer  wins  becoz  rock  dominates  scissors
5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''
import random
from itertools import count 
a=count()
r={ 0:'Rock' , 1:'Paper' , 2:'Scissor' }
while True :
    user=int(input("what do u want to select (0-Rock , 1-paper , 2-Scissors):"))
    if user not in r:
        print("invalid input")
        continue
    computer=random.choice(list(r.keys()))
    print("User:", r[user])
    print("Computer:", r[computer])

    if user==computer:
        print("DRAW")
        choice=input("continue (y/n): ")
    elif (computer == 1 and user == 0) or (computer == 2 and user == 1) or (computer == 0 and user == 2):
        print("computer wins")
        choice=input("continue (y/n): ")
    else:
        print("user wins")
        choice=input("continue (y/n): ")

    if choice=='y':
        continue
    else:
        print("End of the Game !")
        break
   

'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.
2) Print  the  number  and  number  of  attempts
'''



# Find  outputs
import  os
os . system('dir')#list all directories in that drive 
os . system('pause')#stops the exceution of the program untill the user press any key from keyboard
os . system('cls')#doc command clear the screen
os . system('py  test.py')#Hyd<nxt>Sec<nxt>Cyd
#######it runs the test.py file 



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

'''
Write  a  program  to  create  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''