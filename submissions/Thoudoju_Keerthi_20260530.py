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

from threading import Thread
from queue import Queue
import time
def   f1(q):
	i=1
	while True:
		q.put(i)
		time.sleep(1)
		i+=1
def  f2(q):
	while True:
		p=q.get()
		print(p)
		time.sleep(1)
# End  of  the  function
q=Queue()
t1=Thread(target=f1,args=(q,))
t2=Thread(target=f2,args=(q,))
t1.start()
t2.start()



# Write  a  program  to  convert   roman   number  to   arabic  number

# M - 1000
# D - 500
# C - 100
# L - 50
# X - 10
# V - 5
# I - 1

# 1) Input : XIV
#     Reverse  input :   VIX
#     sum = 0 + 5 - 1 + 10 = 14
# 	prev =  10
	
# 2) Input : MCMXC
#     Reverse  input :  CXMCM
#     sum = 0 + 100 - 10 + 1000 - 100 + 1000 = 1990
# 	prev =  1000

# 3) Input : MMXXVI
#     Reverse  string :  
#     sum = 0
# 	prev = 
	
# 4) Input : MCMLXXXIV
#      Reverse  string :  
#     sum = 0
# 	prev = 
	
# 5) Hint : Use  dictionary	
# '''
def   roman_arabic(roman):
	d={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
	r=roman[::-1]
	sum=0
	prev=0
	for i in r:
		if d[i] < prev:
				sum -= d[i]
		else:
			sum+=d[i]
		prev =d[i]
	return sum

# End  of  the  function	
roman = input('Enter  roman  number  :   ') 
arabic =roman_arabic(roman)
print('Arabic  equivalent :  ' , arabic)