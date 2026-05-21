 # Find  outputs
try:
	print(7 / 0)  
	print('Hello') 
except  ZeroDivisionError:
	print('ZDE  1')           #ZDE 1
	try:                      #ZDE 2
		print(8 / 0)      #Bye 
	except  ZeroDivisionError: #End 
		print('ZDE   2') 
	print('Bye') 
except  ZeroDivisionError:
	print('ZDE  3')
print('End')
------------------------------------------------------------------------
#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')             #f1 function
		raise  ValueError(25)            #caught by f1 function : 25
		print('Hi')                      #Recaught by f1 function : msg
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')
--------------------------------------------------------------------------
#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')  
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')          #Begin
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')  
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')
---------------------------------------------------------------------------
 # Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)
		raise  NameError(msg)
	except:
		print('Hello')
	print('End of f1 function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program')
------------------------------------------------------------------------------
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')  
	finally:
		print("f1's  finally")
	print('End  of  f1  function') 
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')  
	finally:
		print("f2's  finally")
	print('End  of  f2  function')   
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')  
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)
	finally:
		print("f3's  finally")
	print('End of f3 function')
def  f4():
	try:
		print('f4 function')
		exit()
	finally:
		print("f4's  finally")
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello') 
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')
print('End  of  the  program')