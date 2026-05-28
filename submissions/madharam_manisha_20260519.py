# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
# No except or finally suite

# Find  outputs  (Home  work)
#print(7 / 0)  # Error 
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')#Division  by  zero  is  not  permitted
#print(7 / 0)  # Error
print('Bye')#Bye

# Identify  error  (Home  work)
#without try suite cannot use except
except:
        print('Hyd')
        print('Sec')
        print('Cyb')

# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') #error here
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
#except NameError: # it should be before default except suite
	print('Name  Error')
	
# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
#except:# only one default except suite is valid 
	print('2nd  default  except')
	
#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)# Error
print(7 / 0.0)# Error
print(0 / 0)# Error
print(0.0 / 0.0)# Error
print(7 // 0)# Error
print(7 % 0)# Error

#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) #Error
print(float('Ten'))#Error
print(complex('True')) #Error
print(bool('Ten')) #True
print(bool(''))#False
print(float('10.8'))# 10.8
print(float('25'))  # 25.0
print(int(10.8))  # 10
print(math . sqrt(-25)) #Error

# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) #25 
del  a   
print(a) #Error
print(eval("   'Ten'   "))  # Ten
print(eval('Ten'))  #Error

#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) #30 
print('10' + '20') #1020
print(10 + '20') #Error
print(len('25')) #2
print(len(25)) #Error
s = {10 , 20 , 15 , 18}
print(s[0])  #Error
b = {[10 , 20] : [30 , 40]}  #Error
print(int(3 + 4j))  #Error
print(int([10 , 20 , 30]))#Error
print(float(None))  #Error

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) #Green
print(a['Y']) #Error

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) 
print('Hyd'[1]) 
print('Hyd'[2])
#print('Hyd'[3])#Error  
list = [10 , 20 , 15 , 18]
print(list[0])  
print(list[3])  
#print(list[4]) #Error
print(list[-1])  
print(list[-4]) 
#print(list[-5]) #Error
tpl = (10 , 20 , 30)
#print(tpl[3])#Error
r = range(10)
#print(r[10]) #Error 
s = {10 , 20 , 15 , 18}
#print(s[4]) #Error
d = {10 : 'Hyd' , 20 : 'Sec'}
#print(d[0]) #Error

# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('ZDE  1')# ZDE  1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')# Bye

# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('Hyd')# Hyd
	#print(8 / 0)  #Error
except:
	print('Sec')
print('Bye')# Bye


'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)  
except   ArithmeticError:
	print('Arithmetic Error')# Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')# End

#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  #f1 function ---2
		print(7 / 0)  
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:
		print('Bye')
	print('End  of  f1  function')
# End of f1  function
try:
	print('Begin')  #Begin---1
	f1()  
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')# ZDE  is  caught  outside---3
except:
	print('Bye')
print('End')#End---4

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')# f1 func----2
		print(7 / 0)  
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')# ----3
	print('End  of  f1  function')#-----4
# End  of  the  function
try:
	print('Begin') #Begin
	f1()
	print('Hello')#-----5
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')#-----6

'''
What  are   the  outputs  if  input  is  1 ?  --->#Invalid  index

What  are   the  outputs  if  input  is  2 ?  --->#Invalid  index

What  are   the  outputs  if  input  is  3 ?  --->#Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  4 ?  --->#Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  --->#Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  --->#Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  --->#Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  --->#'Invalid dict key'
'''
while  True:
	try:
		ch = eval(input('Enter  choice (9-exit) : '))  
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5]) 
			case  2:
				s = 'Hyd'
				print(s[3]) 
			case  3:
				print(int('Two'))  
			case  4:
				a = 25
				print(len(a))  
			case  5:
				print(eval('Hyd')) 
			case  6:
				print(7 / 0)  
			case  7:
				print(10 + '20') 
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18]) 
			case   9:
				break
	except   ZeroDivisionError:
		print('Div by 0 is not allowed')
	except  ValueError:
		print('No  result')
	except  IndexError:
		print('Invalid  index')
	except  TypeError:
		print('Invalid   argument (or)  operand')
	except  KeyError:
		print('Invalid dict key')
	except  NameError:
		print('Object  does  not  exist')
	except:
		print('A new error')
# End of while loop
print('Bye')#Bye

#  Find  outputs
def  f1():
	print('f1  function')#----1,,, #----2
	raise  ValueError('Hyd')
	print('Sec') 
# End of  the  function
#f1()#Error reported
try:
	print('Begin')#-----1
	f1()
	print('Bye') 
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)#Caught  ValueError  outside  the  function  : Hyd----3
#f1()  #Errror reported
print('End of the program')#----4

#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
	raise ValueError()
# End of  the function
try:
	print('Begin')#----1
	f1(10)  #----f1 func 2
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd')
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)#    25----3
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')#-----4

# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)
		elif   a == 20:
			raise  NameError(10.8)
		elif   a == 30:
			raise  IndexError('Hyd')
		raise  EOFError(True)
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)
	print('End  of  f1  function')
# End  of  the  function
f1(10)# Caught ValueError : 25, End of f1 func
f1(20)# Caught NameError : 10.8, End of f1 func
f1(30)# Caught IndexError : Hyd, End of f1 func
f1(0)# Caught EOFError : True, End of f1 func
print('End of the program')# End of the program

#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
new = Thread(target = f1)
f1()# child Thread 10 times
for  i  in  range(10):
        print('main  thread')# main thread 10 times simultaneously
		
#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')# main thread 10 times
		
# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()# executes the empyty run() method of Thread class
for  i   in   range(10):
        print('main  thread')# main thread 10 times
		
# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()# register the child thread with thread schedular
# Child Thread for some times  
for  i  in  range(10):
        print('Main  Thread') # Main Thread for somes times
#child . start()# Error