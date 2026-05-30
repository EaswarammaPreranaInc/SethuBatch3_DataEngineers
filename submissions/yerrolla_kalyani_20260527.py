'''Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]'''
from  threading  import *
import  time
def   disp(s):
	l.acquire()
	print('[' , s , end = '')  
	time . sleep(3)
	print(' ]')
	l.release()
# End  of  the  function
l=Lock()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

'''Find   outputs (Home  work)'''
from threading import *
import  time
def    disp():
	main_thread() . join(10)
	for  i  in  range(10):
		print('child  thread')
# End  of  the  function		
child = Thread(target = disp)
child . start()
for  i  in  range(10):
	print('main  thread')
	time . sleep(3)

''' Find  outputs  (Home  work)'''
from threading import *
import time
def  disp():
	main_thread() . join()  #child thread waits for the main thread to dead
	for  i  in  range(10):
		print('child  thread') # 10 times  child  thread
# End  of  the  function		
child = Thread(target = disp)
child . start()
child . join()  #  Main thread waits for child thread to dead
for  i  in  range(10):
	  print('main  thread')
	  
'''Modify  following  program  such  that  final  balance  should  be  1300'''
from  threading  import  *
import  time
class   Account:
	def  __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
		self.lock = Lock() 
	def  credit(self , amt): 	 
		s = current_thread() . name
		self.lock.acquire()
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal    
		time . sleep(1)
		self . bal = x + amt
		self.lock.release()
#  End  of  the  class	
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
t1 . start()  
t2 . start() 
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)  
''' Find  outputs (Home  work) '''
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
'''output'''
# One is under execution
# Two is under execution
# Three is under execution

# One finished execution
# Four is under execution

# Two finished execution
# Five is under execution

# Three finished execution
# Six is under execution

# Four finished execution
# Seven is under execution

# Five finished execution
# Eight is under execution

# Six finished execution
# Nine is under execution

# Seven finished execution
# Eight finished execution
# Nine finished execution

'''  Find  outputs'''
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
	print(n , ' != ' , fact(n)) # calling fact function
# End of the function
sem = Semaphore()
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1 . start() # Executes disp(4)
t2 . start() 
'''Find  outputs  (Home  work)'''
from  threading  import  *
import  time
def  f1():
	l1 . acquire()   # locked by t1
	print('1st  thread  locks  object  l1') # 1st  thread  locks  object  l1
	time . sleep(1)
	l2 . acquire() 
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():
	l2 . acquire()    # locked by t2
	print('2nd   thread  locks  object  l2') # 2nd   thread  locks  object  l2
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
t1 . start() # t1 executes f1
t2 . start() # t2 executes f2
time . sleep(1)
print('Deadlock') # Deadlock
''' Find  outputs  (Home  work)'''
from threading import *
from queue import Queue
q = Queue()
for i in range(10, 51, 10):
    q.put(i)
print("Deleted elements")
while not q.empty():
    print(q.get())
print(active_count())
print("End")
''' Find  outputs  (Home  work)'''
from queue import LifoQueue
stack = LifoQueue()
for i in range(10, 51, 10):
    stack.put(i)
print("Deleted elements")
while not stack.empty():
    print(stack.get())
print("End")
'''output'''
# Deleted elements
# 50
# 40
# 30
# 20
# 10
# End
''' Find  outputs  (Home  work)'''
from queue import PriorityQueue
import random
pq = PriorityQueue()
for _ in range(5):
    pq.put(random.randint(1, 100))
print("Deleted elements")
while not pq.empty():
    print(pq.get())
print("End")
'''output'''
# Deleted elements
# 2
# 13
# 14
# 22
# 65
# End
''' Find  outputs  (Home  work)'''
from queue import Queue
q = Queue()
q.put(('Hyd', 10)) # ('Hyd', 10)
q.put(('Delhi', 20)) #('Delhi', 20)
q.put(('Chennai', 15))# ('Chennai', 15)
q.put(('Pune', 5))  #('Pune', 5)
q.put(('Mumbai', 12))  #('Mumbai', 12)
while not q.empty():
    print(q.get())
''' Find  outputs  (Home  work)'''
from queue import LifoQueue
stack = LifoQueue()
stack.put(('Hyd', 10))
stack.put(('Delhi', 20))
stack.put(('Chennai', 15))
stack.put(('Pune', 5))
stack.put(('Mumbai', 12))
while not stack.empty():
    print(stack.get())
'''output'''
# ('Mumbai', 12)
# ('Pune', 5)
# ('Chennai', 15)
# ('Delhi', 20)
# ('Hyd', 10)
''' Find  outputs  (Home  work)'''
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(('Hyd', 10))
pq.put(('Hyd', 20))
pq.put(('Hyd', 15))
pq.put(('Hyd', 5))
pq.put(('Hyd', 12))
print('Deleted tuples')
while not pq.empty():
    print(pq.get())
'''output'''    
# ('Hyd', 5)
# ('Hyd', 10)
# ('Hyd', 12)
# ('Hyd', 15)
# ('Hyd', 20) 
''' Find  outputs (Home  work)'''  
from threading import *
import time
def f1():
    for i in range(10):
        print('child thread')
        time.sleep(2)
main = main_thread()
print(main.daemon)          # Output: False
main.daemon = True          # No effect 
child = Thread(target=f1)
print(child.daemon)         #  False
child.daemon = True
print(child.daemon)         #  True
child.start()
child.daemon = True         # has no effect after start
time.sleep(5)
print('End of main thread') # End of main thread
'''(Home  work)Find  outputs
Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread'''
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
'''output'''
# One : 1
# Two : 1
# Three : 1
# One : 2
# Two : 2
# Three : 2
# One : 3
# Two : 3
# Three : 3
# One : 4
# Two : 4
# Three : 4
# One : 5
# Two : 5
# Three : 5
# main thread is dead
# One : 6
# Two : 6
# One : 7
# Two : 7
# One : 8
# Two : 8
# One : 9
# Two : 9
# One : 10
# Two : 10
# One is dead
# Two is dead