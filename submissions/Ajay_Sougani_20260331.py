 
#   Find  outputs
def  f1():
	global  a
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1() # 3 2 1 Bye Hello hi 0 bye Hello Hi 0 bye Hello Hi 0 Bye
print('End') # End

#  Tricky  program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
# End  of  the  function
x = 10
f1(x , x := x + 1) # 43, 32, 21
print(x) # 11

# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3) # 3 2 1 0 0 1 2 3

#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # This  will  cause  a  RecursionError: maximum  recursion  depth  exceeded 

#  Find  outputs  (Home  work)
def  f1():
        print('f1    function')
def  f2():
        print('f2  function')
# End  of  the  function
f1() # f1    function
f2() # f2  function
print(f1  is  f2) # False
f2 = f1 
f2() # f1    function
print(f1  is  f2) # True
f2 = f1() # f1    function
print(f2) # None
f2() # TypeError: 'NoneType' object is not callable


# Find  outputs (Home  work)
# How  to  assign  ref  'p'  to  print()  function
p = print
p('Hello')
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('Hyderabad')
print = None
print('Hello')
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p('Hello')

# Find   outputs (Home  work)
# How  to  assign  ref  'x'  to  id()  function

#Find outputs (Home work)
def outer():
    print('Outer function')
    def inner():
        print('Inner function')
    #End of the function
    print('Hello')
    inner()
    print('Back to outer function')
# inner() # Error as name 'inner' is not defined (It's local to outer)



#Find outputs (Home work)
def f1(a):
    def f2():
        return 10
    #End of the function f2
    return f2() + 20 + a
#End of the function f1
print(f1(30)) # 60 (10 + 20 + 30)



#Find outputs (Home work)
def outer():
    print('Outer function')           # Outer function
    def inner1():
        print('1st inner function')   # Executed later via call
    def inner2():
        print('2nd inner function')   # Executed later via call
    print('Hi')                       # Hi
    inner2()                          # 2nd inner function
    print('Hello')                    # Hello
    inner1()                          # 1st inner function
    print('Back to outer function')   # Back to outer function
print('Begin')                        # Begin
outer()
print('Bye')                          # Bye



#Find outputs (Home work)
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x) # 30
        print(globals()['x']) # 10
    inner()
outer() # 30, 10
print('Bye')



#Find outputs (Home work)
x = 10
def outer():
    x = 20
    def inner():
        print(x) # 20 (Accesses enclosing x)
        print(globals()['x']) # 10
    inner()
outer()



#Find outputs (Home work)
x = 10
def outer():
    def inner():
        print(x) # 10 (Accesses global because no local x exists)
    inner()
outer()



#Find outputs (Home work)
def outer():
    x = 10
    def inner():
        x = 20        # Creates a NEW local x for inner()
        print(x)      # 20
        x += 7        # Only modifies inner's local x (becomes 27)
    # End of inner function
    print(x)          # 10
    x += 5            # outer's x becomes 15
    inner()
    print(x)          # 15 (outer's x remains unchanged by inner)
# End of the function
outer()
print('Bye')          # Bye



#Find outputs (Home work)
def outer():
    x = 10
    def inner():
        nonlocal x    # Links to outer's x
        print(x)      # 15 (current value of outer's x)
        x = 20        # Changes outer's x to 20
        print(x)      # 20
        x += 5        # Changes outer's x to 25
    # End of inner function
    print(x)          # 10
    x += 5            # outer's x becomes 15
    inner()
    print(x)          # 25 (modified by inner)
# End of outer function
outer()
print(x)            # Error as 'x' is not defined in the global scope.



#Find outputs (Home work)
def outer():
    x = 10
    def inner():
        # print(x)    # Error as name 'x' is used prior to nonlocal declaration
        nonlocal x
        x = 20
        print(x)
        x += 5
    # End of inner function
    print(x)
    x += 5
    inner()
    print(x)
# End of outer function
# outer()             # Error because program will crash during compilation/execution.



#Find outputs (Home work)
def outer():
    x = 10            # Enclosing variable 'x'
    def inner():
        global x      # This creates/references a GLOBAL 'x', not the 'x' in outer()
        x = 20        # Global x = 20
        print(x)      # 20
        x += 5        # Global x = 25
    # End of inner function
    print(x)          # 10 (Prints outer's x)
    x += 5            # outer's x becomes 15
    inner()           # Calls inner, which manipulates the GLOBAL x
    print(x)          # 15 (Prints outer's x; it was NOT changed by inner)
outer()
print(x)              # 25 (Prints the GLOBAL x created/modified by inner)



#Find outputs (Home work)
def outer():
    def inner():
        nonlocal x    # Error as there is no binding for nonlocal 'x' found
        x = 20
        print(x)
    # End of inner function
    inner()
    print(x)
outer()             # The code fails before it even runs.
print(x)            # This would also fail as 'x' is not global.




#Find outputs (Home work)
def outer():
    def inner():
        global x      # This tells Python to create/use 'x' at the module level
        x = 20        # Global x is now 20
        print(x)      # 20
        x = x + 5     # Global x becomes 25
    # End of inner function
    inner()           # Calls inner, creating the global x
    print(x)          # 25 (Accesses the global x because outer has no local x)
# End of the function
outer()               # Triggers the whole process
print(x)              # 25 (Accesses the same global x)



#Identify Error
def f1():
   nonlocal x # Error as nonlocal x used at module level (must be in nested function)



#Find outputs (Home work)
def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200 # New local b
        print(a, b) # 100 200
    #End of inner function
    print(a, b) # 10 20
    inner()
    print(a, b) # 100 20
#End of outer function
outer()



def f1():
    x = 'John'
    def f2():
        nonlocal x    # This links 'x' to the 'x' in f1's scope
        x = 'Hello'   # This changes the value of f1's 'x'
    # End of inner function
    f2()
    return x          # Returns the modified value
# End of outer function
print(f1())           # Hello



def fun():
    x = 10
    def gun():
        # Error as local variable 'x' referenced before assignment
        x = x + 20 
        print(x)
    # End of inner function
    gun()
# End of outer function
fun()



x = 10
def outer():
    x = 20
    def inner():
        global x      # Tells Python to look at the module level (10)
        nonlocal x    # Error as name 'x' is nonlocal and global



#Find outputs (Home work)
def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x) # 10
        f3()
    f2()
f1()
x = id
# How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
x = id(25)
# How  to  assign  ref  'p'  to  len()  function
p = len
# How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
p('Hyd')

