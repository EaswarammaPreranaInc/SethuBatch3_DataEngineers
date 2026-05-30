 # How  to  resolve  deadlock ?
from  threading  import  *
import  time
def  f1():
	l1 . acquire() 
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
#  End  of  the  function
def  f2():
	l1 . acquire()  
	time . sleep(1)
	l2 . acquire()
	print('2nd   thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  2nd   thread')
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1 . start()#1st  thread  is  under  execution <nxt>End  of  the  1st  thread
t2 . start()#2nd   thread  is  under  execution #End  of  the  2nd   thread
t1 . join()
t2 . join()
print('End  of  main  thread')
# outputs:
#1st  thread  is  under  execution 
#End  of  the  1st  thread
#2nd   thread  is  under  execution 
#End  of  the  2nd   thread
# End  of  main  thread


# Producer-Consumer  problem
from  threading  import  *
import  time
from  random  import  randint
class  buffer:
	def   store(self ,  y): 
		s = current_thread() . name 
		self . x  =  y
		print(s  ,  'stores' ,  self . x)
	def   ret(self):
		s = current_thread() . name  
		print(s  ,  'retrieves' ,  self . x)
def   f1(buf):
	i = 1
	while  True: 
		buf . store(i) 
		i += 1   
		time . sleep(randint(1 , 4))  
def  f2(buf):
	while  True:
		buf . ret()
		time . sleep(randint(1 , 4))  
# End  of  the  function
buf = buffer()
p  = Thread(target = f1 , name = 'producer' , args = (buf,))
c  = Thread(target = f2 , name = 'consumer' , args = (buf,))
p . start() 
c . start() 
print('Press  ctrl + break  or  Fn+B  to  stop')
# outputs:
# producer stores 1
# consumer retrieves 1
# Press  ctrl + break  or  Fn+B  to  stop
# consumer retrieves 1
# producer stores 2
# ....
# ....
# ....
# ....
# ....
# producer stores n
# consumer retrieves n
# ....
# ....
# ....
# ....
# ....
# Press  ctrl + break  or  Fn+B  to  stop