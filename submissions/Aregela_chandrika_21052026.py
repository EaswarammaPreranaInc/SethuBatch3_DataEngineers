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