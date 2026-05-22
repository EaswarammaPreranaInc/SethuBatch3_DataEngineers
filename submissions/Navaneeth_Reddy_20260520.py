# Find  outputs
try:
	print(7 / 0)  
	print('Hello') 
except  ZeroDivisionError:
	print('ZDE  1') 
	try:
		print(8 / 0)  
	except  ZeroDivisionError:
		print('ZDE   2') 
	print('Bye') 
except  ZeroDivisionError:
	print('ZDE  3')
print('End')
'''
Output :
ZDE  1
ZDE   2
Bye
End
'''

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')  
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
'''
Output :
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
		print('Hi')  
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
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
'''
Output:
Begin
f1 function
Caught by f1 function :  25
Recaught ValueError :   25
End of the program
'''

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
'''
Output:
Begin
f1 function
Caught by f1 function :   25
Some other error
End of the program
'''

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
'''
Output:
Begin
f1 function
f1's finally
ValueError is caught outside :   Hyd
f2 function
f2's finally
f3 function
Caught by f3 function :   25
f3's finally
End of f3 function
f4 function
f4's finally
Outside finally
'''

# Find  outputs  (Home  work)
import sys
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
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')
'''
Output:
Begin
f1 function
f1's finally
ValueError is caught outside :  Hyd
End of the program
'''

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
			raise  Exception()# IndentationError as it is not indented
	except:
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function') 
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')


# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')
'''
Output:
Begin
f1 function
Caught KeyError
f1 finally
Recaught Exception
Outside finally
End of the program
'''

# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program')
'''
Output:
Begin
f1 function
Caught KeyError
f1 finally
Outside finally
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
Output:
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
Output:
try
else
finally
End
'''

# Find  outputs   (Home  work)
try:
	print('try')
else: # SyntaxError else cannot appear without except.
    print('else')
finally:
    print('finally')
print('End')


# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else: # only one else stmt can be not more
	print('else2')
finally:
	print('finally')
print('end')


# Find  outputs  (Home  work)
try:
	print('try')
else:# else cannot be before except
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')


# Find  outputs   (Home  work)
try:
	print('try')# try
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')# else


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
print(f1())# 10

# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20
	else:
		return  30
print(f1())# 20

# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())#30

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
print(f1())# 10 \n 40


'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->

2) What  is  the  output  if  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  ')) 
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')
'''
Output:
Enter any number : 24
Hyd
End

Enter any number : 25
Sec
End
'''


''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->

2) What  is  the  output  when  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))  
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')
'''
Output:
Enter any number : 24

End

Enter any number : 25
Sec
End
'''