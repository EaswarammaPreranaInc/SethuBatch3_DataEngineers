# 1. OUTPUT
# Error: inner() is not defined globally (NameError occurs before finishing)

# Expected execution till error:
# Begin
# Outer function
# Hello
# Inner function
# Back to outer function
# Hi
# NameError: name 'inner' is not defined


# 2. OUTPUT
def f1(a):
    def f2():
        return 10
    return f2() + 20 + a

print(f1(30))
# Output: 60


# 3. OUTPUT
print('Begin')
def outer():
    print('Outer function')
    def inner1():
        print('1st inner function')
    def inner2():
        print('2nd inner function')
    print('Hi')
    inner2()
    print('Hello')
    inner1()
    print('Back to outer function')

outer()
print('Bye')

# Output:
# Begin
# Outer function
# Hi
# 2nd inner function
# Hello
# 1st inner function
# Back to outer function
# Bye


# 4. OUTPUT
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
        print(globals()['x'])
    inner()

outer()
print('Bye')

# Output:
# 30
# 10
# Bye


# 5. OUTPUT
x = 10
def outer():
    x = 20
    def inner():
        print(x)
        print(globals()['x'])
    inner()

outer()

# Output:
# 20
# 10


# 6. OUTPUT
x = 10
def outer():
    def inner():
        print(x)
    inner()

outer()

# Output:
# 10


# 7. OUTPUT
def outer():
    x = 10
    def inner():
        x = 20
        print(x)
        x += 7
    print(x)
    x += 5
    inner()
    print(x)

outer()
print('Bye')

# Output:
# 10
# 20
# 15
# Bye


# 8. OUTPUT
def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)

outer()
print(x)

# Output:
# 10
# 15
# 20
# 25
# NameError: x is not defined


# 9. ERROR
# SyntaxError: nonlocal used after accessing variable


# 10. OUTPUT
def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)

outer()
print(x)

# Output:
# 10
# 20
# 15
# 25


# 11. ERROR
# SyntaxError: no binding for nonlocal 'x' found


# 12. OUTPUT
def outer():
    def inner():
        global x
        x = 20
        print(x)
        x = x + 5
    inner()
    print(x)

outer()
print(x)

# Output:
# 20
# 25
# 25


# 13. ERROR
def f1():
    nonlocal x

# Error: SyntaxError (nonlocal outside nested function)


# 14. OUTPUT
def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)
    print(a, b)
    inner()
    print(a, b)

outer()

# Output:
# 10 20
# 100 200
# 100 20


# 15. OUTPUT
def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x

print(f1())

# Output:
# Hello


# 16. ERROR
def fun():
    x = 10
    def gun():
        x = x + 20
        print(x)
    gun()

# Error: UnboundLocalError


# 17. ERROR
x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x

# Error: SyntaxError (both global and nonlocal for same variable)


# 18. OUTPUT
def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)
        f3()
    f2()

f1()

# Output:
# 10