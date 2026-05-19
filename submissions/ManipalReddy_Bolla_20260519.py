# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')#try and except both should present
	
# Find  outputs  (Home  work)
print(7 / 0)#error if commented except will execute
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')#prints Division by zero is not permitted
print(7 / 0)#error #if commented
print('Bye')# Bye


# Identify  error  (Home  work)
except:#error 
        print('Hyd')
        print('Sec')
        print('Cyb')
		
	
# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')#error
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
except NameError:#error because default except must after all excepts
	print('Name  Error')
	
	
# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')# only one default except should be there
	
	
#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#error in below all 
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)


'''
When  is  ZeroDivisionError  raised ?  --->  When  division  by  0  (or)  0.0  is  made
'''


#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))#raise
print(float('Ten'))#raise
print(complex('True'))#raise
print(bool('Ten'))
print(bool(''))
print(float('10.8'))
print(float('25'))  
print(int(10.8))  
print(math . sqrt(-25))#raise



# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)  
del  a   
print(a)#error
print(eval("   'Ten'   "))  
print(eval('Ten'))  


# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) 
print(a['Y'])#error


# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('ZDE  1')#ZDE  1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye


# Find  outputs  (Home  work)
try:
	print(7 / 0)  
	print('Hello')  
except    ZeroDivisionError:
	print('Hyd')
	print(8 / 0)#During handling of the above exception, another exception occurred  
except:
	print('Sec')
print('Bye')


'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)  
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')#End


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
		print('f1  function')#f1 function  
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
	print('Begin')#Begin  
	f1()  
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')#ZDE  is  caught  outside
except:
	print('Bye')
print('End')#End


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
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
print('End')


while  True:
	try:
		ch = eval(input('Enter  choice (9-exit) : '))  
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])#Invalid  index
			case  2:
				s = 'Hyd'#Invalid  index
				print(s[3]) 
			case  3:
				print(int('Two'))#No  result
			case  4:
				a = 25
				print(len(a))#Invalid   argument (or)  operand
			case  5:
				print(eval('Hyd')) #Object  does  not  exist
			case  6:
				print(7 / 0)  #Div by 0 is not allowed
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
print('Bye')


