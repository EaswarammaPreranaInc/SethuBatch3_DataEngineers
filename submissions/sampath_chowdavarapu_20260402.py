#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')# f1 function
def   f2(fun):
	print('f2  function')# f2 function
	fun() # calls f1()
	print('Back  to  f2  function')# Back to f2 function

# end of the function
print('Begin')# Begin
f2(f1)
print('End')# End

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Find  outputs  (Home  work)
def  f1():
	print('f1  function') # f1 function
def   f2 (fun):
	print('f2  function')# f2 function
	fun()#Error
	print('Back  to  f2  function')
# end of the function
print('Begin') # Begin
f2(f1()) # first f1() executes ->prints and returns None -> fun = None -> TypeError
print('End')
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def outer():
    print('Outer Function') # Outer Function
    def inner():
        print('Inner function')
    return inner

fun = outer() # Outer Function → fun = inner
print('Hello') # Hello
fun() # Inner function
print('Bye') # Bye
inner() # NameError

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def outer(x):
    print('Outer Function') # Outer Function
    def inner1():
        print('1st inner function')
    def inner2():
        print("2nd inner function")
    if x == 10:
        return inner1
    else:
        return inner2

f1 = outer(10) # Outer Function → f1 = inner1
f2 = outer(20) # Outer Function → f2 = inner2
f1() # 1st inner function
f2() # 2nd inner function

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def outer(msg):
    def inner():
        print(msg)
    return inner

hi_fun = outer('Hi') # inner(msg='Hi')
hello_fun = outer('Hello') # inner(msg='Hello')
hi_fun() # Hi
hello_fun() # Hello

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner

def f1():
    return 10

f1 = decor(f1) # f1 = inner
print(f1()) # 10 + 2 = 12

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decor(fun):
    print(fun._name_) # wish
    def inner(name):
        if name == 'Python':
            print('Hello', name)
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print('Hi', name)

wish('Python') # Hello Python
wish('Java') # Hi Java

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decor(fun):
    def inner(x, y):
        try:
            return fun(x, y)
        except:
            return 'Division by 0 is not permitted'
    return inner

@decor
def div(a, b):
    return a / b

print(div(10, 3)) # 10/3 = 3.333...
print(div(10, 0)) # Exception → handled → message
print(inner(10, 3)) # NameError

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decor(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2)) # 4.5
print(div(2, 9)) # swap → 9/2 = 4.5

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decor(fun):
    def inner():
        print(f'Decorating {fun._name_} function') # Decorating f1 function
        fun() # Hello
        print('Decoration is finished') # Decoration is finished
    return inner

@decor
def f1():
    print('Hello')

f1() # full execution
print('Bye') # Bye

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def decor(fun):
    print(fun._name_) # f1, f2, f3, f4 (at definition time)
    def inner(*x):
        print(x)
        fun(*x)
        print('End of decoration')
    return inner

@decor
def f1(x):
    print('f1 function :', x)

@decor
def f2(x, y):
    print('f2 function :', x, y)

@decor
def f3(x, y, z):
    print('f3 function :', x, y, z)

@decor
def f4():
    print('f4 function')

f1(10) # (10,) → f1 function : 10 → End
f2(25, 10.8) # (25,10.8) → f2 → End
f3('Hyd', True, 3+4j) # (...) → f3 → End
f4() # () → f4 → End

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def square(fun):
    def inner1():
        x = fun()
        return x * x
    return inner1

def double(fun):
    def inner2():
        y = fun()
        return 2 * y
    return inner2

@double
@square
def num():
    return 10

print(num()) # square → 100 → double → 200

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

