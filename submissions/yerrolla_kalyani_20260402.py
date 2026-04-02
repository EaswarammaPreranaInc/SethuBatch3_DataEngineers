#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')#Begin
f2(f1)#f2  function <nxt> f1  function <nxt> Back  to  f2  function
print('End')#End



#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):#none
	print('f2  function')
	fun()#error 
	print('Back  to  f2  function')
# end of the function
print('Begin')#Begin
f2(f1())#f1  function <nxt> Back  to  f2  function <nxt> End
print('End')#End


# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()#Outer Function 
print('Hello')#Hello
fun()#Inner function
print('Bye')#Bye
inner()#error cnnot call inner() function directly 

# Find  outputs (Home  work)
def  outer(x):
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
f1 = outer(10)#Outer  Function 
f2 = outer(20)#Outer  Function
f1()#1st  inner  function
f2()#2st  inner  function


# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') 
hello_fun = outer('Hello')#
hi_fun()#Hi
hello_fun()#Hello


#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
# End  of  the  function
f1 = decor(f1)#
print(f1())#12




# Find  outputs(Home  work)
def   decor(fun):
	print(fun . __name__)#wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor #wish=inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')#Hello Python
wish('Java')#Hi Java





# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor#div=inner 
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))#3.33333
print(div(10 , 0))#'Division   by  0  is  not  permitted'
print(inner(10 , 3))#cannot call inner function directly



# Modify  following  div  function  such  that  both  div(9 , 2)  and  div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner (a,b):
        if a<b:
            a,b=b,a 
            return fun(a,b)                
    return inner#How  to  decorate  the  function  such  that  4.5  is  return
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))  #  4.5
print(div(2 , 9))  # 4.5


 #  Find  outputs (Home  work)
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
f1()#Decorating  f1  function<nxt> Hello <nxt> Decoration  is  finished
print('Bye')#Bye



# Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #  *  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor #f1=inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor #f2=inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor #f3=inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor #f4=inner
def   f4():
	print('f4 function')
# end of function
f1(10)   #(10,)    <nxt> f1  function  :  ' , 10     <nxt>     End of decorator
f2(25 , 10.8)#(25 , 10.8)     <nxt> f2  function  :  ' , 25  10.8       <nxt>      End of decorator
f3('Hyd' ,  True  , 3 + 4j)#('Hyd' ,  True  , 3 + 4j)     <nxt> f3  function  :  Hyd'     True      3 + 4j       <nxt>      End of decorator
f4()#()   <nxt>  f4 function  <nxt>   End  of  decoration



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
@double #num=inner2
@square #num=inner1
def  num():
	return  10 
#end of the function
print(num())#200