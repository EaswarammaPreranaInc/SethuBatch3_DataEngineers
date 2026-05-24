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
'''
Output:
t1 ---> f1 function ×10
t2 ---> m1 method of class c1 ×10
t3 ---> No output
t4 ---> run method of MyThread class ×10
t5 ---> run method of MyThread class ×10
t6 ---> f1 function ×10
t7 ---> No output
t8 ---> run method of MyThread class ×10
t9 ---> m1 method of class c1 ×10
t10 ---> run method of MyThread class ×10
t11 ---> No output
t12 ---> m1 method of MyThread class ×10
t13 ---> f1 method of class c1 ×10
'''


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
Output:
Run Method
Start Method
Main Thread
'''

# Find  outputs (Home  work)
from   threading  import  *
main = current_thread() 
print(main.name) #How  to  print  name  of  main  thread)
main.name='Hyd'#How  to  modify  name  of  main  thread  to   'Hyd'
print(main.name) #How  to  print  new  name  of  main  thread
t=Thread(name='Sec')#How  to  create  a  new  thread  with  name  "Sec"
print(t.name)How  to  print  name  of  new  thread
t.name='Cyb'#How  to  modify  name  of  new  thread  to   'Cyb'
print(t.name)#How  to  print  new  name  of  new  thread
#How  to  print  number  of  threads  under  execution
'''
Output:
MainThread
Hyd
Sec
Cyb
'''

# Find  outputs (Home  work)
from  threading  import  *
t1 = Thread()
t2 = Thread()
t3 = Thread() #How  to  create  three  threads  t1 , t2 , t3
print('Default  names  of  the  threads')
print(t1.name)
print(t2.name)
print(t3.name)#How  to  print  name  of  each  thread
t1.name="One"
t2.name="Two"
t3.name="Three" #How  to  modify  name  of  each  thread  to  'One' ,  'Two'   and   'Three'
print('New  names  of  the  threads')
print(t1.name)
print(t2.name)
print(t3.name) #How  to  print  name  of  each  thread
How  to  print  number  of  threads  under  execution

# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread().name)#How  to  print  name  of  child  thread)
t=Thread(target=f1,name='child')#How  to  create  a  new  thread  with  name  'child'  and  target  f1
t.start()#How  to  start  the  new  thread
print(current)thread().name)#How  to  print  name  of   main  thread)


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
Output:
Hyd : 10
Sec : 20
Hyd : 10
Sec : 20
Press  ctrl + break  or  Fn + b  to  stop
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
Output:
Rama guess 21 in attempt : 1
Rama guess 35 in attempt : 2
.
.
.
.
Rama guess 75 in attempt : some attempts
Rama finish in "no. of" attempts
sita guess 11 in attempt : 1
.
.
.
sita guess 50 in attempt : some attempts
Rama finish in "no. of" attempts