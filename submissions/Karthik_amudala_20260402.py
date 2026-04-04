#  Find  outputs  (Home  work)  

def  f1():  
	print('f1  function')        # f1 function  

def   f2(fun):  
	print('f2  function')        # f2 function  
	fun()                        # calls f1 → f1 function  
	print('Back  to  f2  function')   # Back to f2 function  

# end of the function  

print('Begin')                 # Begin  
f2(f1)                         # f2 function → f1 function → Back to f2 function  
print('End')                   # End


#  Find  outputs  (Home  work)

def  f1():
	print('f1  function')            # f1 function

def   f2 (fun):
	print('f2  function')            # (Not executed due to error)
	fun()
	print('Back  to  f2  function')

# end of the function

print('Begin')                     # Begin
f2(f1())                          # f1 function → then ERROR
print('End')                      # error(Not executed)

# Find  outputs (Home  work)

def   outer():
	print('Outer  Function')        # Outer Function
	def  inner():
		print('Inner function')
	return   inner

# End  of  the  function

fun = outer()                      # Outer Function
print('Hello')                     # Hello
fun()                              # Inner function
print('Bye')                       # Bye
inner()                            # ERROR (inner not defined)


# Find  outputs (Home  work)

def  outer(x):
	print('Outer  Function')        # Outer Function
	def  inner1():
		print('1st  inner  function')
	def  inner2():
		print("2nd  inner  function")
	if   x == 10:
		return  inner1
	else:
		return  inner2

# End  of  the  outer  function

f1 = outer(10)                    # Outer Function
f2 = outer(20)                    # Outer Function
f1()                              # 1st inner function
f2()                              # 2nd inner function


# Find  outputs  (Home  work)

def   outer(msg):
	def  inner():
		print(msg)
	return  inner

# End  of  the  function

hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()                          # Hi
hello_fun()                       # Hello


#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?

def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner

def  f1():
        return  10

# End  of  the  function

f1 = decor(f1)     # manually decorating f1
print(f1())        # calling inner()

#Out put
#12



# Find  outputs(Home  work)

def   decor(fun):
	print(fun._name_)              # wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)  # Hello Python
		else:
			fun(name)              # Hi Java
	return  inner

@decor
def    wish(name):
        print('Hi' , name)        # Hi <name>

# End  of  the  function

wish('Python')                    # Hello Python
wish('Java')                      # Hi Java



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

print(div(10 , 3))        # 3.3333333333333335
print(div(10 , 0))        # Division by 0 is not permitted
print(inner(10 , 3))      # ERROR



#  Find  outputs (Home  work)

def   decor(fun):
	def   inner():
		print(F'Decorating  {fun.__name__}  function')   # Decorating f1 function
		fun()                                           # Hello
		print('Decoration  is  finished')               # Decoration is finished
	return  inner

@decor
def   f1():
	print('Hello')                                     # Hello

# End  of  the  function

f1()                                                 # Decorating f1 function → Hello → Decoration is finished
print('Bye')                                         # Bye

#out put
Decorating f1 function
Hello
Decoration is finished
Bye




# Most tricky program

def   decor(fun):
	print(fun.__name__)                # f1 / f2 / f3 / f4 (at decoration time)

	def   inner(*x):  
		print(x)                      # arguments tuple
		fun(*x)                       # actual function call
		print('End  of  decoration')  # End of decoration
	return  inner

@decor
def   f1(x):
	print('f1  function  :  ' , x)     # f1 function : x

@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )  # f2 function : x y

@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)  # f3 function : x y z

@decor
def   f4():
	print('f4 function')               # f4 function

# end of function

f1(10)                               # (10,) → f1 function : 10 → End of decoration
f2(25 , 10.8)                        # (25,10.8) → f2 function → End of decoration
f3('Hyd' ,  True  , 3 + 4j)          # ('Hyd',True,(3+4j)) → f3 → End
f4()                                 # () → f4 function → End
#out put
f1
f2
f3
f4
(10,)
f1  function  :   10
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
		x = fun()                   # 10
		return  x * x              # 100
	return  inner1

def   double(fun):
	def  inner2():
		y = fun()                  # 100
		return  2 * y             # 200
	return   inner2

@double
@square
def  num():
	return  10

#end of the function

print(num())                       # 200


