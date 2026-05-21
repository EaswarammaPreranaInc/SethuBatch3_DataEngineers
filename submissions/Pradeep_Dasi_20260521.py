# Find  outputs   (Home  work)
try:
	print('Outer   try')#Outer   try
	try:
		print('Inner    try')#Inner    try
		print(7 / 0)  #error raised 
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')#ZDE   of   inner   try
		int('Ten')#type error raised by inner try suite
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')#ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')#Outer  try  finally
print('End  of  outer  try')#End  of  outer  try



#  Find outputs   (Home  work)
try:
	print('Outer  try')#Outer  try
	try:
		print('Inner  try')#Inner  try
		int('Hyd') #type error is raised  
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')#default except of outer try
finally:
	print('Outer try finally')#Outer try finally
print('End of outer try')#End of outer try

#  Find outputs   (Home  work)
try:
	print('Outer  try')#Outer  try
	try:
		print('Inner  try')#Inner  try
		'Hyd'[3]  #syntax error 
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')
except:
	print('default except of outer try')#default except of outer try
finally:
	print('Outer try finally')#Outer try finally
print('End  of  outer  try')#End  of  outer  try

#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer  try
	try:
		print('Inner  try')#Inner  try
		eval('Hyd')#value error is raised  
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')#ValueError  of   inner  try
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End of inner try')#End of inner try
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')#Outer  try  finally
print('End  of  outer  try')#End  of  outer  try

#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer  try
	try:
		print('Inner  try')#Inner  try
		print(10 + '20') #type error is raised by inner try suite 
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')#Outer  try  finally   
print('End  of  outer  try')

### i.e. error is reported and abnormal termination.

# Find  outputs   (Home  work)
class   MyError:
	def   _init_(self , y):
		self . a = y
		print('Constructor')
# End  of  the  class
def  compute(x):
		print(x)  
		if  x > 20:
			raise   MyError(x)# error becoz  there is no MyError error class , there is regular python class  MyError
		print('Hello') 
# End  of  the function
try:
	compute(10)#10<nxtline>Hello
	compute(30)#30 <nxtline>  abnormal termination 
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')


# Find  outputs   (Home  work)
class   MyError(NameError):
	def    _init_(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()
	print('Hello')
# End  of  the  function
try:
	compute(30) #30 <nxtline>   Caught  MyError  outside  :  "" <nxtline>End
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')




# Find  outputs (Home  work)
try:
	print(1)#1
	print(2)#2
	print(3)#3
except:
	print(4)
else:
	print(5)#5
finally:
	print(6)#6
print(7)#7

 # Find  outputs   (Home  work)
try:
	print(1)#1
	print(7 / 0) #error raised control moved to except suite
	print(3)
except:
	print(4)#4
else:
	print(5)
finally:
	print(6)#6
print(7)#7



 # Find  outputs   (Home  work)
try:
	print(1) #1
	print(7 / 0) #error raised control moved to except suite
	print(3)
except:
	int('Two')  #type error raised but not caught
else:
        print(5)
finally:
        print(6)#6
print(7)




 # Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
a . m1() # prints  10 times-----> 'child  thread'
for  i  in  range(10):
	print('main  thread')#'prints  10 times-----> main  thread'

# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()#child  thread is executed 10 times vary from run to run based on thread sheaduler time
for  i  in  range(10):
        print('main  thread')#main  thread  is executed 10 times vary from run to run based on thread sheaduler time


#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target=c1.m1)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
		# outputs are:
        #     Child  Thread  :   1
        #     Main  Thread  :   1
        #     Main  Thread  :   2
        #     Main  Thread  :   3
        #     Main  Thread  :   4
        #     Main  Thread  :   5
        #     Main  Thread  :   6
        #     Main  Thread  :   7
        #     Main  Thread  :   8
        #     Main  Thread  :   9
        #     Main  Thread  :   10
        #     Child  Thread  :   2
        #     Child  Thread  :   3
        #     Child  Thread  :   4
        #     Child  Thread  :   5
        #     Child  Thread  :   6
        #     Child  Thread  :   7
        #     Child  Thread  :   8
        #     Child  Thread  :   9
        #     Child  Thread  :   10





# Find  outputs  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()#error ther is no start methos in the Thread class of user defined class
for  i  in  range(10):
        print('main  thread')


 # Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()# onj is created for the imported thread class 
t . start()#default target isthe run method of thread class
for  i  in  range(10):
        print('Main  Thread')#10 times ---->    Main  Thread

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
# End  of  the  class
child = MyThread()
child .  run()#10 times ---->   child  thread
for  i  in  range(10):
        print('main  thread')#10 times ---->main  thread

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')#run method
def  f1():
	print('f1  function')
new = MyThread(target = f1)
new . start()#  run  method
print('Main  Thread')#Main  Thread

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(10):
		print('f1  function')
new = MyThread(target = f1) 
new . start()   
for  i  in  range(10):
	print('Main  Thread')


        # outputs : this vary from run to run:
        # f1  function
        # Main  Thread
        # Main  Thread
        # Main  Thread
        # Main  Thread
        # Main  Thread
        # Main  Thread
        # f1  function
        # f1  function
        # f1  function
        # f1  function
        # Main  Thread
        # Main  Thread
        # Main  Thread
        # f1  function
        # Main  Thread
        # f1  function
        # f1  function
        # f1  function
        # f1  function

 # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
new = MyThread() 
new . start()  
for  i  in  range(10):
	print('Main  Thread')#Main  Thread---->printed 10 times(same for every run)

 # Find  outputs (Home  work)
from  threading  import *
class  MyThread(Thread):
	def   walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')#Main  Thread---->printed 10 times(same for every run)