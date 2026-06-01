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

def   f1(q):
	Insert  a  random  number  into  Queue  object  and  sleep
	Repeat  this  process  for  infinite  times
def  f2(q):
	Remove  the  first  element  from  Queue  object  and  print
	Repeat  this  process  for  infinite  times
# End  of  the  function
How  to  create  two  threads  
How  to  start  them
'''
from threading import Thread
from queue import Queue
from random import randint
import time
def f1(q):
    while True:
        n = randint(1, 100)
        q.put(n)
        print('Produced:', n)
        time.sleep(2)
def f2(q):
    while True:
        n = q.get()
        print('Consumed:', n)
q = Queue()
p = Thread(target=f1, args=(q,))
c = Thread(target=f2, args=(q,))
p.start()
c.start()

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

def   roman_arabic(roman):
		How  to  return  arabic  equivalent  of  roman  number
# End  of  the  function	
roman = input('Enter  roman  number  :   ') 
How  to   call  roman_arabic()  function
print('Arabic  equivalent :  ' , ???)
'''

def roman_arabic(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    total = 0
    prev = 0
    for ch in roman[::-1]:
        value = d[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total
roman = input('Enter roman number: ')
print('Arabic equivalent:', roman_arabic(roman))