1) Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd] [Sec] [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')  
	time . sleep(3)
	print(' ]')
# End  of  the  function
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

#from  threading  import *
import  time

def   disp(s):
	l.acquire()
	print('[' , s , end = '')  
	time . sleep(3)
	print(' ]')
	l.release()
# End  of  the  function
l = Lock()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()

2) outputs
from threading import *
import  time
def    disp():
	main_thread() . join(10)
	for  i  in  range(10):
		print('child  thread') #10 times child thread
# End  of  the  function		
child = Thread(target = disp)
child . start()
for  i  in  range(10):
	print('main  thread') #10 times main thread
	time . sleep(3)

3) outputs 
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
	  print('main  thread')

4) Modify  following  program  such  that  final  balance  should  be  1300
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
		l.release()
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

5) outputs 
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
t1 . start()#one is under execution
t2 . start()#two is under execution
t3 . start()#three is under execution
t4 . start()#four is under execution
t5 . start()#five is under execution
t6 . start()#six is under execution
t7 . start()#seven is under execution
t8 . start()#eight is under execution
t9 . start()#nine is under execution
if t1 gets chance one finished execution
if t2 gets chance two finished execution
if t3 gets chance three finished execution
if t4 gets chance four finished execution
if t5 gets chance five finished execution
if t6 gets chance six finished execution
if t7 gets chance seven finished execution
if t8 gets chance eight finished execution
if t9 gets chance nine finished execution



6) outputs 
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
t2 . start()

7) outputs 
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
print('Deadlock')

8) outputs 
from queue import Queue
from threading import active_count 
q = Queue() 
for i in [10, 20, 30, 40, 50]:
	q.put(i) #How  to  insert  10 , 20 , 30 , 40 , 50  into  Queue  object   with  for  loop
print('Deleted  elements')
while not q.empty():
	print(q.get()) #How  to  remove  each  element  of  Queue  object  and  also  print
print(active_count())   
print('End')

9) outputs 
from queue import PriorityQueue 
pq = PriorityQueue() 
pq.put(1)
pq.put(2)
pq.put(3)
pq.put(4)
pq.put(5) #How  to  insert  5  random  elements  into  priority  queue
print('Deleted  elements')
while not pq.empty(): #How  to  remove  each  element  of  object  pq  and  also  print
	print(pq . get())  
print('End')

10) outputs 
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get()) #How  to  remove  each  tuple  of  stack  object   and  also  print

11) outputs 
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get()) #How  to  remove  each  tuple  of  object  'q'  and  also  print

12) outputs 
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty():
    print(pq.get()) #How  to  remove  each  tuple  of  object  'q'  and  also  print

13) outputs 
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')#child thread
		time . sleep(2)
main = main_thread()   
print(main . daemon)#False  
main . daemon = True  
child = Thread(target = f1)
print(child . daemon)  #False
child . daemon = True
print(child . daemon) #true
child . start()
child . daemon = True
time . sleep(5)  
print('End  of  main  thread')#end of main thread

14) outputs 
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

15) outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not pq.empty():
	print(q.get()) #How  to  remove  each  tuple  of  object  'q'  and  also  print

16) outputs
from queue import LifoQueue
stack = LifoQueue()
for i in [10, 20, 30, 40, 50]:
	stack.put(i) #How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not stack.empty(): #How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get())
print('End')

