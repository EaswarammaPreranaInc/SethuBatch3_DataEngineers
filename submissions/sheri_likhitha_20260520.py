# Find  outputs
try:
	print(7 / 0) 	#zero division by error occurs 
	print('Hello') 
except  ZeroDivisionError:
	print('ZDE  1') 	#ZDE 1
	try:
		print(8 / 0) 	#zero division by error occurs 
	except  ZeroDivisionError:
		print('ZDE   2') 	#ZDE 2
	print('Bye') 			#Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')				#End




#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)	#value error is raised
		print('Hi') 	#skipped 
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)	#Caught  by  f1 function : 25
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)	#Recaught by f1 function :  25
	except:
		print('Hello')
	print('End  of  f1  function')		#End  of  f1  function
# End  of  the  function
try:
	print('Begin')		#Begin
	f1()			#f1 function
	print('Hyd')		#Hyd
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')	#End of the program






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


#Begin
f1 function
Caught by f1 function :  25
Recaught ValueError :   25
End of the program




# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)	#value error is raised
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)	#Caught  by  f1 function :25 
		raise  NameError(msg)		#name error is raised
	except:
		print('Hello')
	print('End of f1 function')
# End  of  the  function
try:
	print('Begin')		#Begin
	f1()			#f1 function
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')	#some other error
print('End of the program')		#End of the program





# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi') 	#skipped 
	finally:
		print("f1's  finally")	#f1's finally
	print('End  of  f1  function') 	#End  of  f1  function
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')		  
	finally:
		print("f2's  finally")	#f2's  finally
	print('End  of  f2  function')	   
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')	#skipped  
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)	#Caught by f3 function :   25
	finally:
		print("f3's  finally")		#f3's finally
	print('End of f3 function')		#End of f3 function
def  f4():
	try:
		print('f4 function')
		exit()
	finally:
		print("f4's  finally")		#f4's finally
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')		#Begin
	f1()			#f1 function
	print('Hello') 		#Hello
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)	#ValueError is caught outside :   Hyd
f2()			#f2  function
f3()			#f3  function
try:
	f4()		#f4 function
finally:
		print('Outside  finally')	#Outside finally
print('End  of  the  program')






# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")	#f1's finally
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
	print('Begin')		#Begin
	f1()			#f1 function 
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)	#ValueError is caught outside :   Hyd
print('End  of  the  program')			#End  of  the  program






# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')	#Caught  KeyError
			raise  Exception()
	except:
		print('Sec')			
	finally:
		print("f1's  finally")		#f1's  finally
	print('End  of  f1  function') 
# End  of  the  function
try:
	print('Begin')		#Begin
	f1()			#f1  function
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')		#Recaught  Exception
finally:
	print('Outside  finally')		#Outside finally
print('End  of  the  program')			#End of the program





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


#outputs
Begin
f1 function
Caught KeyError
f1 finally
Caught Name Error outside
Outside finally
End of the program




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


#outputs:
Begin
f1 function
Caught KeyError
f1 finally
Outside finally





# Find  outputs  (Home  work)
try:
	print('try')	#try
	print(7 / 0)  
except:
	print('except')	#except
else:
	print('else')
finally:
	print('finally')   #finally
print('End')		#End




# Find  outputs  (Home  work)
try:
	print('try')	#try
except:
	print('except')
else:
	print('else')	#else
finally:
	print('finally')  #finally
print('End')		#end



# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')	#else without except error
finally:
    print('finally')
print('End')	#this program does not produce any outputs




# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else:
	print('else2')		#only one else is allowed for one try suite
finally:
	print('finally')
print('end')




# Find  outputs  (Home  work)
try:
	print('try')
else:
	print('else')	#else appears before except invalid  syntax error
except:
	print('except')
finally:
	print('finally')
print('end')




# Find  outputs   (Home  work)
try:
	print('try')	#try
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')	#else



# Find  outputs
def   f1():
	try:
		return  10 + '20'  
	except:
		return  10 + 20
print(f1())	#30



# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1())	#10




