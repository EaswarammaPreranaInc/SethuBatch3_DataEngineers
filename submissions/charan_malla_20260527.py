'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
	l.acquire()
	print('[' , s , end = '')  
	time . sleep(3)
	l.release()
	print(' ]')
# End  of  the  function
l = Lock()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread().join(10)
	for  i  in  range(10):
		print('child  thread')
# End  of  the  function		
child = Thread(target = disp)
child . start()
for  i  in  range(10):
	print('main  thread')
	time . sleep(3)
'''
main  thread
main  thread
main  thread
main  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''
	
#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()  
	for  i  in  range(10):
		print('child  thread')
# End  of  the  function		
child = Thread(target = disp)
child . start()
child . join()  
for  i  in  range(10):
	  print('main  thread') # Deadlock situation no output 

	  
'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from  threading  import  *
import  time
class   Account:
	def  _init_(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
		l.acquire()
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal    
		time . sleep(1)
		self . bal = x + amt
		l . release() 
#  End  of  the  class	
l = Lock()
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()  
t2 . start() 
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)


#  Object   ac   --->

#  Find  outputs (Home  work)
from threading import *
import time
def   f1():
        sem . acquire() 
        name = current_thread() . name
        print(name , 'is   under   execution')
        time . sleep(1)
        print(name , 'finished  execution')
        sem . release()
# End  of  the  function
sem = Semaphore(3)
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1 . start()
t2 . start()
t3 . start()
t4 . start()
t5 . start()
t6 . start()
t7 . start()
t8 . start()
t9 . start()
'''
Lock is acquired  by  three threads  at  a  time because of Semaphore value is 3
Remaining threads wait until semaphore is released 
output varies  because of  scheduling of threads by OS
'''

#  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem . acquire()
	if   n  >  0:
		x = n * fact(n - 1)
	else:
		x = 1
	sem . release()
	return   x
# End of the function
def    disp(n):
	print(n , ' != ' , fact(n))
# End of the function
sem = Semaphore()
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1 . start()
t2 . start() # Deadlock situation because of recursive call of fact() function and 
             #semaphore is not released until the last call of fact() function is completed

#  Find  outputs  (Home  work)
from  threading  import  *
import  time
def  f1():
	l1 . acquire()  
	print('1st  thread  locks  object  l1')
	time . sleep(1)
	l2 . acquire() 
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():
	l2 . acquire()  
	print('2nd   thread  locks  object  l2')
	time . sleep(1)
	l1 . acquire()  
	print('2nd   thread  is  under  execution')
	l1 . release()
	l2 . release()
	print('End  of  the  2nd   thread')
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1 . start()
t2 . start()
time . sleep(1)
print('Deadlock') # first thread locks l1 and second thread locks l2 hence deadlock situation occurs

#  Find  outputs  (Home  work)
#How  to  insert  10 , 20 , 30 , 40 , 50  into  Queue  object   with  for  loop
print('Deleted  elements')
#How  to  remove  each  element  of  Queue  object  and  also  print
print(active_count()) 
print(q . get())  
print('End')
'''
from  threading  import *
from  queue  import  Queue
from threading import *
q = Queue()
for i in range(10, 60, 10):
    q.put(i)
    print('Deleted  elements')
    while not q.empty():
        print(q.get(i))
print(active_count()) 
print(q . get())  
print('End')
'''

#  Find  outputs  (Home  work)
How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')
'''
from  queue  import  LifoQueue
stack = LifoQueue()
for i in range(10, 60, 10):
    stack.put(i)
    print('Deleted  elements')
    while not stack.empty():
        print(stack.get())
print(stack . get())  
print('End')
'''

#  Find  outputs  (Home  work)
How  to  insert  5  random  elements  into  priority  queue
print('Deleted  elements')
How  to  remove  each  element  of  object  pq  and  also  print
print(pq . get())  
print('End')
'''
from  queue  import  PriorityQueue
from random import randint
pq = PriorityQueue()	
for i in range(5):
    pq.put(randint(1, 100))
    print('Deleted  elements')
    while not pq.empty():
        print(pq.get())
print(pq . get())  
print('End')
'''

# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not q.empty(): # How  to  remove  each  tuple  of  object  'q'  and  also  print
    print(q.get())
'''
('Hyd', 10)
('Delhi', 20)	
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)
'''

#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty(): # How  to  remove  each  tuple  of  object  'stack'  and  also  print
    print(stack.get())

#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty(): # How  to  remove  each  tuple  of  object  'pq'  and  also  print
	print(pq.get())
'''
('Pune', 5)
('Hyd', 10)
('Mumbai', 12)
('Chennai', 15)
('Delhi', 20)
'''

# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty():   #How  to  remove  each  tuple  of  object  'q'  and  also  print
    print(pq.get())
'''
Deleted tuples
('Hyd', 5)	
('Hyd', 10)
('Hyd', 12)
('Hyd', 15)
('Hyd', 20)
'''

#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()   
print(main . daemon) 
main . daemon = True  
child = Thread(target = f1)
print(child . daemon)  
child . daemon = True
print(child . daemon) 
child . start()
child . daemon = True
time . sleep(5)  
print('End  of  main  thread') 
'''
Error because main thread cannot be daemon thread and 
after starting child thread we cannot change its daemon property
'''

'''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread
'''
from  threading  import  *
def    f1():
	name = current_thread() . name
	for  i  in  range(1 , 11):
			print(name , ' : ' , i)
	print(name , 'is  dead')
#  End  of  the  function
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t3 . daemon = True
t1 . start()
t2 . start()
t3 . start()
print('main  thread  is  dead')
'''
One : Output varies because of scheduling of threads by OS
Two : Output varies because of scheduling of threads by OS
Three : Output varies because of scheduling of threads by OS
main  thread  is  dead
One : Output varies because of scheduling of threads by OS
Two : Output varies because of scheduling of threads by OS
Three : Output varies because of scheduling of threads by OS
One is  dead
Two is  dead
Three is  dead
'''
