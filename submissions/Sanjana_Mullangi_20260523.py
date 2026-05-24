'''
Tricky  program
1) What  are  the  outputs  for  t1 . start() ?  --->10 times 'f1  function'  

2) What  are  the  outputs  for  t2 . start() ?  --->10 times 'm1  method  of  class  c1' 

3) What  are  the  outputs  for  t3 . start() ?  --->Empty run method of Thread Class

4) What  are  the  outputs  for  t4 . start() ?  --->10 times 'run   method  of  MyThread  class'

5) What  are  the  outputs  for  t5 . start() ?  --->10 times 'run   method  of  MyThread  class'

6) What  are  the  outputs  for  t6 . start() ?  --->10 times 'f1  function'

7) What  are  the  outputs  for  t7 . start() ?  --->Empty run method of Thread class

8) What  are  the  outputs  for  t8 . start() ?  --->10 times 'run   method  of  MyThread  class'

9) What  are  the  outputs  for  t9 . start() ?  --->10 times 'm1  method  of  class  c1'

10) What  are  the  outputs  for  t10 . start() ?  --->10 times 'run   method  of  MyThread  class'

11) What  are  the  outputs  for  t11 . start() ?  --->Empty run method of Thread class

12) What  are  the  outputs  for  t12 . start() ?  --->10 times 'm1  method  of  MyThread  class'

13) What  are  the  outputs  for  t13 . start() ?  --->10 times 'f1  method  of  class  c1'
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
#t1 . start()  #  What  does  thread  t1  do ?
#t2 . start()  #  What  does  thread  t2  do ?
#t3 . start()   #  What  does  thread  t3  do ?
#t4 . start()   #  What  does  thread  t4  do ?
#t5 . start()   #  What  does  thread  t5  do ?
#t6 . start()  #  What  does  thread  t6  do ?
#t7 . start() #  What  does  thread  t7  do ?
t8 . start()   #  What  does  thread  t8  do ?
#t9 . start()   #  What  does  thread  t9  do ?
#t10 . start()  #  What  does  thread  t10  do ?
#t11 . start()   #  What  does  thread  t11  do ?
#t12 . start()  #  What  does  thread  t12  do ?
#t13 . start()   #  What  does  thread  t13  do ?



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
Run Method
Start Method
Main  Thread
'''


# Find  outputs (Home  work)
from   threading  import  *
main = current_thread() 
print(main.name)#How  to  print  name  of  main  thread
main.name='Hyd'#How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name)#How  to  print  new  name  of  main  thread
t = Thread(target=f1(), name='Sec')
t.start()#How  to  create  a  new  thread  with  name  "Sec"
print(main.name)#How  to  print  name  of  new  thread
main.name='Cyb'#How  to  modify  name  of  new  thread  to   'Cyb'
print(main.name)#How  to  print  new  name  of  new  thread
print(active_count())#How  to  print  number  of  threads  under  execution


# Find  outputs (Home  work)
from  threading  import  *
def f1():
    print(current_thread().name)
t1 = Thread(target=f1, name="A")
t2 = Thread(target=f1, name="B")
t3 = Thread(target=f1, name="C")#How  to  create  three  threads  t1 , t2 , t3
print('Default  names  of  the  threads')
t1.start()
t2.start()
t3.start()#How  to  print  name  of  each  thread
t1.name = "One"
t2.name = "Two"
t3.name = "Three"#How  to  modify  name  of  each  thread  to  'One' ,  'Two'   and   'Three'
print('New  names  of  the  threads')
print(t1.name)
print(t2.name)
print(t3.name)#How  to  print  name  of  each  thread
print(active_count())#How  to  print  number  of  threads  under  execution


# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread().name)#How  to  print  name  of  child  thread
child=Thread(target=f1,name="child")#How  to  create  a  new  thread  with  name  'child'  and  target  f1
child.start()#How  to  start  the  new  thread
print(main_thread().name)#How  to  print  name  of   main  thread


# Find  outputs (Home  work)
from  threading  import  *
def f1():
    print(current_thread().name)
t1=Thread(target=f1,name="Hyd")#How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread(target=f1,name="")#How  to  create  another  thread  t2  without  a  name
t1.start()
t2.start()
print(main_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
main_thread().name="India"#How  to  modify  name  of  main  thread  to  'India'
t1.name="Sec"#How  to  modify  name  of  thread  t1  to  'Sec'
t2.name="Cyb"#How  to  modify  name  of  thread  t2  to  'Cyb'
print(main_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
print(active_count())#How  to  print  number  of  threads  under  execution


# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name 
	while   True: 
		print(s , ' : ' , x)
# End  of  the  function
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()   
t2 . start()  
print(active_count())  
print('Press  ctrl + break  or  Fn + b  to  stop ')
'''
infinite loop-while is always True and main thread executes both the threads
'''


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
'''
two threads are executed and random integers are choosen '''