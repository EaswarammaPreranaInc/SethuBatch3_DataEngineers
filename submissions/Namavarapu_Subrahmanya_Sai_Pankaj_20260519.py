'''
# 1) Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')  # No Except Suite
'''
'''
2) # Find  outputs  (Home  work)
print(7 / 0)  
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0) 
print('Bye')   # ZeroDivisionError
'''
'''
3) # Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')  # Except try suite cant be used without try suite
'''
'''
4) # Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')
except:
		print('Five')
		print('Six')
		print('Seven')  # Error because except block should be immediately after try block and no statements in between
print('Eight')
'''
'''
5) # Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')  # Error
'''
'''
6) # Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')  # Error cause only 1 except suite is allowed
'''
'''
7) #  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)  
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)  # All statements raise ZeroDivisionError

When  is  ZeroDivisionError  raised ?  --->  When  division  by  0  (or)  0.0  is  made
'''
'''
8) #  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))  # Raises Value Error
print(float('Ten'))  # Raises Value Error
print(complex('True'))   # Raises Value Error
print(bool('Ten')) 
print(bool(''))
print(float('10.8'))
print(float('25'))  
print(int(10.8))  
print(math . sqrt(-25))   # Raises Value Error

When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''
'''
9) # Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)  
del  a   
print(a)   # Raises Value Error
print(eval("   'Ten'   "))  
print(eval('Ten'))   # Raises Value Error

When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''
'''
10) #  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)  
print('10' + '20') 
print(10 + '20')    # Raises TypeError
print(len('25')) 
print(len(25))    # Raises Value Error
s = {10 , 20 , 15 , 18}
print(s[0])    # Raises Value Error 
b = {[10 , 20] : [30 , 40]}     # Raises Value Error
print(int(3 + 4j))     # Raises Value Error
print(int([10 , 20 , 30]))   # Raises Value Error
print(float(None))     # Raises Value Error

When  is  TypeError  raised ? ---> When  expression  has  illegal  operands  
																			 (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''
'''
11) # Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) 
print(a['Y'])     # Raises Key Error

When  is  KeyError  raised  ?  --->  When  the  dictionary  key  is  invalid
'''
'''
12) # Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) 
print('Hyd'[1]) 
print('Hyd'[2])
print('Hyd'[3])       # Raises Index Error
list = [10 , 20 , 15 , 18]
print(list[0])  
print(list[3])  
print(list[4])      # Raises Key Error
print(list[-1])  
print(list[-4]) 
print(list[-5])      # Raises Key Error
tpl = (10 , 20 , 30)
print(tpl[3])     # Raises Key Error
r = range(10)
print(r[10])       # Raises Key Error
s = {10 , 20 , 15 , 18}
print(s[4]) 
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0]) 

When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''
'''
13) # Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:
	print('ZDE  2')  #Error because Same except block cannot be written multiple times
print('Bye')
'''
'''
14) Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
try:
	print(7 / 0)  
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')  # ArithmeticError <nextline> End
'''
'''
15) #  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')  # ArithmeticError <nextline> End
'''
'''
16) # Find  outputs  (Home  work)
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
	print('Begin')  
	f1()  
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')
except:
	print('Bye')
print('End') #  Begin <nextline>f1 function<nextline>ZDE is caught outside<nextline>End
'''
'''
17) # Find  outputs  (Home  work)
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
	print('Begin')
	f1()
	print('Hello')
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')  # Begin <nextline> f1 function <nextline> ZDE is caught by f1 function <nextline> End of f1 function <nextline> Hello <nextline> End
'''
'''
18) # What are the outputs if input is 1 ? ---> Invalid index
# What are the outputs if input is 2 ? ---> Invalid index
# What are the outputs if input is 3 ? ---> No result
# What are the outputs if input is 4 ? ---> Invalid argument (or) operand
# What are the outputs if input is 5 ? ---> Object does not exist
# What are the outputs if input is 6 ? ---> Div by 0 is not allowed
# What are the outputs if input is 7 ? ---> Invalid argument (or) operand
# What are the outputs if input is 8 ? ---> Invalid dict key
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
'''
'''
19) #  Find  outputs
def  f1():
	print('f1  function')
	raise  ValueError('Hyd')
	print('Sec') 
# End of  the  function
f1()
try:
	print('Begin')
	f1()
	print('Bye') 
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()  
print('End of the program')  # f1 function <nextline> ValueError: Hyd
'''
'''
20) #Find  outputs  (Home  work)
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
print('End')  # Begin <nextline> f1 function <nextline> Caught TypeError outside the function : 25 <nextline> End
'''
'''
21) # Find  outputs  (Home  work)
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
print('End of the program') # Caught ValueError : 25 <nextline> End of f1 function <nextline> Caught NameError : 10.8 <nextline> End of f1 function <nextline> Caught IndexError : Hyd <nextline> End of f1 function <nextline> Caught EOFError : True <nextline> End of f1 function <nextline> End of the program
'''
'''
22) Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''
class singly_linked_list(sll):  
	def delete(a , i):
		if i <= 0 or i > len(a):
			return None
		elif i == 1:
			x = a.first.data
			a.first = a.first.next
			return x
		else:
			p = a.first
			for k in range(1 , i - 1):
				p = p.next
			x = p.next.data
			p.next = p.next.next
			return x
# End of the class
a = singly_linked_list()
n = int(input('Enter number of nodes : '))
for i in range(n):
	x = int(input('Enter data : '))
	a.append(x)
while True:
	i = int(input('Enter value of i : '))
	x = a.delete(i)
	if x == None:
		print(F'Node {i} does not exist')
	else:
		print('Data of deleted node is ' , x)
	print('Linked list : ' , a)
	ch = input('Would you like to delete another node (Y or N) ? : ')
	if ch == 'n' or ch == 'N':
		break
'''
23) Write  a  method  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
class singly_linked_list(linked_list):
	def concat(a , b):
		if a.first == None:
			a.first = b.first
		else:
			p = a.first
			while p.next != None:
				p = p.next
			p.next = b.first
# End of the class
a = singly_linked_list()
n = int(input('Enter number of nodes in first linked list : '))
for i in range(n):
	x = int(input('Enter data : '))
	a.append(x)
b = singly_linked_list()
n = int(input('Enter number of nodes in second linked list : '))
for i in range(n):
	x = int(input('Enter data : '))
	b.append(x)
a.concat(b)
print('Resultant linked list : ')
print(a)
'''
24) #  Write  a  method  to  copy  a  linked  list
'''
class singly_linked_list(linked_list):
	def copy(a):
		b = singly_linked_list()
		p = a.first
		while p != None:
			b.append(p.data)
			p = p.next
		return b
# End of the class
a = singly_linked_list()
n = int(input('Enter number of nodes : '))
for i in range(n):
	x = eval(input('Enter data : '))
	a.append(x)
b = a.copy()
print('First linked list : ')
print(a)
print('Copied linked list : ')
print(b)
'''
25) #  Write  destructor  to  delete  whole  linked  list
class  singly_linked_list(linked_list): 
	def    __del__(a):
			How  to  delete  each  node  of  the  linked  list  until  it  is  empty
#  End  of  the  clas
How  to  create  a  linked  list
'''
class singly_linked_list(linked_list):
	def __del__(a):
		cur = a.first
		while cur != None:
			next = cur.next
			del cur
			cur = next
		a.first = None
# End of the class
a = singly_linked_list()
n = int(input('Enter number of nodes : '))
for i in range(n):
	x = eval(input('Enter data : '))
	a.append(x)
print(a)
'''
26) #  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
new = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')  # # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
27) #  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread') # child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> child thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
28) # Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')  # main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread <nextline> main thread
'''
'''
29) # Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()  # Child Thread and Main Thread outputs may come in any order <nextline> RuntimeError: threads can only be started once
'''