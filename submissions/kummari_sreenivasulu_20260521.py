'''
# 1) Find  outputs   (Home  work)
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
print('End  of  outer  try')  # Outer try <nextline> Inner try <nextline> ZDE of inner try <nextline> Inner try finally <nextline> ValueError of outer try <nextline> Outer try finally <nextline> End of outer try
'''
'''
2) #  Find outputs   (Home  work)
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
print('End of outer try')  # Outer try <nextline> Inner try <nextline> ValueError of inner try <nextline> Inner try finally <nextline> End of inner try <nextline> Outer try finally <nextline> End of outer try
'''
'''
3) #  Find outputs   (Home  work)
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
print('End  of  outer  try')  # Outer try <nextline> Inner try <nextline> Inner try finally <nextline> IndexError of outer try <nextline> Outer try finally <nextline> End of outer try
'''
'''
4) #  Find  outputs (Home  work)
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
print('End  of  outer  try')  # Outer try <nextline> Inner try <nextline> Inner try finally <nextline> default except of outer try <nextline> Outer try finally <nextline> End of outer try
'''
'''
5) #  Find  outputs (Home  work)
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
print('End  of  outer  try')  # Outer try <nextline> Inner try <nextline> Inner try finally <nextline> Outer try finally <nextline> TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
'''
6) # Find  outputs   (Home  work)
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
print('End')  # Constructor <nextline> TypeError: exceptions must derive from BaseException
'''
'''
7) # Find  outputs   (Home  work)
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
print('End')  # 30 <nextline> Constructor <nextline> Caught MyError outside : <nextline> End
'''
'''
8) # Find  outputs (Home  work)
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
print(7)  # 1 <nextline> 2 <nextline> 3 <nextline> 5 <nextline> 6 <nextline> 7
'''
'''
9) # Find  outputs   (Home  work)
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
print(7)  # 1 <nextline> 4 <nextline> 6 <nextline> 7
'''
'''
10) # Find  outputs   (Home  work)
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
print(7)  # 1 <nextline> 6 <nextline> ValueError: invalid literal for int() with base 10: 'Two'
'''
'''
11) # Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
a . m1()
for  i  in  range(10):
	print('main  thread') # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
12) # Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread') # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
13) #  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(How  to  specify  the  target  as  m1  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i) # Child Thread : 1 to 10 and Main Thread : 1 to 10 outputs may come in any order
'''
'''
14) # Find  outputs  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()
for  i  in  range(10):
        print('main  thread') # AttributeError: 'Thread' object has no attribute 'start'
'''
'''
15) # Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread') # Main Thread outputs may come along with Child Thread outputs in any order
'''
'''
16) # Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
# End  of  the  class
child = MyThread()
child .  run()
for  i  in  range(10):
        print('main  thread') # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
17) # Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
# End  of  the  class
child = MyThread()
child .  run()
for  i  in  range(10):
        print('main  thread') # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
18) # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
new = MyThread(target = f1)
new . start()
print('Main  Thread') # run method <nextline> Main Thread
'''
'''
19) # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(10):
		print('f1  function')
new = MyThread(target = f1) 
new . start()   
for  i  in  range(10):
	print('Main  Thread') # f1 function and Main Thread outputs may come in any order
'''
'''
20) # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(10):
		print('f1  function')
new = MyThread(target = f1) 
new . start()   
for  i  in  range(10):
	print('Main  Thread') # f1 function and Main Thread outputs may come in any order
'''
'''
21) # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
new = MyThread() 
new . start()  
for  i  in  range(10):
	print('Main  Thread') # Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread
'''
'''
22) # Find  outputs (Home  work)
from  threading  import *
class  MyThread(Thread):
	def   walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')  # Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread <nextline> Main Thread
'''