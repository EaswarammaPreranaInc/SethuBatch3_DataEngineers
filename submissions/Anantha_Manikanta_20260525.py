'''
# 1) Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('child  thread')
# End  of  the  function
child = Thread(target = disp)
child . start()
child . join()
for  i  in  range(10):
	print('main  thread')  # # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
# 2) Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2) 
#  End  of  the  function		
child = Thread(target = disp)
child . start()
child . join(10) 
for  i  in  range(10):
	print('main  thread')  # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread
'''
'''
# 3) Find  outputs (Home work)
from  threading  import  *
main = main_thread()  
name  =  main . name  
print(name , ' is started')
main . join()
print(name , 'is ended')  # MainThread is started <nextline> RuntimeError: cannot join current threa
'''
'''
# 4) Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
start = time . time()
double()
square()
end = time . time()
print(end - start)  # Double : 2 <nextline> Double : 4 <nextline> Double : 6 <nextline> Double : 8 <nextline> Double : 10 <nextline> Double : 12 <nextline> Square : 1 <nextline> Square : 4 <nextline> Square : 9 <nextline> Square : 16 <nextline> Square : 25 <nextline> Square : 36 <nextline> Approximately 12 seconds
'''
'''
# 5) Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
# End  of  the  function
print(active_count())
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())
t1 . start()
t2 . start()
t3 . start()
print(active_count())
t1 . join()
t2 . join()
t3 . join()
print(active_count()) # 1 <nextline> 1 <nextline> One is started <nextline> Two is started <nextline> Three is started <nextline> 4 <nextline> One is ended <nextline> Two is ended <nextline> Three is ended <nextline> 1
'''
'''
# 6) Find  outputs  (Home  work)
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , ' is  started')
	time . sleep(3)
	print(name , '  is  ended')
# End  of  the  function
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
list = enumerate()
for  t  in   list:
	print(t . name)
t1 . join()
t2 . join()
t3 . join()
list = enumerate()
for  t  in  list:
	print(t . name) # One is started <nextline> Two is started <nextline> Three is started <nextline> MainThread <nextline> One <nextline> Two <nextline> Three <nextline> One is ended <nextline> Two is ended <nextline> Three is ended <nextline> MainThread
'''
'''
# 7) is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started')
	time . sleep(3)
	print(name , '   is    ended')
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())  # One is started <nextline> Two is started <nextline> Three is started <nextline> True <nextline> True <nextline> True <nextline> One is ended <nextline> Two is ended <nextline> Three is ended <nextline> False <nextline> False <nextline> False
'''
'''
# 8) Find  outputs (Home  work)
from  threading  import  *
import  time
def   table(n):
	print('Table  :  ' , n)
	for i  in  range(1 , 11):
		print(F'{n}  *  {i}    =   {n * i}')
		time . sleep(1)
#  End  of  the  function		
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start() # Table : 7 and Table : 4 outputs may come in any order <nextline> Tables of 7 and 4 may print simultaneously in any order
'''