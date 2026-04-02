 #  Find  outputs  (Home  work)
def  f1():
	print('f1  function')#f1 function
def   f2(fun):
	print('f2  function')#f2 function
	fun()
	print('Back  to  f2  function')#back to function
# end of the function
print('Begin')#begin
f2(f1)
print('End')#end
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')#begin
f2(f1())
print('End')
output:
Begin
f1  function
f2  function
Back  to  f2  function
End
 # Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()#
print('Bye')
#inner()
#output:
Outer  Function
Hello
Inner function
Bye
# Find  outputs (Home  work)
def  outer(x):x=10,20
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
f1 = outer(10)
f2 = outer(20)
f1()
f2()
output:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function

# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
 #  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
# End  of  the  function
f1 = decor(f1)
print(f1())#12
# Find  outputs(Home  work)
def   decor(fun):
	print(fun . _name_)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
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
	How  to  decorate  the  function  such  that  4.5  is  returned
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))  #  4.5
print(div(2 , 9))  # 4.5
[12:55 pm, 02/04/2026] SRINIVAS Sir Maths: #  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . _name_}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')
 # Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . _name_)
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
# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x 100
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y 100*2
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())#200