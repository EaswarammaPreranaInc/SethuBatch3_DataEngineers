
from  threading  import  *
class  MyThread(Thread):
        def  run(self):
                for  i  in  range(10):
                        print('run   method  of  MyThread  class')
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  MyThread  class')
class  c1(Thread):
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  class  c1')
        def   f1(self):
                 for  i  in  range(10):
                         print('f1  method  of  class  c1')
# end of class
def   f1():
        for  i  in  range(10):
                print('f1  function')
#end of f1 function
t1 = Thread(target = f1)	
t2 = Thread(target = c1() .  m1() 
t3 = Thread()			
t4 = MyThread()			
t5 = MyThread(target = f1)	
t6 = c1(target =  f1)		
t7 = c1()			
t8 = MyThread(target = c1() . m1) 
t9 = c1(target = c1() . m1)	
t10 = MyThread(target = t4 . run) 
t11 = c1(target = t7 . run)	  
t12 = c1(target = t4 . m1)	  
t13 = c1(target = t7 . f1)	 
# Run  with  any  one  of  the  following  stmts
t1 . start() 	#f1 thread executes  f1 function ×10 times 
t2 . start() 	#m1 method of class c1 ×10 times 
t3 . start()	#No output   
t4 . start()	#run method of MyThread class ×10 times   
t5 . start()	#run method of MyThread class ×10 times   
t6 . start()	#f1 function ×10 times  
t7 . start()	#No output 
t8 . start()	#run method of MyThread class ×10 times   
t9 . start()	#m1 method of class c1 ×10 times 
t10 . start()	#run method of MyThread class ×10 times  
t11 . start()	#No output   
t12 . start()	#m1 method of MyThread class ×10 times  
t13 . start()	#f1 method of class c1 ×10 times 





#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()	#starts the new thread new thread excutes run() method
		print('Start Method')	#Start Method
	def   run(self):
		print('Run Method')	#Run Method
# End  of  the  class		
child = MyThread()
child . start()		#creates a new thread and internally calls run() method
print('Main  Thread') 	#Main  Thread




from threading import *

# Current(main) thread object
main = current_thread()

# Print name of main thread
print("Old name of main thread :", main.name)

# Modify name of main thread
main.name = "Hyd"

# Print new name of main thread
print("New name of main thread :", main.name)

# Create new thread with name "Sec"
t = Thread(name="Sec")

# Print name of new thread
print("Old name of new thread :", t.name)

# Modify name of new thread
t.name = "Cyb"

# Print new name of new thread
print("New name of new thread :", t.name)

# Print number of threads under execution
print("Number of threads under execution :", active_count())


#outputs:
Old name of main thread : MainThread
New name of main thread : Hyd
Old name of new thread : Sec
New name of new thread : Cyb
Number of threads under execution : 1





from threading import *

# Create three threads
t1 = Thread()
t2 = Thread()
t3 = Thread()

print("Default names of the threads")

# Print default names
print(t1.name)
print(t2.name)
print(t3.name)

# Modify thread names
t1.name = "One"
t2.name = "Two"
t3.name = "Three"

print("New names of the threads")

# Print new names
print(t1.name)
print(t2.name)
print(t3.name)

# Print number of active threads
print("Number of threads under execution :", active_count())

#outputs:
Default names of the threads
Thread-1
Thread-2
Thread-3

New names of the threads
One
Two
Three

Number of threads under execution : 1





from threading import *

def f1():
    print("Child thread name :", current_thread().name)

# Create new thread with name 'child'
t = Thread(target=f1, name="child")

# Start the thread
t.start()

# Print main thread name
print("Main thread name :", current_thread().name)

#outputs:
Child thread name : child
Main thread name : MainThread





from threading import *

# Create thread t1 with name 'Hyd'
t1 = Thread(name="Hyd")

# Create thread t2 without a name
t2 = Thread()

# Print names
print("Main thread name :", current_thread().name)
print("Thread t1 name   :", t1.name)
print("Thread t2 name   :", t2.name)

# Modify names
current_thread().name = "India"
t1.name = "Sec"
t2.name = "Cyb"

# Print modified names
print("New main thread name :", current_thread().name)
print("New thread t1 name   :", t1.name)
print("New thread t2 name   :", t2.name)

# Print active thread count
print("Number of threads under execution :", active_count())

#outputs:
Main thread name : MainThread
Thread t1 name   : Hyd
Thread t2 name   : Thread-1

New main thread name : India
New thread t1 name   : Sec
New thread t2 name   : Cyb

Number of threads under execution : 1





# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name 	#t1,t2 name:Hyd  name:Sec
	while   True: 
		print(s , ' : ' , x)	#infinite loop prints t1 and t2 alternatively
# End  of  the  function
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))	#thread is created with name and args  f1(10)
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])	#thread is created with name and args  f1(20)
t1 . start()   
t2 . start()  
print(active_count()) 	#3 
print('Press  ctrl + break  or  Fn + b  to  stop ')	#Press  ctrl + break  or  Fn + b  to  stop 



# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name 	#s=Rama s=Sita
	while  True:  
		x = randint(1 , 100)	#loop starts 
		ctr += 1 
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	# End  of  while  loop
	print(F'{s}  finish  in  {ctr}  attempts')
# End  of  the  function
t1 = Thread(target = f1 , args = [75] , name = 'Rama')	#thread is createed
t2 = Thread(target = f1 , args = [50] , name = 'Sita')	#thread is createed
t1 . start() 
t2 . start()
#outputs:
Rama guess 12 in attempt : 1
Sita guess 90 in attempt : 1
Rama guess 75 in attempt : 2
Rama finish in 2 attempts
Sita guess 45 in attempt : 2
Sita guess 50 in attempt : 3
Sita finish in 3 attempts


Sita guess 10 in attempt : 1
Rama guess 60 in attempt : 1
Sita guess 50 in attempt : 2
Sita finish in 2 attempts
Rama guess 75 in attempt : 2
Rama finish in 2 attempts




 