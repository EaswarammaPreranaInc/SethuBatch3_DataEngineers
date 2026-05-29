'''
1) Tricky  program
# 1) What are the outputs for t1.start() ? ---> f1 function

# 2) What are the outputs for t2.start() ? ---> m1 method of class c1

# 3) What are the outputs for t3.start() ? ---> No output

# 4) What are the outputs for t4.start() ? ---> run method of MyThread class

# 5) What are the outputs for t5.start() ? ---> run method of MyThread class

# 6) What are the outputs for t6.start() ? ---> f1 function

# 7) What are the outputs for t7.start() ? ---> No output

# 8) What are the outputs for t8.start() ? ---> run method of MyThread class

# 9) What are the outputs for t9.start() ? ---> m1 method of class c1

# 10) What are the outputs for t10.start() ? ---> run method of MyThread class

# 11) What are the outputs for t11.start() ? ---> f1 function

# 12) What are the outputs for t12.start() ? ---> f1 function

# 13) What are the outputs for t13.start() ? ---> f1 method of class c1'''
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
t1.start() ---> f1 function
t2.start() ---> m1 method of class c1
t3.start() ---> No output
t4.start() ---> run method of MyThread class
t5.start() ---> run method of MyThread class
t6.start() ---> f1 function
t7.start() ---> No output
t8.start() ---> run method of MyThread class
t9.start() ---> m1 method of class c1
t10.start() ---> run method of MyThread class
t11.start() ---> f1 function
t12.start() ---> f1 function
t13.start() ---> f1 method of class c1
'''
'''
2) #  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
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
print('Main  Thread') # Run Method <nextline> Start Method <nextline> Main Thread
'''
'''
3) # Find  outputs (Home  work)
from   threading  import  *
main = current_thread() 
print(How  to  print  name  of  main  thread)  # print(main.name)
How  to  modify  name  of  main  thread  to   'Hyd'  # main.name = 'Hyd'
How  to  print  new  name  of  main  thread  # print(main.name)
How  to  create  a  new  thread  with  name  "Sec"  # child = Thread(name = 'Sec')
How  to  print  name  of  new  thread  # print(child.name)
How  to  modify  name  of  new  thread  to   'Cyb'  # child.name = 'Cyb'
How  to  print  new  name  of  new  thread  # print(child.name)
How  to  print  number  of  threads  under  execution  # print(active_count())
'''
'''
4) # Find  outputs (Home  work)
from  threading  import  *
How  to  create  three  threads  t1 , t2 , t3  # t1 = Thread() <nextline> t2 = Thread() <nextline> t3 = Thread()
print('Default  names  of  the  threads')
How  to  print  name  of  each  thread  # print(t1.name) <nextline> print(t2.name) <nextline> print(t3.name)
How  to  modify  name  of  each  thread  to  'One' ,  'Two'   and   'Three'  # t1.name = 'One' <nextline> t2.name = 'Two' <nextline> t3.name = 'Three'
print('New  names  of  the  rhreads')
How  to  print  name  of  each  thread  # print(t1.name) <nextline> print(t2.name) <nextline> print(t3.name)
How  to  print  number  of  threads  under  execution  # print(active_count())
'''
'''
5) # Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(How  to  print  name  of  child  thread)  # print(current_thread().name)
How  to  create  a  new  thread  with  name  'child'  and  target  f1 # child = Thread(target = f1 , name = 'child')
How  to  start  the  new  thread # child.start()
print(How  to  print  name  of   main  thread)  # print(current_thread().name)
'''
'''
6) # Find  outputs (Home  work)
from  threading  import  *
How  to  create  a  thread  t1  with  name  'Hyd'  # t1 = Thread(name = 'Hyd')
How  to  create  another  thread  t2  without  a  name  # t2 = Thread()
print(How  to  print  name  of  main  thread)  # print(current_thread().name)
print(How  to  print  name  of  thread  t1)  # print(t1.name)
print(How  to  print  name  of  thread  t2)  # print(t2.name)
How  to  modify  name  of  main  thread  to  'India'  # current_thread().name = 'India'
How  to  modify  name  of  thread  t1  to  'Sec'  # t1.name = 'Sec'
How  to  modify  name  of  thread  t2  to  'Cyb'  # t2.name = 'Cyb'
print(How  to  print  name  of  main  thread) # print(current_thread().name)
print(How  to  print  name  of  thread  t1)  # print(t1.name)
print(How  to  print  name  of  thread  t2)  # print(t2.name)
print(How  to  print  number  of  threads  under  execution)  # print(active_count())
'''
'''
7) # Find  outputs  (Home  work)
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
print('Press  ctrl + break  or  Fn + b  to  stop ')  # Hyd : 10 and Sec : 20 outputs may come in any order continuously <nextline> 3 <nextline> Press ctrl + break or Fn + b to stop
'''
'''
8) # Find  outputs (Home  work)
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
t2 . start()  # Rama guess values and Sita guess values may come in any order until they get 75 and 50 respectively <nextline> Rama finish in some attempts <nextline> Sita finish in some attempts
'''