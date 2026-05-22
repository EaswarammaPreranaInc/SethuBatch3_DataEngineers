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
Output:
Outer try
Inner try
ZDE of inner try
Inner try finally
ValueError of outer try
Outer try finally
End of outer try
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
Output:
Outer try
Inner try
ValueError of inner try
Inner try finally
End of inner try
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
Output:
Outer try
Inner try
Inner try finally
IndexError of outer try
Outer try finally
End of outer try
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
Output:
Outer try
Inner try
Inner try finally
default except of outer try
Outer try finally
End of outer try
'''

#  Find  outputs (Home  work)
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
Output:
Outer try
Inner try
Inner try finally
Outer try finally
reports TypeError
'''

# Find  outputs   (Home  work)
class   MyError:
	def   __init__(self , y):
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
Output:
10
Hello
30
Constructor
reports TypeError exceptions must derive from BaseException
'''

# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
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
Output:
30
Constructor
Caught MyError outside : 
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
Output:
1
2
3
5
6
7
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
Output:
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
	int('Two')  # raises ValueError
else:
        print(5)
finally:
        print(6)
print(7)
'''
Output:
1
6
reports ValueError
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
Output:
child thread
(child thread 10 times)
main thread
(main thread 10 times)
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
Output:
child thread
(10 times)
main thread
(10 times)
'''

#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target = c1.m1)#How  to  specify  the  target  as  m1  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
'''
Output:
order varies from execution to exceution
'''

# Find  outputs  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start() # raises AttributeError as 'Thread' object (t) has no attribute 'start'
for  i  in  range(10):
        print('main  thread')

# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')
'''
Output:
Main Thread
(10 times)
'''

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
# End  of  the  class
child = MyThread()
child .  run()
for  i  in  range(10):
        print('main  thread')
'''
Output:
child thread
(10 times)
main thread
(10 times)
'''

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
new = MyThread(target = f1)
new . start()
print('Main  Thread')
'''
Output:
run method
Main Thread
run() method is overridden
'''

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
'''
Output:
f1 function
(10 times)
Main Thread
(10 times)
'''

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
new = MyThread() # default target is run() which does ntg
new . start()  
for  i  in  range(10):
	print('Main  Thread')
'''
Output:
Main Thread
(10 times)
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
Output:
Main Thread
(10 times)
'''