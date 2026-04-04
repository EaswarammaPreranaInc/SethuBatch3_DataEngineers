def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')

'''
begin
f2 function
f1 function
back to f2 function
'''

def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
#f2(f1())
print('End')

'''
begin
f1 function
f2 function 
error
'''

def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()
print('Bye')
#inner() #error
'''
output:

outer function
hello
innerfunction
bye 
error


'''
 

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
f1 = outer(10)
f2 = outer(20)
f1()
f2()
'''
output :
outer function
outer function
1st inner function
2nd inner function


'''

def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()  # hi
hello_fun() # hello
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
# End  of  the  function
print(f1())



def   decor(fun):
	print(fun . __name__)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor # wish =decor(wish)-->wish=inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python') 
wish('Java')

'''
wish
hello,Python
hello,Java

'''

def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor #div=decor(div)--->div=inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10 , 3)) error inner function can't be accessed directly
'''

3.3333
Division   by  0  is  not  permitted

'''


# Modify  following  div  function  such  that  both  div(9 , 2)  and  div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a,b):
		if a < b:
			a, b = b, a   # swap
		return fun(a,b)


	return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))  #  4.5
print(div(2 , 9))  # 4.5



def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #  *  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor # f1=decor(f1)--->f1=inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor # f2=decor(f3)--->f2=inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor # f3=decor(f3)--->f3=inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor # f4=decor(f4)--->f4=inner
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()

'''
(10)
f1  function  :  10
End  of  decoration
(25 , 10.8)
f2  function  : 25 10.8 
End  of  decoration
('Hyd' ,  True  , 3 + 4j)
f3 function : Hyd'   True   3 + 4j
End  of  decoration
()
f4 function
end of decoration
'''