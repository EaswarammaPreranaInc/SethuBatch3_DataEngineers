# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('child  thread')
# End  of  the  function
child = Thread(target = disp)
child . start()
child . join()
for  i  in  range(10):
	print('main  thread')
'''
child thread 10 times
main thread 10 times
outputs are same every run
'''



#  Find  outputs (Home  work)
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
	print('main  thread')
'''
child thread 10 times
main thread 10 times
outputs vary every run
'''



# Find  outputs (Home work)
from  threading  import  *
main = main_thread()  
name  =  main . name  
print(name , ' is started') # MainThread is started
main . join()
print(name , 'is ended')



# Find  outputs (Home  work)
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
print(end - start)
'''
Double :  2
Double :  4
Double :  6
Double :  8
Double :  10
Double :  12
Square :  1
Square :  4
Square :  9
Square :  16
Square :  25
Square :  36
time taken to excecute the program
'''



# Find  outputs  (Home  work)
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
print(active_count())
'''
One is started
Two is started
Three is started
One is ended
Two is ended
Three is ended
'''



# Find  outputs  (Home  work)
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
	print(t . name)



# is_alive()  method   demo  program
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
t1 . start() # One is started
t2 . start() # Two is started
t3 . start() # Three is started
print(t1 . is_alive()) # True
print(t2 . is_alive()) # True
print(t3 . is_alive()) # True
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive()) # False
print(t2 . is_alive()) # False
print(t3 . is_alive()) # False



# Find  outputs (Home  work)
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
t2 . start()
'''
7 table is printed until 10
4 table is printed until 10
outputs vary every run
'''
