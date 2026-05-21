# Find  outputs
try:
	print(7 / 0)  
	print('Hello') 
except  ZeroDivisionError:
	print('ZDE  1') # ZDE  1
	try:
		print(8 / 0)  
	except  ZeroDivisionError:
		print('ZDE   2')  # ZDE   2
	print('Bye')  # Bye
except  ZeroDivisionError: # skipped
	print('ZDE  3')
print('End') # End

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')  # Skipped
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)
			raise   ValueError(msg)
		except  ValueError  as   msg: # Skipped
			print('Recaught  by  f1 function  : ' , msg)
	except: # Skipped
		print('Hello') # Skipped
	print('End  of  f1  function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x: # Skipped
	print('Recaught ValueError  :  ' , x)
except: # Skipped
	print('Some other error') # Skipped
print('End of the program')
'''
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program
'''

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')  # Skipped
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
	except: # Skipped
		print('Hello')
	print('End  of  f1  function') 
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')  
except  ValueError  as  x: 
	print('Recaught ValueError  :  ' , x)
except: # Skipped
	print('Some other error')
print('End of the program')
'''
Begin
f1 function
Caught  by  f1 function  :  25
Recaught ValueError  :   25
End of the program
'''

# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi') # Skipped
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)
		raise  NameError(msg)
	except: # Skipped
		print('Hello')
	print('End of f1 function') # Skipped
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd') # Skipped
except  ValueError  as  x: # Skipped
	print('Recaught ValueError : ' , x) # Skipped
except:
	print('Some other error')
print('End of the program')
'''
Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program
'''

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')   # Skipped
	finally:
		print("f1's  finally")
	print('End  of  f1  function') # Skipped
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')  # Skipped
	finally:
		print("f2's  finally")
	print('End  of  f2  function')   # Skipped
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')  # Skipped
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
	print('End of f4 function') # Skipped
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')  # Skipped
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')
print('End  of  the  program') # Skipped
'''
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function :   25
f3's  finally
End of f3 function
f4 function
f4's  finally
Outside  finally
'''

# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi') # Skipped
	finally:
		print("f1's  finally")
	print('End  of  f1  function') # Skipped
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
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)
	finally:
		print("f3's  finally")
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
# End  of  all  the  functions
try:
	print('Begin')
	f1() 
	f2() # Skipped
	f3() # Skipped
	f4() # Skipped
	print('Hello') # Skipped
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')
'''
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
End  of  the  program
'''

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd') # Skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except: # Skipped
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function') # Skipped
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello') # Skipped
except  ValueError: # Skipped
	print('Hello') 
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')
'''
Begin
f1  function
Caught  KeyError
f1's  finally
Recaught  Exception
Outside  finally
End  of  the  program
'''

# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd') # Skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()
	except  NameError: # Skipped
		print('Sec') # Skipped
	finally:
		print('f1 finally')
	print('End  of  f1 function') # Skipped
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello') # Skipped
except ValueError: # Skipped
	print('Hello')
except   Exception:
	print('Recaught  Exception')
except  NameError: # Skipped
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')
'''
Begin
f1  function
Caught  KeyError
f1 finally
Caught  Name Error  outside
Outside  finally
End of the program
'''

# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd') # Skipped
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()
	except  NameError: # Skipped
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function') # Skipped
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello') # Skipped
except  ValueError: # Skipped
	print('Hello') # Skipped
except   KeyError: # Skipped
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program') # Skipped
'''
Begin
f1  function
Caught  KeyError
f1 finally
Outside  finally
'''

# Find  outputs  (Home  work)
try:
	print('try')
	print(7 / 0)  
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')
'''
try
except
finally
End
'''

# Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')
'''
try
else
finally
End
'''

# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else') # ERROR because there should be no else without except suite
finally:
    print('finally')
print('End')

# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1') # ERROR because there should be only one else suite for each try suite
else:
	print('else2') # ERROR because there should be only one else suite for each try suite
finally:
	print('finally')
print('end')

# Find  outputs  (Home  work)
try:
	print('try')
else:  # ERROR because else suite should be after except suite
	print('else') 
except:
	print('except')
finally:
	print('finally')
print('end')

# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')
'''
try
else
'''

# Find  outputs
def   f1():
	try:
		return  10 + '20'  
	except:
		return  10 + 20 
print(f1()) # 30

# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1()) # 10

# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20
	else:
		return  30
print(f1()) # 20

# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1()) # 30

# Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40
print(f1()) # 40

'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  ---> Hyd  End
2) What  is  the  output  if  input  is  25 ?  ---> Sec  End
'''
try:
	x = eval(input('Enter  any  number  :  ')) 
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')

''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  ---> 'empty'End
2) What  is  the  output  when  input  is  25 ?  ---> Sec End
'''
try:
	x = eval(input('Enter  any  number  :  '))  
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')