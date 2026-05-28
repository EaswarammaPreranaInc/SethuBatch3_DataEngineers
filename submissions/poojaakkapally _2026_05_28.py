# How  to  resolve  deadlock ?
'''from  threading  import  *
import  time
def  f1():
	l1 . acquire() 
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')#---1   1st  thread  is  under  execution
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')#---2   End  of  the  1st  thread
	# t1 dead       t2 or mainTread gets chance     t2 or MT got chance
#  End  of  the  function
def  f2():
	l1 . acquire() # t2 waits until t1 locks l1 
	time . sleep(1)
	l2 . acquire()
	print('2nd   thread  is  under  execution')#----3 2nd   thread  is  under  execution
	l2 . release()
	l1 . release()
	print('End  of  the  2nd   thread')#4----End  of  the  2nd   thread
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)# 
t1 . start()# 
t2 . start()# 
t1 . join()# M.T waits for t1 expiry
t2 . join()# M.T waits for t2 expiry
print('End  of  main  thread')# 5----- End  of  the  main   thread
'''
# Producer-Consumer  problem
from  threading  import  *
import  time
from  random  import  randint
class  buffer:
	def   store(self ,  y): 
		s = current_thread() . name 
		self . x  =  y
		print(s  ,  'stores' ,  self . x)# 1---producer	stores	1
	def   ret(self):
		s = current_thread() . name  
		print(s  ,  'retrieves' ,  self . x)# 2.---consumer retieves 1
def   f1(buf):
	i = 1
	while  True: 
		buf . store(i) 
		i += 1   
		time . sleep(randint(1 , 4))  # t1 sleeps and mt got chance
def  f2(buf):
	while  True:
		buf . ret()# 2
		time . sleep(randint(1 , 4))  
# End  of  the  function
buf = buffer()
p  = Thread(target = f1 , name = 'producer' , args = (buf,))
c  = Thread(target = f2 , name = 'consumer' , args = (buf,))
p . start() 
c . start() 
print('Press  ctrl + break  or  Fn+B  to  stop')

# Output vary run to run