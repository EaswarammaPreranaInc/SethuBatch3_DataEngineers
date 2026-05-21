 # Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')  #try without except is not possible
---------------------------------------------------------------
# Find  outputs  (Home  work)
print(7 / 0)  #Error
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)  
print('Bye')
---------------------------------------------------------------
 # Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')  #except without try is not possible
----------------------------------------------------------------
# Find  outputs (Home  work)
try:
        print('One')            One
        print('Two')            Two
        print('Three')          Three
print('Four')   #error          Eight                
except:                         
		print('Five')
		print('Six')
		print('Seven')
print('Eight')
------------------------------------------------------------------
# Find  outputs  (Home work)
try:
	print('try suite')  #try suite
except:
	print('default  except')    #default except should be at last
except NameError:
	print('Name  Error')
------------------------------------------------------------------
# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')   #there should be only one default except
-------------------------------------------------------------------
#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)         #All the statements raise ZeroDivisionError
'''
When  is  ZeroDivisionError  raised ?  --->  When  division  by  0  (or)  0.0  is  made
'''
---------------------------------------------------------------------
#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))   #raises ValueError
print(float('Ten'))  #raises value Error
print(complex('True')) #Raises ValueError
print(bool('Ten'))   #True
print(bool(''))      #False
print(float('10.8'))  #10.8
print(float('25'))    #25.0   
print(int(10.8))      #10 
print(math . sqrt(-25))  #ValueError
'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
i.e. not  even  None
'''
----------------------------------------------------------------------------
# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)  #25
del  a   
print(a) #Error
print(eval("   'Ten'   "))   #'Ten'
print(eval('Ten'))  #NameError
'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''
--------------------------------------------------------------------------------
#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)  #30
print('10' + '20') #1020
print(10 + '20')  #TypeError
print(len('25'))  #2
print(len(25))  #TypeError
s = {10 , 20 , 15 , 18}
print(s[0])   #10
b = {[10 , 20] : [30 , 40]}  #TypeError
print(int(3 + 4j))  #TypeError
print(int([10 , 20 , 30]))  #TypeError
print(float(None))    #TypeError

'''
When  is  TypeError  raised ? ---> When  expression  has  illegal  operands  (or)
when  an  illegal  argument  is  passed  to  the  function (or)  method
------------------------------------------------------------------------------------
# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])  #Green
print(a['Y'])  #KeyError
'''
When  is  KeyError  raised  ?  --->  When  the  dictionary  key  is  invalid
'''
-----------------------------------------------------------------------------------
# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])  #H
print('Hyd'[1])  #Y
print('Hyd'[2])  #D
print('Hyd'[3])  #IndexError 
list = [10 , 20 , 15 , 18]
print(list[0]) #10  
print(list[3]) #15 
print(list[4]) #18
print(list[-1])  #18 
print(list[-4]) #10
print(list[-5]) #IndexError
tpl = (10 , 20 , 30)
print(tpl[3]) #IndexError
r = range(10)
print(r[10])  #10 
s = {10 , 20 , 15 , 18} 
print(s[4])  #IndexError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])  #10
'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''
------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('ZDE  1')          #ZDE 1
except    ZeroDivisionError:     #Bye
	print('ZDE  2')
print('Bye')
-----------------------------------------------------------------------------------
# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('Hyd')    #Hyd
	print(8 / 0)   #Error
except:
	print('Sec')
print('Bye')
-----------------------------------------------------------------------------------
'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)  
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:   
	print('Zero Division  Error')  #ZeroDivisionError
print('End')                       #End
-----------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')  #Arithmetic Error
print('End')                       #End
---------------------------------------------------------------------------------
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  
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
	print('Begin')      #Begin
	f1()                #f1 function
	print('Hi')         #ZDE  is  caught  outside
except  ZeroDivisionError:  #End
	print('ZDE  is  caught  outside')
except:
	print('Bye')
print('End')
----------------------------------------------------------------------------
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		print(7 / 0)  
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')
	print('End  of  f1  function')
# End  of  the  function
try:
	print('Begin')       #Begin
	f1()                 #f1 function
	print('Hello')       #ZDE is caught by f1 function
except  ZeroDivisionError:   #End of f1 function 
	print("Hi")          #Hello
except  ValueError:          #End
	print("Bye")
print('End')
--------------------------------------------------------------------------------
 What  are   the  outputs  if  input  is  1 ?  --->  #IndexError

What  are   the  outputs  if  input  is  2 ?  --->  #IndexError

What  are   the  outputs  if  input  is  3 ?  --->  #NameError

What  are   the  outputs  if  input  is  4 ?  --->  #TypeError

What  are   the  outputs  if  input  is  5 ?  --->  #NameError

What  are   the  outputs  if  input  is  6 ?  --->  #ZeroDivisionError

What  are   the  outputs  if  input  is  7 ?  --->  #TypeError

What  are   the  outputs  if  input  is  8 ?  --->  #KeyError
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
print('Bye')
-------------------------------------------------------------------------------
# Find  outputs
def  f1():
	print('f1  function')
	raise  ValueError('Hyd')
	print('Sec') 
# End of  the  function
f1()
try:
	print('Begin')             #Begin
	f1()                       #f1 function
	print('Bye')               #Caught  ValueError  outside  the  function         
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()  
print('End of the program')
----------------------------------------------------------------------------
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
	print('Begin')
	f1(10)  
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')
---------------------------------------------------------------------------
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
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')
-------------------------------------------------------------------------------
 Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''
class  singly_linked_list(sll):  
	def  delete(a , i):
		if   'i'  is  an  invalid  node  number:
			return  ???
		elif  deletion of  1st  node:
			How  to  delete  1st  node  and  return  the  data  of  deleted  node
		else:  
			How  to  delete  ith  node  and  return  the  data  of  deleted  node
# End  of  the  class
How  to  create  a  linked  list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	How  to  delete  ith  node
	if   ???:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  ??)
	How  to  print  linked   list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
-----------------------------------------------------------------------------------------------
 '''
Write  a  method  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
class  singly_linked_list(linked_list):
	def  concat(a , b):
		if  1st  linked  list  is  empty
			   Result  is  2nd   linked  list 
		else:  
			  How  to  modify  last  node  link  to  1st  node  of  2nd  linked  list
#  End  of  the  class
How  to  create  first   linked  list 
How  to  create  2nd   linked  list 
How  to  concatenates  the  two  linked  lists
How  to  print  the  resultant  linked  list
-------------------------------------------------------------------------------------------------
#  Write  a  method  to  copy  a  linked  list
class  singly_linked_list(linked_list):  
	def  copy(a):
		How  to  create  object  'b'
		How  to  copy  all  the  nodes  of  linked  list  'a'  to  'b'
		How  to   return  linked  list  'b'	
#  End  of  the  clas
How  to  create   linked  list  'a'
How  to  copy  all  the  nodes  of  linked  list  'a'  to  'b'
How  to  print  linked  list  'a'
How  to  print  linked  list  'b'
--------------------------------------------------------------------------------------------------
#  Write  destructor  to  delete  whole  linked  list
class  singly_linked_list(linked_list): 
	def    __del__(a):
			How  to  delete  each  node  of  the  linked  list  until  it  is  empty
#  End  of  the  clas
How  to  create  a  linked  list
-------------------------------------------------------------------------------------------------
#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
new = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
------------------------------------------------------------------------------------------------
 #  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
--------------------------------------------------------------------------------------------
 # Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
---------------------------------------------------------------------------------------------
# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()
---------------------------------------------------------------------------------------------