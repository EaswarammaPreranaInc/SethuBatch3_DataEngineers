'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  --->

2) What  are  the  outputs  for  t2 . start() ?  --->

3) What  are  the  outputs  for  t3 . start() ?  --->

4) What  are  the  outputs  for  t4 . start() ?  --->

5) What  are  the  outputs  for  t5 . start() ?  --->

6) What  are  the  outputs  for  t6 . start() ?  --->

7) What  are  the  outputs  for  t7 . start() ?  --->

8) What  are  the  outputs  for  t8 . start() ?  --->

9) What  are  the  outputs  for  t9 . start() ?  --->

10) What  are  the  outputs  for  t10 . start() ?  --->

11) What  are  the  outputs  for  t11 . start() ?  --->

12) What  are  the  outputs  for  t12 . start() ?  --->

13) What  are  the  outputs  for  t13 . start() ?  --->
'''
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
t2 = Thread(target = c1() . m1)
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
t1 . start()  #  What  does  thread  t1  do ?
#t2 . start()  #  What  does  thread  t2  do ?
#t3 . start()   #  What  does  thread  t3  do ?
#t4 . start()   #  What  does  thread  t4  do ?
#t5 . start()   #  What  does  thread  t5  do ?
#t6 . start()  #  What  does  thread  t6  do ?
#t7 . start() #  What  does  thread  t7  do ?
#t8 . start()   #  What  does  thread  t8  do ?
#t9 . start()   #  What  does  thread  t9  do ?
#t10 . start()  #  What  does  thread  t10  do ?
#t11 . start()   #  What  does  thread  t11  do ?
#t12 . start()  #  What  does  thread  t12  do ?
#t13 . start()   #  What  does  thread  t13  do ?

ANSWER:

'''

1) t1.start()   ---> Executes f1() function
                      Output : "f1 function" 10 times

2) t2.start()   ---> Executes c1().m1()
                      Output : "m1 method of class c1" 10 times

3) t3.start()   ---> Executes default Thread.run()
                      Output : No output

4) t4.start()   ---> Executes overridden run() of MyThread
                      Output : "run method of MyThread class" 10 times

5) t5.start()   ---> MyThread has its own run() method,
                      so target=f1 is ignored
                      Output : "run method of MyThread class" 10 times

6) t6.start()   ---> c1 does not override run(),
                      so target=f1 executes
                      Output : "f1 function" 10 times

7) t7.start()   ---> c1 has no run() method
                      Output : No output

8) t8.start()   ---> MyThread overrides run(),
                      so target=c1().m1 ignored
                      Output : "run method of MyThread class" 10 times

9) t9.start()   ---> c1 uses default Thread.run(),
                      target=c1().m1 executes
                      Output : "m1 method of class c1" 10 times

10) t10.start() ---> MyThread overrides run(),
                      so target=t4.run ignored
                      Output : "run method of MyThread class" 10 times

11) t11.start() ---> target=t7.run
                      t7 is object of c1 which uses default run()
                      No target inside t7
                      Output : No output

12) t12.start() ---> target=t4.m1 executes
                      Output : "m1 method of MyThread class" 10 times

13) t13.start() ---> target=t7.f1 executes
                      Output : "f1 method of class c1" 10 times





#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
# End  of  the  class		
child = MyThread()
child . start()
print('Main  Thread')
'''
OUTPUTS:


Run Method
Start Method
Main Thread



# Find  outputs (Home  work)
from   threading  import  *
main = current_thread() 
print(How  to  print  name  of  main  thread)
How  to  modify  name  of  main  thread  to   'Hyd'
How  to  print  new  name  of  main  thread
How  to  create  a  new  thread  with  name  "Sec"
How  to  print  name  of  new  thread
How  to  modify  name  of  new  thread  to   'Cyb'
How  to  print  new  name  of  new  thread
How  to  print  number  of  threads  under  execution


from threading import *

main = current_thread()

# Print name of main thread
print(main.name)

# Modify name of main thread to 'Hyd'
main.name = 'Hyd'

# Print new name of main thread
print(main.name)

# Create a new thread with name "Sec"
t = Thread(name='Sec')

# Print name of new thread
print(t.name)

# Modify name of new thread to 'Cyb'
t.name = 'Cyb'

# Print new name of new thread
print(t.name)

# Print number of threads under execution
print(active_count())


OUTPUTS:
MainThread
Hyd
Sec
Cyb
1





# Find  outputs (Home  work)
from  threading  import  *
How  to  create  three  threads  t1 , t2 , t3
print('Default  names  of  the  threads')
How  to  print  name  of  each  thread
How  to  modify  name  of  each  thread  to  'One' ,  'Two'   and   'Three'
print('New  names  of  the  rhreads')
How  to  print  name  of  each  thread
How  to  print  number  of  threads  under  execution


from threading import *

# Create three threads
t1 = Thread()
t2 = Thread()
t3 = Thread()

print('Default names of the threads')

# Print names of threads
print(t1.name)
print(t2.name)
print(t3.name)

# Modify names of threads
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'

print('New names of the threads')

# Print new names
print(t1.name)
print(t2.name)
print(t3.name)

# Print number of active threads
print(active_count())


OUTPUTS:

Default names of the threads
Thread-1
Thread-2
Thread-3

New names of the threads
One
Two
Three

1






# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(How  to  print  name  of  child  thread)
How  to  create  a  new  thread  with  name  'child'  and  target  f1
How  to  start  the  new  thread
print(How  to  print  name  of   main  thread)


from threading import *

def f1():
    # Print name of child thread
    print(current_thread().name)

# Create new thread with name 'child' and target f1
t = Thread(target=f1, name='child')

# Start the new thread
t.start()

# Print name of main thread
print(current_thread().name)



OUTPUTS:
child
MainThread




# Find  outputs (Home  work)
from  threading  import  *
How  to  create  a  thread  t1  with  name  'Hyd'
How  to  create  another  thread  t2  without  a  name
print(How  to  print  name  of  main  thread)
print(How  to  print  name  of  thread  t1)
print(How  to  print  name  of  thread  t2)
How  to  modify  name  of  main  thread  to  'India'
How  to  modify  name  of  thread  t1  to  'Sec'
How  to  modify  name  of  thread  t2  to  'Cyb'
print(How  to  print  name  of  main  thread)
print(How  to  print  name  of  thread  t1)
print(How  to  print  name  of  thread  t2)
print(How  to  print  number  of  threads  under  execution)


from threading import *

# Create thread t1 with name 'Hyd'
t1 = Thread(name='Hyd')

# Create another thread t2 without a name
t2 = Thread()

# Print names
print(current_thread().name)
print(t1.name)
print(t2.name)

# Modify names
current_thread().name = 'India'
t1.name = 'Sec'
t2.name = 'Cyb'

# Print modified names
print(current_thread().name)
print(t1.name)
print(t2.name)

# Print number of active threads
print(active_count())


OUTPUTS:
MainThread
Hyd
Thread-1
India
Sec
Cyb
1



# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name 
	while  True:  
		x = randint(1 , 100) 
		ctr += 1 
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	# End  of  while  loop
	print(F'{s}  finish  in  {ctr}  attempts')
# End  of  the  function
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() 
t2 . start()



from threading import Thread, current_thread
from random import randint

def f1(n):
    ctr = 0
    s = current_thread().name

    while True:
        x = randint(1, 100)
        ctr += 1

        print(f'{s} guess {x} in attempt : {ctr}')

        if x == n:
            break

    # End of while loop
    print(f'{s} finish in {ctr} attempts')

# End of function

t1 = Thread(target=f1, args=[75], name='Rama')
t2 = Thread(target=f1, args=[50], name='Sita')

t1.start()
t2.start()
