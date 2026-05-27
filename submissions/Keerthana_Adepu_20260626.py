#1
'''
Modify  following  program  such  that  child  thread  should  wait  for  main  thread  expiry
from threading import *
def   disp():  	
	for  i  in  range(10):
		print('new  thread')
# End  of  the  function		
child = Thread(target = disp)
child . start()
for  i  in  range(10):
	print('main  thread')
	'''
from threading import *
def disp():
	main_thread.join()   
	for i in range(10):
		print('child thread')
main_thread = current_thread()
child = Thread(target=disp)
child.start()
for i in range(10):
	print('main thread')
'''
10 times main thread
10 times child thread
outputs are same for every run
'''



#2
'''
Modify  following   program  such  that  t1  should  execute  double()  function  and
t2  should  execute  square()  function
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
#  End  of  the  function
start = time . time()
double()
square()
end = time . time()
print(end - start)
'''
from threading import *
import time
def double():
	for i in range(1 , 7):
		print('Double :' , 2 * i)
		time . sleep(1)
def square():
	for i in range(1, 7):
		print('Square :', i * i)
		time . sleep(1)
start = time . time()
t1 = Thread(target = double)
t2 = Thread(target = square)
t1 . start()
t2 . start()
t1 . join()
t2 . join()
end = time . time()
print(end - start)
'''
double() and square() execute concurrently
output order can't be predicted
outputs are different for each run
end - start = 6 . some seconds
'''



# Find  outputs (Home  work)
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '') 
	time . sleep(3)
	print(']')  
# End  of  the  function
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()  
t2 . start() 
t3 . start()
'''
[ Hyd[ Sec[ Cyb]
]
]
outputs are same for every run
'''

#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    _init_(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def    credit(self , amt):
		s = current_thread() . name 
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')
		x = self . bal 
		time . sleep(1)
		self . bal  =  x  +  amt  
# End  of  the  class
ac = Account(25 , 1000.0)
print('Initial  Balance :  ' , ac . bal)  
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama')
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start()  
t2 . start() 
t1 . join() 
t2 . join()
print('Final  Balance  :   ' , ac . bal)
'''
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100  into account   25
Sita  is  depositing  Rs. 200  into account   25
Final  Balance  :    1200.0
or
Initial Balance : 1000.0
Sita is depositing Rs. 200 into account 25
Rama is depositing Rs. 100 into account 25
Final Balance : 1100.0
'''

#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked')
r . acquire()
print('Locked')
r . release()
print('Unlocked')
r . release()
print('Unlocked')
r . release()    # error , because the lock is already open we can't open already opened object
print('End')
'''
Locked
Locked
Unlocked
Unlocked
End
'''

# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked')
l . acquire() 
print('Locked')
l . release()
print('Unlocked')
l . release()
print('Unlocked')
print('End')
'''
Locked
'''
