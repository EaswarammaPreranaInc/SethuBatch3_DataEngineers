def f1():
    print('Hyd') # Hyd
    print('Sec') # Sec
    print('Cyb') # Cyb


print('Begin') # Begin
x = f1() # Hyd Sec Cyb (printed), x = None
print(x) # None
print(type(x)) # <class 'NoneType'>
print('End') # End


*********


def f1():
    return 10, 20, 30


x = f1()
print(x) # (10, 20, 30)
print(type(x)) # <class 'tuple'>


a, b, c = f1()
print(a) # 10
print(b) # 20
print(c) # 30


print('for loop') # for loop
for k in f1():
    print(k) # 10
                     # 20
                     # 30


**********
def f1():
    return 10 # function exits here
    return 20 # not executed
    return 30 # not executed


print('Begin') # Begin
x = f1()
print(x) # 10
print('End') # End


return 100 # ERROR 




**********


f1() # ERROR 


def f1():
    print('Hello')


print(f1()) # Hello \n None
print(f1) # <function f1 at memory_address>


**"********


print('Hello') # Hello


def f1():
    print('f1 function') # f1 function


print('Hi') # Hi
print(f1()) # f1 function \n None
print(f1) # <function f1 at memory_address>
print('Bye') # Bye


************


def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')


print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # some memory address (varies every run)
print('End') # End

