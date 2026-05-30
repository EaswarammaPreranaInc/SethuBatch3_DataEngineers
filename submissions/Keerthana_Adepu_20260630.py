#1
'''
Producer  Consumer  problem  with  Queue  class  (Home  work)

1) What  does  thread  'p'  do  ?   --->   Inserts  a  random  number  between  1  and  100   into  Queue  object  and  sleeps

2) Which  method  is  used  to  insert  an  element  into  Queue  object ?  ---> put()  method  of  Queue  class

3) What  does  put()  method  do  (2  events) ?  --->  Inserts  an  element  into  Queue   object  and
																				   notifies  the  waiting  thread

4) Why  thread  'p'  sleeps   after  insertion ? --->   Just  to  give  a  chance  for  thread  'c'  to  remove  the  element

5) What  does  thread  'c'  do ?   --->  Removes  the  element  from  Queue  object  and  prints

6) Which  method  is  used  to  remove  an  element  from  Queue  object ?  --->  get()  method  of  Queue  class

7) What  does  get()  method  do  when  Queue  is  empty ?  --->  Moves  the  current  thread  to  waiting  state

8) How  long  are  the  two  threads   executed ?  --->  Infinite  times
'''
from threading import *
from queue import Queue
from random import randint
import time
def   f1(q):
    s = current_thread() . name
    while True:
        x = randint(1 , 100)
        q . put(x)
        print(s , 'stores', x)
        time . sleep(2)
def  f2(q):
    s = current_thread() . name
    while True:
        print(s , 'retrieves' , q . get())
# End  of  the  function
q = Queue()
p = Thread(target = f1 , name = 'Producer' , args = [q])
c = Thread(target = f2 , name = 'Consumer' , args = [q])
p . start()
c . start()



#2
'''
Write  a  program  to  convert   roman   number  to   arabic  number

M - 1000
D - 500
C - 100
L - 50
X - 10
V - 5
I - 1

1) Input : XIV
    Reverse  input :   VIX
    sum = 0 + 5 - 1 + 10 = 14
	prev =  10
	
2) Input : MCMXC
    Reverse  input :  CXMCM
    sum = 0 + 100 - 10 + 1000 - 100 + 1000 = 1990
	prev =  1000

3) Input : MMXXVI
    Reverse  string :  
    sum = 0
	prev = 
	
4) Input : MCMLXXXIV
     Reverse  string :  
    sum = 0
	prev = 
	
5) Hint : Use  dictionary	
'''
def   roman_arabic(roman):
    a_r = {'M' : 1000 , 'D' : 500 , 'C' : 100 , 'L' : 50 , 'X' : 10 , 'V' : 5 , 'I' : 1}
    roman = roman[::-1]
    sum = 0
    prev = 0
    for x in roman:
        if a_r[x] >= prev:
            sum += a_r[x]
            prev = a_r[x]
        else:
            sum -= a_r[x]
            prev = a_r[x]
    return sum
# End  of  the  function	
roman = input('Enter roman number: ')
r = roman_arabic(roman)
print('Arabic equivalent: ' , r)
