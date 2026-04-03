#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')#Begin
f2(f1)#f2 function <nextline> f1 function <nextline> Back to f2 function 
print('End')#End


#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()#Error NoneType object is not callable
	print('Back  to  f2  function')
# end of the function
print('Begin')#Begin
f2(f1())# f1 function <nextline> f2 function <comment <fun() to get out from error> <nextline> Back to f2 function
print('End')#End


# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()#prints-->Outer Function and returns inner
print('Hello')#Hello
fun()#inner()-->Inner function 
print('Bye')#Bye
inner()#error inner function not callable directly 


# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')#Outer Function Outer Function
	def  inner1():
		print('1st  inner  function')#1st inner function
	# End  of  inner1  function
	def  inner2():
		print("2nd  inner  function")#2nd inner function
	# End  of  inner2  function
	if   x == 10:
		return  inner1
	else:
		return  inner2
# End  of  the  outer  function
f1 = outer(10)#prints-->Outer Function return inner1 because(if condition is true x==10) 
f2 = outer(20)#prints-Outer Function return inner2 (else is True ) 
f1()#inner1() is called inside inner1() is executed
f2()#inner2()is called inside inner2() is executed


# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)# Hi Hello 
	return  inner
# End  of  the  function
hi_fun = outer('Hi')# Outer called 1st time and returns inner
hello_fun = outer('Hello')#outer called 2nd time and return inner
hi_fun()#inner() 
hello_fun()#inner()


#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
# End  of  the  function
f1 = decor(f1)#f1=inner
print(f1())#print(inner())-->print(10+2)-->12


# Find  outputs(Home  work)
def   decor(fun):
	print(fun . __name__)#wish(prints function name)
	def    inner(name):
		if   name  == 'Python':#True
			print('Hello' , name)#Hello Python
		else:
			fun(name)#
	return  inner
@decor#wish=decor(wish)# returns inner
def    wish(name):
        print('Hi' , name)#Hi Java
# End  of  the  function
wish('Python')#inner('Python')#if is executed
wish('Java')#inner('Java')#else is executed


# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor#div=decor(div)#return inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))#print(inner(10,3)-->print(3.3)#3.3 
print(div(10 , 0))#Division by 0 is not permitted
print(inner(10 , 3))#error directly inner() is not callable


# Modify  following  div  function  such  that  both  div(9 , 2)  and  div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a, b):#from here 
		if a < b:
			a, b = b, a 
		return fun(a, b)
	return inner
@decor#div=decor(div)=inner
def  div(a , b):
    return   a /b
print(div(9 , 2))  # 4.5
print(div(2 , 9))  # 4.5


#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')#Decorating f1 function
		fun()#f1()#Hello
		print('Decoration  is  finished')#Decoration is finished
	return  inner
@decor#f1=decor(f1)#inner
def   f1():
	print('Hello')
# End  of  the  function
f1()#inner()
print('Bye')#Bye


# Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)#f1 <nextline> f2 <nextline> f3 <nextline> f4
	def   inner(*x):  #  *  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor#f1=div(f1)#inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor#f2=div(f2)#inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor#f3=div(f3)#inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor#f4=div(f4)#inner
def   f4():
	print('f4 function')
# end of function
f1(10)#(10,) <nextline> f1 function : 10 <nextline> End of decoration
f2(25 , 10.8)#(25, 10.8) <nextline> f2 function : 25 10.8 <nextline> End  of  decoration
f3('Hyd' ,  True  , 3 + 4j)##('Hyd', True , 3+4j) <nextline> f3 function : Hyd True  3+4j <nextline> End  of  decoration
f4()#() <nextline> f4 function <nextline> End  of  decoration


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
print(num())#200



