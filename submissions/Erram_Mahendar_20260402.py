# Find outputs
def f1():
 a = 3
 if a:
  print(a) # 3 
  a = a - 1 # 2
  f1() 
  print('Hello')
  print('Hi')
  print(a)
 print('Bye')
# End of the function
a = 3
f1()
print('End')


'''
3
2
1
Bye 
Hello
Hi
0
Bye 
Hello
Hi
0
Bye 
Hello
Hi
0
Bye 
End
'''def f1():
print('f1 function')
def f2(fun):
print('f2 function')
fun()
print('Back to f2 function')
# end of the function
print('Begin')#Begin
f2(f1)#f2 function f1 function Back to f2 function
print('End')#end


# Find outputs (Home work)
def f1():
print('f1 function')
def f2 (fun):
print('f2 function')
fun()
print('Back to f2 function')
# end of the function
print('Begin')#begin
f2(f1())#f1 function f2 function
print('End')#end

# Find outputs (Home work)
def outer():
print('Outer Function')#Outer Function
def inner():
print('Inner function')
return inner
# End of the function
fun = outer()#outer
print('Hello')#Hello
fun()#Inner function
print('Bye')#Bye
inner()#error



# Find outputs (Home work)
def outer(x):
print('Outer Function')#Outer Function
def inner1():
print('1st inner function')
# End of inner1 function
def inner2():
print("2nd inner function")
# End of inner2 function
if x == 10:
return inner1
else:
return inner2
# End of the outer function
f1 = outer(10)#inner1
f2 = outer(20)#inner2
f1()#1st inner function
f2()#2nd inner function


# Find outputs (Home work)
def outer(msg):
def inner():
print(msg)
return inner
# End of the function
hi_fun = outer('Hi')#inner
hello_fun = outer('Hello')
hi_fun()#Hi
hello_fun()#Hello

# How to call f1() function when @decor tag is missing ?
def decor(fun):
def inner():
x = fun()
return x + 2
return inner
def f1():
return 10
# End of the function
f1 = decor(f1)#inner
print(f1())#12


# Find outputs(Home work)
def decor(fun):
print(fun . _name_)#wish
def inner(name):
if name == 'Python':
print('Hello' , name)
else:
fun(name)
return inner
@decor# wish = inner
def wish(name):
print('Hi' , name)
# End of the function
wish('Python')#Hello Python
wish('Java')#Hi Java


# Find outputs(Home work)
def decor(fun):#decor(div)
def inner(x , y):
try:
return fun(x , y)
except:
return 'Division by 0 is not permitted'
return inner
@decor#div = inner
def div(a , b):
return a / b
# End of the function
print(div(10 , 3))#10/3
print(div(10 , 0))#'Division by 0 is not permitted'
print(inner(10 , 3))#error



# Modify following div function such that both div(9 , 2) and div(2 , 9) should return 4.5 only
def decor(fun):
def inner(x , y):
if x>y:
return fun(x , y)
else:
return fun(y,x)
return inner
@decor
def div(a , b):
return a /b
print(div(9 , 2)) # 4.5
print(div(2 , 9)) # 4.5



# Find outputs (Home work)
def decor(fun):#decor(f1)
def inner():
print(F'Decorating {fun . _name_} function')#Decorating inner function
fun()#Hello
print('Decoration is finished')#Decoration is finished
return inner
@decor#f1 = inner
def f1():
print('Hello')
# End of the function
f1()
print('Bye')



# Most tricky program
# Same decorator to multiple functions with different signatures
def decor(fun):
print(fun . _name_)
def inner(*x): # * is var-arg parameter
print(x)
fun(*x) # Unpacks object 'x'
print('End of decoration')
return inner
@decor#f1= inner
def f1(x):
print('f1 function : ' , x)
@decor#f2= inner
def f2(x , y):
print('f2 function : ' , x , y )
@decor#f3= inner
def f3(x , y , z):
print('f3 function : ' , x , y , z)
@decor#f4=inner
def f4():
print('f4 function')
# end of function
f1(10)#(10,) f1 function : 10 End of decoration
f2(25 , 10.8)#(25 , 10.8) f2 function : 25 10.8 End of decoration
f3('Hyd' , True , 3 + 4j)#('Hyd' , True , 3 + 4j) f3 function : ('Hyd' , True , 3 + 4j) End of decoration
f4()#() f4 function
#f1 f2 f3 f4

# Find outputs (Home work)
def square(fun):
def inner1():
x = fun()#10
return x * x#20
return inner1
def double(fun):
def inner2():
y = fun()#20
return 2 * y
return inner2
@double#num=double(square(num))400---->double(inner1)#20----->inner2
@square
def num():
return 10
#end of the function
print(num())#400