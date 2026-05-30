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
    
    
    
'''child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread'''





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
    
    
    
'''child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
child  thread
child  thread
child  thread
child  thread
child  thread'''





# Find  outputs (Home work)
from  threading  import  *
main = main_thread()  
name  =  main . name  
print(name , ' is started') # MainThread  is started
main . join() # Error
print(name , 'is ended')