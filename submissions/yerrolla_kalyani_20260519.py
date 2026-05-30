# Find  outputs  (Home  work)
print(7 / 0)  #error ZeroDivisionError---->here error is not handeld
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')#Division  by  zero  is  not  permitted
print(7 / 0)  #error ZeroDivisionError---->here error is not handeld
print('Bye')#Bye

#Identify  error  (Home  work)
except:#error without try we cann't use the except suite
        print('Hyd')
        print('Sec')
        print('Cyb')


#Find  outputs (Home  work)
try:
        print('One')#One
        print('Two')#Two
        print('Three')#Three
print('Four')#syntax error not an exceptional error to handel it  so, except suite is not executed (if we comment it the program will run properly)
except:
        print('Five')#Five
        print('Six')#Six
        print('Seven')#Seven
print('Eight')#Eight


# Find  outputs  (Home work)
try:
	print('try suite')#try suite
except:               #default except suite should be at the last
	print('default  except')
except NameError:# this  except suite NameError should be before the default except suite
	print('Name  Error')


#Find  outputs  (Home  work)
try:
	print('try suite')#try suite
except:
	print('1st  default  except')
except:                             #error here due to for i except suite there will be only the one except by default but not morethan one except suite.
	print('2nd  default  except')

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#error ZeroDivisionError  raised
print(7 / 0.0)#error ZeroDivisionError  raised
print(0 / 0)#error ZeroDivisionError  raised
print(0.0 / 0.0)#error ZeroDivisionError  raised
print(7 // 0)#error ZeroDivisionError  raised
print(7 % 0)#error ZeroDivisionError  raised



'''
When  is  ZeroDivisionError  raised ?  --->  When  division  by  0  (or)  0.0  is  made
'''
#  #  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) ##error value error
print(float('Ten'))#error value error
print(complex('True')) #error value error
print(bool('Ten')) #error value error
print(bool(''))#False
print(float('10.8'))#10.8
print(float('25')) #25.0
print(int(10.8)) # 10
print(math . sqrt(-25)) #error because math . sqrt(-25) + or - 5 which is  sqrt of negative number is not possible in python which is a dialamatic one


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)  
del  a   
print(a) # error ,a is not defined therefore  NameError
print(eval("   'Ten'   "))  #Ten
print(eval('Ten')) #error , Ten is not defined therefore  NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''

#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) #30 
print('10' + '20') #1020
print(10 + '20') #error because the unsopported operand between int and string i.e. TypeError 
print(len('25')) #2
print(len(25)) # int class not have len() function
s = {10 , 20 , 15 , 18}
print(s[0])  #error set is not indexed i.e. TypeError 
b = {[10 , 20] : [30 , 40]}  #error keys should be immutable objects only not  mutable objects.
print(int(3 + 4j))  #error complex obj is not converted to int i.e. TypeError
print(int([10 , 20 , 30])) #error int function can take only one argument that too  non-sequence  only .
print(float(None))# NoneType object is not converted to float class



'''
When  is  TypeError  raised ? ---> When  expression  has  illegal  operands  
																			 (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

 # Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) #Green
print(a['Y']) #errro no key 'Y' in the a i.e.KeyError


'''
When  is  KeyError  raised  ?  --->  When  the  dictionary  key  is  invalid
'''

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])# H
print('Hyd'[1]) #y
print('Hyd'[2]) #d
print('Hyd'[3])  # error invalid index number  ,index outof range i.e.IndexError
list = [10 , 20 , 15 , 18]
print(list[0])  #10
print(list[3])  #18
print(list[4]) # error invalid index number  ,index outof range i.e.IndexError
print(list[-1])  #18
print(list[-4]) #10
print(list[-5]) # error invalid index number  ,index outof range i.e.IndexError
tpl = (10 , 20 , 30)
print(tpl[3])## error invalid index number  ,index outof range i.e.IndexError
r = range(10)
print(r[10]) # error invalid index number  ,index outof range i.e.IndexError
s = {10 , 20 , 15 , 18}
print(s[4]) #error set is not indexed and it is a   i.e. TypeError 
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])# error dictionary is not indexed Key errro 


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''

Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('ZDE  1')#ZDE  1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye
#

Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('Hyd')#Hyd
	print(8 / 0)  #error is reported here because it is not enclosed in the try suite
except:
	print('Sec')
print('Bye')
# 



 '''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''



try:
	print(7 / 0)  
except   ArithmeticError:
	print('Arithmetic Error')	#	Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')	 
print('End')	#End



#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error
print('End')#End


 # Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  #f1  function
		print(7 / 0)  #error reported
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))	
	except ZeroDivisionError:
		print('Bye')#Bye
	print('End  of  f1  function')
# End of f1  function
try:
	print('Begin')  #Begin
	f1()  
	print('Hi')#Hi
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')#ZDE  is  caught  outside
except:
	print('Bye')
print('End')#End


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1  function
		print(7 / 0)  
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')#ZDE  is  caught  by  f1  function
	print('End  of  f1  function')#End  of  f1  function
# End  of  the  function
try:
	print('Begin')#Begin
	f1()
	print('Hello')#Hello
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')#End


'''
What  are   the  outputs  if  input  is  1 ?  --->#error index outof range  i.e.IndexError
What  are   the  outputs  if  input  is  2 ?  ---># error index outof range  i.e.IndexError
What  are   the  outputs  if  input  is  3 ?  ---># ValueError
What  are   the  outputs  if  input  is  4 ?  --->#NameError
What  are   the  outputs  if  input  is  5 ?  ---> ValueErro
What  are   the  outputs  if  input  is  6 ?  --->ZeroDivisionError
What  are   the  outputs  if  input  is  7 ?  --->TypeError
What  are   the  outputs  if  input  is  8 ?  --->KeyError
'''
while  True:
	try:
		ch = eval(input('Enter  choice (9-exit) : '))  
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])#  Invalid  index			#error index outof range  i.e.IndexError
			case  2:
				s = 'Hyd'
				print(s[3])#Invalid  index		 # error index outof range  i.e.IndexError
			case  3:
				print(int('Two'))  #No  result  # ValueError
			case  4:
				a = 25
				print(len(a))  #Object  does  not  exist #NameError
			case  5:
				print(eval('Hyd')) #No  result # ValueError
			case  6:
				print(7 / 0)  #Div by 0 is not allowed  # ZeroDivisionError
			case  7:
				print(10 + '20') #Invalid   argument (or)  operand
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18]) #Invalid dict key
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

 Find  outputs
def  f1():
	print('f1  function')
	raise  ValueError('Hyd')#
	print('Sec') 
# End of  the  function
f1()#f1  function<nxt>Hyd
try:
	print('Begin')#Begin
	f1()#f1  function<nxt line>Caught  ValueError  outside  the  function  :  Hyd
	print('Bye') 
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()  #error is reported
print('End of the program')

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
	print('Begin')#Begin
	f1(10)  #f1  function<nxtline>Caught  TypeError  outside  the  function : 25
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
print('End') #End


 #Find  outputs  (Home  work)
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
f1(10)#Caught  ValueError  :  25
f1(20)#Caught   NameError  :  10.8
f1(30)#Caught  IndexError  :  Hyd
f1(0)	#Caught   EOFError  : True
print('End of the program')#End of the program


"""

Write  a  method  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
"""
class  singly_linked_list(linked_list):
	def  concat(a , b):
		if  a.first==None:#1st  linked  list  is  empty
			return b.first#Result  is  2nd   linked  list 
		else:
                        last=a.first
                        while  last.link!=None:
                                        last=last.link
                        last.link=b.first	#How  to  modify  last  node  link  to  1st  node  of  2nd  linked  list
#  End  of  the  class

a=singly_linked_list()#How  to  create  first   linked  list 
a.create()

b=singly_linked_list()#How  to  create  2nd   linked  list 
b.create()

a.concat(a,b)#How  to  concatenates  the  two  linked  lists

a.disp()#How  to  print  the  resultant  linked  list
#  Write  a  method  to  copy  a  linked  list
class  singly_linked_list(linked_list):  
	def  copy(a):
		b=singly_linked_list#How  to  create  object  'b'
		b.first=a.first	#How  to  copy  all  the  nodes  of  linked  list  'a'  to  'b'
		return b#How  to   return  linked  list  'b'	
#  End  of  the  clas
a=singly_linked_list()#How  to  create   linked  list  'a'
a.create()
b=a.copy()#How  to  copy  all  the  nodes  of  linked  list  'a'  to  'b'
a.disp()#How  to  print  linked  list  'a'
b.disp()#How  to  print  linked  list  'b'


#  Write  destructor  to  delete  whole  linked  list
class  singly_linked_list(linked_list): 
	 while a.first is not None:
                p = a.first
                a.first = a.first.link
                del p#How  to  delete  each  node  of  the  linked  list  until  it  is  empty
			
a=singly_linked_list()#How  to  create   linked  list  
a.create()


 #  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
new = Thread(target = f1)
f1()#child  thread ---> printed 10 times
for  i  in  range(10):
        print('main  thread')#main  thread ---> printed 10 times

 #  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')#main  thread-->printed 10 times 

 # Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')#main  thread-->10 times 

# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')#Child  Thread-->5 times , Child  Thread-->5 times
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')#Main  Thread --->9 times Main  Thread--->1 vary from run to run 
child . start()#