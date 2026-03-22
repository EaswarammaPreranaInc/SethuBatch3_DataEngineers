# Find  outputs  (Home  work)

def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
# End of the function

print('Begin')        # Begin
x = f1()              # Hyd
                       # Sec
                       # Cyb
print(x)              # None
print(type(x))        # <class 'NoneType'>
print('End')          # End


# Find  outputs  (Home  work)

def f1():
    return 10 , 20 , 30
# End of the function

x = f1()
print(x)              # (10, 20, 30)
print(type(x))        # <class 'tuple'>

a , b , c = f1()
print(a)              # 10
print(b)              # 20
print(c)              # 30

print('for loop')     # for loop
for k in f1():
    print(k)          # 10
                      # 20
                      # 30


# Find  outputs

def f1():
    return 10
    return 20
    return 30
# End of the function

print('Begin')        # Begin
x = f1()
print(x)              # 10
print('End')          # End
return 100            # error


# Find  outputs

f1()                  # error (function not defined yet)

def f1():
    print('Hello')

print(f1())           # Hello
                      # None
print(f1)             # <function f1 at ...>


# Find  outputs  (Home  work)

print('Hello')        # Hello

def f1():
    print('f1 function')
# End of function

print('Hi')           # Hi
print(f1())           # f1 function
                      # None
print(f1)             # <function f1 at ...>
print('Bye')          # Bye


# Find  outputs

def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
# End of the function

print('Begin')        # Begin
print(type(f1))       # <class 'function'>
print(id(f1))         # <id>
print('End')          # End
