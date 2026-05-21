1) outputs
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
#Outer  try
Inner  try
ValueError  of  inner  try 
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try

2) outputs
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
#Outer  try
Inner  try
Inner  try  finally
IndexError  of  outer  try
Outer try finally
End  of  outer  try

3) outputs
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
#Outer  try
Inner  try
Inner  try  finally
default  except  of  outer  try
Outer  try  finally
End  of  outer  try

4) outputs
try:
	print('Outer  try')
	try:
		print('Inner  try')
		print(10 + '20')  #Error
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
#Outer  try
Inner  try
Inner  try  finally
Outer  try  finally


5) outputs
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
#10
Hello
30
Error at myerror

6) outputs
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
	print('Caught  MyError  outside  :  ' ,  msg)#'Caught  MyError  outside  :  '
print('End')#End

7) outputs
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

8) outputs
try:
	print(1)#1
	print(7 / 0) 
	print(3)
except:
	print(4)#4
else:
	print(5)
finally:
	print(6)#6
print(7)#7

9) outputs
try:
	print(1) #1
	print(7 / 0) #ZDE
	print(3)
except:
	int('Two') #ValueError 
else:
        print(5)
finally:
        print(6)#6
print(7)

10) outputs
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')  #child thread 10 times
a = c1()
child  = Thread(target = a . m1)
a . m1()
for  i  in  range(10):
	print('main  thread')  #main thread 10 times

11) outputs
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread') #child thread 10 times
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread') #main thread 10 times

12) outputs
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target=c1.m1) #How  to  specify  the  target  as  m1  method
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)

13) outputs
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start() #Error because it is not valid
for  i  in  range(10):
        print('main  thread')

14) outputs
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')#main thread 10 times

15) outputs
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')#child thread 10 times
# End  of  the  class
child = MyThread()
child .  run()
for  i  in  range(10):
        print('main  thread')#main thread 10 times

16) outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
new = MyThread(target = f1)
new . start()
print('Main  Thread')
#run  method
Main  Thread

17) outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(10):
		print('f1  function') #f1 function 10 times
new = MyThread(target = f1) 
new . start()   
for  i  in  range(10):
	print('Main  Thread') #Main Thread 10 times

18) outputs
from  threading  import  *
class   MyThread(Thread):
	pass
new = MyThread() 
new . start()  
for  i  in  range(10):
	print('Main  Thread') #Main Thread 10 times

19) outputs
from  threading  import *
class  MyThread(Thread):
	def   walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread') #Main Thread 10 times