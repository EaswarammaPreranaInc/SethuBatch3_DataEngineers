#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')	#f1 function 3
def   f2(fun):
	print('f2  function')	#f2 function 2
	fun()
	print('Back  to  f2  function')	#Back to f2 function 4
# end of the function
print('Begin')	#Begin 1
f2(f1)
print('End')	#End 5




#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')	#f1 function 2
def   f2 (fun):
	print('f2  function')	#f2 function 3
	fun()	#error 4
	print('Back  to  f2  function') Back to f2 function 5
# end of the function
print('Begin')	#begin 1
f2(f1())
print('End')	#End 6



# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')	#outer function 1
	def  inner():
		print('Inner function')	#Inner function 3
	return   inner
# End  of  the  function
fun = outer()
print('Hello')	#Hello 2
fun()
print('Bye')	#Bye 4
inner()		#error because inner function is not visible 5



# Find  outputs (Home  work)
def  outer():
	print('Outer  Function')	
	def  inner1():
		print('1st  inner  function')	
	# End  of  inner1  function
	def  inner2():
		print("2nd  inner  function")	
	# End  of  inner2  function
	if   x == 10:
		return  inner1
	else:
		return  inner2
# End  of  the  outer  function
f1 = outer(10)	#error because it dosen't excepts arguments
f2 = outer(20)	#error because it dosen't excepts arguments
f1()	#error because f1 is not defined
f2()	#error because f1 is not defined



# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()	#Hi
hello_fun()	#Hello



#  How  to  call  f1()  function  when  @decor  tag  is  missing
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
# End  of  the  function
f1 = decor(f1)
print(f1())	#12




# Find  outputs(Home  work)
def   decor(fun):
	print(fun . __name__)	#wish 1
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)	#Hello python 2 
		else:
			fun(name)	#Hello java 3
	return  inner
@decor
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')




# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
print(inner(10 , 3))



# Modify  following  div  function  such  that  both  div(9 , 2)  and  div(2 , 9)  should  return  4.5  only
def  decor(fun):
	#How  to  decorate  the  function  such  that  4.5  is  returned
    def inner(a, b):
        if a < b:
            a, b = b, a   # swap values
        return fun(a, b)
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5



#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function') #Decorating 'f1' function 1
		fun()
		print('Decoration  is  finished')	#Decoration is finished 3
	return  inner
@decor
def   f1():
	print('Hello')	#Hello 2
# End  of  the  function
f1()
print('Bye')	#Bye 4




# Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)	 
	def   inner(*x):  #  *  is  var-arg  parameter
		print(x)	
		fun(*x)  #  Unpacks  object  'x'   
		print('End  of  decoration')	
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x)	
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()

outputs:
f1
f2
f3
f4
(10,)
f1 function : 10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration




# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())	#200