# 1. f2(f1) - Function as argument
def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
print('Begin')
f2(f1)
print('End')
# OUTPUT:
# Begin
# f2  function
# f1  function
# Back  to  f2  function
# End

print("\n" + "="*50 + "\n")

# 2. f2(f1()) - ERROR: NoneType not callable
def f1():
    print('f1  function')
def f2(fun):
    print('f2  function')
    fun()
    print('Back  to  f2  function')
print('Begin')
# f2(f1())  # ERROR: TypeError: 'NoneType' object is not callable
print('End')
# OUTPUT: TypeError (f1() returns None)

print("\n" + "="*50 + "\n")

# 3. Closure - outer returns inner
def outer():
    print('Outer  Function')
    def inner():
        print('Inner function')
    return inner
fun = outer()
print('Hello')
fun()
print('Bye')
# OUTPUT:
# Outer  Function
# Hello
# Inner function
# Bye

print("\n" + "="*50 + "\n")

# 4. outer(x) returns different inners
def outer(x):
    print('Outer  Function')
    def inner1():
        print('1st  inner  function')
    def inner2():
        print("2nd  inner  function")
    if x == 10:
        return inner1
    else:
        return inner2
f1 = outer(10)
f2 = outer(20)
f1()
f2()
# OUTPUT:
# Outer  Function
# 1st  inner  function
# Outer  Function
# 2nd  inner  function

print("\n" + "="*50 + "\n")

# 5. Closures capture msg
def outer(msg):
    def inner():
        print(msg)
    return inner
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
# OUTPUT:
# Hi
# Hello

print("\n" + "="*50 + "\n")

# 6. Manual decorator (no @decor)
def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner
def f1():
    return 10
f1 = decor(f1)
print(f1())  # 12
# To call without @decor: f1 = decor(f1)

print("\n" + "="*50 + "\n")

# 7. Decorator prints function name
def decor(fun):
    print(fun.__name__)
    def inner(name):
        if name == 'Python':
            print('Hello', name)
        else:
            fun(name)
    return inner
@decor
def wish(name):
    print('Hi', name)
wish('Python')
wish('Java')
# OUTPUT:
# wish
# Hello Python
# Hi Java

print("\n" + "="*50 + "\n")

# 8. Exception handling decorator
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
print(div(10, 3))      # 3.3333333333333335
print(div(10, 0))      # Division by 0 is not permitted
# print(inner(10, 3))  # NameError: inner not defined

print("\n" + "="*50 + "\n")

# 9. Always return 4.5 decorator
def decor(fun):
    def inner(a, b):
        return 4.5
    return inner
@decor
def div(a, b):
    return a / b
print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5

print("\n" + "="*50 + "\n")

# 10. Print decorator
def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')
        fun()
        print('Decoration is finished')
    return inner
@decor
def f1():
    print('Hello')
f1()
print('Bye')
# OUTPUT:
# Decorating f1 function
# Hello
# Decoration is finished
# Bye

print("\n" + "="*50 + "\n")

# 11. Same decorator for different signatures (*args)
def decor(fun):
    print(fun.__name__)
    def inner(*x):
        print(x)
        fun(*x)
        print('End of decoration')
    return inner
@decor
def f1(x):
    print('f1  function : ', x)
@decor
def f2(x, y):
    print('f2  function : ', x, y)
@decor
def f3(x, y, z):
    print('f3 function : ', x, y, z)
@decor
def f4():
    print('f4 function')
f1(10)
f2(25, 10.8)
f3('Hyd', True, 3 + 4j)
f4()
# OUTPUT shows all function names + args handling

print("\n" + "="*50 + "\n")

# 12. Chained decorators @double @square
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
print(num())  # 200 (square(10)=100, double(100)=200)

