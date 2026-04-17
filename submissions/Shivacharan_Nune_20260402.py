#1)  Find  outputs  (Home  work)
def  f1():
	print('f1  function')  #f1 function is printed and returns None
def   f2(fun):             #fun actual parameter points to f1 function.
	print('f2  function')  #f2 function
	fun()                  #f1 function is called.
	print('Back  to  f2  function') #Back  to  f2  function is printed
# end of the function
print('Begin')         #Begin is printed.
f2(f1)                 #f1 function is passed as argument to f2 funtion and it returns None
print('End')

'''
Begin
f2 function
f1 function
Back  to  f2  function
End
'''
#---------------------------------------------------------------------
#2)#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')  #prints f1 function and returns None
def   f2 (fun): #fun points to None object
	print('f2  function')  #prints f2 function
	#fun()  #Error
	print('Back  to  f2  function') #Back  to  f2  function is printed
# end of the function
print('Begin') #Begin is printed and execution starts here
f2(f1())       #the output of f1 function is passed to f2 functio i.e None-->f2(None)
print('End')

'''
Begin
f1 function
f2 function
Back  to  f2  function
End
'''
#---------------------------------------------------------------------
# Find  outputs (Home  work)
def   outer():
	print('Outer  Function') #prints Outer function and returns None
	def  inner():
		print('Inner function')#prints Inner function and returns None
	return   inner
# End  of  the  function
fun = outer() #start execution here=>fun points to inner function
print('Hello') #Hello
fun() #None is returned
print('Bye') #prints Bye
#inner() #innner function cannaot be called direclty like that.

'''
Outer function
Hello
Inner function
Bye
'''
#---------------------------------------------------------------------
# Find  outputs (Home  work)
def  outer(x): #x points to 10 ,later x points to 20
	print('Outer  Function') #Outer function and returns None
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
f1 = outer(10)   #execution starts here:outer function is called and 10 is copied to  outer outer function and f1 points to inner1 function
f2 = outer(20)   #:outer function is called and 20 is copied to  outer outer function and f2 points to inner2 function 
f1() #executes inner1 function
f2() #executes inner2 function

'''
Outer function
outer function
1st  inner  function
2nd  inner  function
'''
#---------------------------------------------------------------------
# Find  outputs  (Home  work)
def   outer(msg): #msg=Hi,later msg=Hello
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')#hi_fun points to inner
hello_fun = outer('Hello') #hello_fun points to inner
hi_fun() #
hello_fun()
'''
Hi
Hello
'''
#------------------------------------------------
#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): #fun points to f1
	def   inner():
		x = fun() #x=10
		return   x + 2 #12
	return  inner  
def  f1():
        return  10
# End  of  the  function
f1 = decor(f1) #f1 points to inner
print(f1()) #12
'''
12
'''
#---------------------------------------------------------
# Find  outputs(Home  work)
def   decor(fun): #fun points to wish
	#print(fun . _name_) #Error
	def    inner(name): #name points to 'Python',later name points to 'Java'
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)  
	return  inner
@decor   #wish=decor(wish)=>wish=inner
def  wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')#inner('Python')=>None is returned
wish('Java')#inner('Java')=>None is returned
'''
Hello,Python
Hi,Java
'''
#---------------------------------------------------
# Find  outputs(Home  work)
def   decor(fun): #fun points to div
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor  # div=inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) #inner(10,3)=>3.33
print(div(10 , 0))#inner(10,0)=
print(inner(10 , 3))#cannot be direclty called.

'''
3.3333333333333335
Division   by  0  is  not  permitted
'''
#------------------------------------------------------------
# Modify  following  div  function  such  that  both  div(9 , 2)  and  div(2 , 9)  should  return  4.5  only
def  decor(fun): #fun=div
    def inner(x,y):
        if  x>y:
            return fun(x,y)
        else:
            return fun(y,x)
    return inner
@decor #div=decor(div)=>div=inner
def  div(a , b):
    return   a /b
print(div(9 , 2))  #  4.5
print(div(2 , 9))  # 4.5
#---------------------------------------------------------
def   decor(fun):
	def   inner():
		#print(F'Decorating  {fun . _name_}  function') #Error
		fun()
		print('Decoration  is  finished')
	return  inner
@decor   #f1=inner
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')

'''
Hello
Decoration  is  finished
Bye

'''
#--------------------------------------------------
# Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun): #fun=f1
	print(fun . _name_)
	def   inner(*x):  #  *  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor   #f1=inner
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

'''
(10,)
f1  function  :  ' , 10
End  of  decoration
(25,10.8)
f2  function  :  ' , 25 , 10.8
End  of  decoration
('Hyd' ,  True  , 3 + 4j)
f3 function : ' , 'Hyd',True,3+4j
End  of  decoration
()
f4 function
End  of  decoration
'''
#--------------------------------------
# Find  outputs  (Home  work)
def  square(fun): #fun points to num 
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):#fun points to 
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double #num=double(square(num))==>double(inner1)
@square #num=square(num)
def  num():
	return  10
#end of the function
print(num()) #double(inner1)

'''
200
'''
