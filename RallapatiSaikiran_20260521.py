# Find  outputs   (Home  work)
try:
	print('Outer   try')
	try:
		print('Inner    try')
		print(7 / 0)   
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
Outer   try
Inner    try
ZDE   of   inner   try
Inner  try  finally
ValueError  of  outer  try
Outer  try  finally
End  of  outer  try
'''

#  Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd')  
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End of outer try')
'''
Outer  try
Inner  try
ValueError  of  inner  try 
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try
'''

#  Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		'Hyd'[3]  
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End  of  outer  try')
'''
Outer  try
Inner  try  finally
IndexError  of  outer  try
Outer try finally
End  of  outer  try
'''
#  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		eval('Hyd') 
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
Outer  try
Inner  try  finally
default  except  of  outer  try
Outer  try  finally
End  of  outer  try
'''

# Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		print(10 + '20')  
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
Outer  try
Inner  try  finally
default  except  of  outer  try
Outer  try  finally
End  of  outer  try
'''

# Find  outputs   (Home  work)
class   MyError:
	def   _init_(self , y):
		self . a = y
		print('Constructor')
# End  of  the  class
def  compute(x):
		print(x)  
		if  x > 20:
			raise   MyError(x)
		print('Hello') 
# End  of  the function
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')
'''
10
Hello
30
Caught  MyError  outside  :   <__main__.MyError object at 0x...>
End
'''
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
	compute(30) 
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')
'''
30
Caught  MyError  outside  :   
End
'''

# Find  outputs (Home  work)
try:
	print(1)
	print(2)
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)
'''
30
Caught  MyError  outside  :   
End
'''

# Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0) 
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)
'''
1
4
6
7
'''

# Find  outputs   (Home  work)
try:
	print(1) 
	print(7 / 0) 
	print(3)
except:
	int('Two')  
else:
        print(5)
finally:
        print(6)
print(7)
'''
1
6
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: 'Two'
'''
# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
a . m1()
for  i  in  range(10):
	print('main  thread')
'''
child  thread
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
'''	

# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread')
'''
child  thread
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
'''		

#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(How  to  specify  the  target  as  m1  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
'''
Child  Thread  :  1
Main  Thread  :  1
Child  Thread  :  2
Main  Thread  :  2
Main  Thread  :  3
Child  Thread  :  3
Main  Thread  :  4
Child  Thread  :  4
...
Child  Thread  :  10
Main  Thread  :  10
'''		
# Find  outputs  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()
for  i  in  range(10):
        print('main  thread')
'''
AttributeError: 'Thread' object has no attribute 'start'
'''		

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
new = MyThread() 
new . start()  
for  i  in  range(10):
	print('Main  Thread')
'''
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
'''	

# Find  outputs (Home  work)
from  threading  import *
class  MyThread(Thread):
	def   walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')        
'''
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
'''





















