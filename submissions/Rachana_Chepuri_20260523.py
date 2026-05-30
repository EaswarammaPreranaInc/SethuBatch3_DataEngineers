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
t1 . start()  #  What  does  thread  t1  do ?#10 time  'f1  function' , same for every run ---> f1  function <nxt>f1  function<nxt>f1  function.........<nxt>f1  function
t2 . start()  #  What  does  thread  t2  do ?#10 time  'm1  method  of  class  c1'
#t3 . start()   #  What  does  thread  t3  do ?# executes empty run method of thread class therefore no outputs 
t4 . start()   #  What  does  thread  t4  do ?#10 times prints  ,  run   method  of  MyThread  class
t5 . start()   #  What  does  thread  t5  do ?#10 times prints  ,  run   method  of  MyThread  class
t6 . start()  #  What  does  thread  t6  do ?#10 times prints ,f1  method  of  class  c1
t7 . start() #  What  does  thread  t7  do ?# executes empty run method of thread class therefore no outputs
t8 . start()   #  What  does  thread  t8  do ?##10 times prints  ,  run   method  of  MyThread  class.
t9 . start()   #  What  does  thread  t9  do ?##10 times printed ,m1  method  of  class  c1 
t10 . start()  #  What  does  thread  t10  do ?#10 times printed , run   method  of  MyThread  class
t11 . start()   #  What  does  thread  t11  do ?#executes empty run method of thread class therefore no outputs 
t12 . start()  #  What  does  thread  t12  do ?#10 times  printed --->   m1  method  of  class  c1
t13 . start()   #  What  does  thread  t13  do ?# 10 times  printed --->  f1  method  of  class  c1



''' What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)'''
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
# End  of  the  class		
child = MyThread()
child . start()#Run Method <nxtline> Start Method
print('Main  Thread')#Main  Thread


''' Find  outputs (Home  work)'''
from   threading  import  *
main = current_thread() 
print(current_thread())#How  to  print  name  of  main  thread
main.name = "Hyd"# How  to  modify  name  of  main  thread  to   'Hyd'
print("New main thread name :", main.name)# How  to  print  new  name  of  main  thread
t = Thread(name="Sec")# How  to  create  a  new  thread  with  name  "Sec"
print("New thread name :", t.name)# How  to  print  name  of  new  thread
t.name = "Cyb"# How  to  modify  name  of  new  thread  to   'Cyb'
print("Modified new thread name :", t.name)# How  to  print  new  name  of  new  thread
print("Number of threads :", active_count())# How  to  print  number  of  threads  under  execution



''' Find  outputs (Home  work)'''
from  threading  import  *
t1=Thread()# How  to  create  three  threads  t1 , t2 , t3
t2=Thread()
t3=Thread()
print('Default  names  of  the  threads')
print("name_t1_thread:",t1.name)
print("name_t2_thread:",t2.name)
print("name_t3_thread:",t3.name)# How  to  print  name  of  each  thread
t1.name="One"# How  to  modify  name  of  each  thread  to  'One' ,  'Two'   and   'Three'
t2.name="Two"
t3.name="Three"
print('New  names  of  the  threads')
print("name t1 thread after modification:",t1.name)
print("name t2 thread after modification:",t2.name)
print("name t3 thread after modification:",t3.name)# How  to  print  name  of  each  thread
print("number of threads under execution :",active_count())# How  to  print  number  of  threads  under  execution


''' Find  outputs (Home  work)'''
from  threading  import  *
def  f1():
	print(current_thread())#How  to  print  name  of  child  thread)
t=Thread(target=f1,name="child")#How  to  create  a  new  thread  with  name  'child'  and  target  f1
t.start()#How  to  start  the  new  thread
print(current_thread())#How  to  print  name  of   main  thread)

''' Find  outputs (Home  work)'''
from  threading  import  *
t1=Thread(name='Hyd')#How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread()#How  to  create  another  thread  t2  without  a  name
print(main_thread)#How  to  print  name  of  main  thread)
print("name  of  thread  t1",t1.name)
print("name  of  thread  t2",t2.name)
current_thread.name="India"#How  to  modify  name  of  main  thread  to  'India'
t1.name='Sec'#How  to  modify  name  of  thread  t1  to  'Sec'
t2.name='Cyb'#How  to  modify  name  of  thread  t2  to  'Cyb'
print("name  of  main  thread:",current_thread)
print("name  of  thread  t1:",t1.name)
print("name  of  thread  t2:",t2.name)
print("number  of  threads  under  execution:",active_count())

''' Find  outputs  (Home  work)'''
from  threading  import  *
def   f1(x):
	s = current_thread() . name 
	while   True: 
		print(s , ' : ' , x)
# End  of  the  function
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()  # s :10
t2 . start()  #s :20
print(active_count())  #1
print('Press  ctrl + break  or  Fn + b  to  stop ')

'''Find  outputs (Home  work)'''
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


# output:

# output vary from run to run 
# for sita n is 50 and for Rama n is 75  if  x == n  for any of the thread t1 or t2 ,the execution stops there .
# t1---starts  and t2--- starts ,t1---starts  and t2--- starts .... they work on round robin based .
# Rama  guess  55   in  attempt  :  1
# Rama  guess  45   in  attempt  :  2
# Rama  guess  43   in  attempt  :  3
# Rama  guess  12   in  attempt  :  4
# Sita  guess  89   in  attempt  :  1
# Sita  guess  46   in  attempt  :  2
# Sita  guess  62   in  attempt  :  3
# Sita  guess  49   in  attempt  :  4
# Rama  guess  55   in  attempt  :  5
# .....
# ...
# .....
# .....
# ...
# .....
# .....
# ...
# .....
# Sita  guess  90   in  attempt  :  174
# Sita  guess  52   in  attempt  :  175
# Sita  guess  71   in  attempt  :  176
# Sita  guess  50   in  attempt  :  177
# Sita  finish  in  177  attempts