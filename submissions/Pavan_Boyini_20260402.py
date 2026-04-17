#Find outputs (Home work)
def f1():
    print('f1 function')
def f2(fun):
    print('f2 function')
    fun()
    print('Back to f2 function')
# end of the function
print('Begin') # Begin
f2(f1) 
# f2 function
# f1 function
# Back to f2 function
print('End') # End





#Find outputs (Home work)
def f1():
    print('f1 function')
def f2(fun):
    print('f2 function')
    fun()
    print('Back to f2 function')
# end of the function
print('Begin') # Begin
# f2(f1()) 
# f1 function
# f2 function
# Error as 'NoneType' object is not callable
# Reason: f1() is called first; it prints 'f1 function' and returns None. 
# f2 then receives None as 'fun' and tries to call it (None()), causing the error.
print('End')




#Find outputs (Home work)
def outer():
    print('Outer Function')
    def inner():
        print('Inner function')
    return inner
# End of the function
fun = outer() # Outer Function
print('Hello') # Hello
fun() # Inner function
print('Bye') # Bye
# inner() 
# Error as name 'inner' is not defined
# Reason: 'inner' is a local function defined inside 'outer' and cannot be accessed globally.


#Find outputs (Home work)
def outer(x):
    print('Outer Function')
    def inner1():
        print('1st inner function')
    def inner2():
        print("2nd inner function")
    if x == 10:
        return inner1
    else:
        return inner2
# End of the outer function
f1 = outer(10) # Outer Function
f2 = outer(20) # Outer Function
f1() # 1st inner function
f2() # 2nd inner function




#Find outputs (Home work)
def outer(msg):
    def inner():
        print(msg)
    return inner
# End of the function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun() # Hi
hello_fun() # Hello




#Find outputs (Home work)
def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner
def f1():
    return 10
# End of the function
f1 = decor(f1) # Manually decorating the function
print(f1()) # 12




#Find outputs (Home work)
def decor(fun):
    print(fun.__name__) # OUTPUT: wish
    # Reason: __name__ returns the string name of the function object 'fun'.
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
wish('Java')   # Hi Java




#Find outputs (Home work)
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
# End of the function
print(div(10, 3)) # 3.3333333333333335
print(div(10, 0)) # Division by 0 is not permitted
# print(inner(10, 3)) 
# Error as name 'inner' is not defined
# Reason: 'inner' exists only inside the 'decor' function scope.
 


# Modify following div function such that both div(9,2) and div(2,9) should return 4.5 only
def decor(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a # Swap to ensure larger number is divided by smaller
        return fun(a, b)
    return inner
@decor
def div(a, b):
    return a / b
print(div(9, 2)) # 4.5
print(div(2, 9)) # 4.5

#10
#Find outputs (Home work)
def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function') 
        # OUTPUT: Decorating f1 function
        fun()
        print('Decoration is finished')
    return inner

@decor
def f1():
    print('Hello')

f1() 
# Full Output for f1():
# Decorating f1 function
# Hello
# Decoration is finished

print('Bye') # Bye



# Most tricky program
# Same decorator to multiple functions with different signatures
def decor(fun):
    print(fun.__name__) 
    # OUTPUT when script loads: 
    # f1
    # f2
    # f3
    # f4
    # (Note: These print immediately when the @decor line is read, not when called)
    
    def inner(*x): 
        print(x)
        fun(*x) 
        print('End of decoration')
    return inner

@decor
def f1(x):
    print('f1 function : ', x)

@decor
def f2(x, y):
    print('f2 function : ', x, y)

f1(10) 
# Output:(10,)
# f1 function : 10
# End of decoration

#Find outputs (Home work)
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
@double # Second decoration
@square # First decoration
def num():
    return 10
# Logic: double(square(num)) -> double(100) -> 200
print(num()) # 200