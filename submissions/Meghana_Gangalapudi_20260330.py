a = 10
b = 7
x = lambda a, b : a + b , a - b , a * b , a / b 

print(type(x))        # <class 'tuple'>
print(x)              # (<function <lambda>>, 3, 70, 1.4285714285714286)

for y in x:
    print(y)          # 1st loop: <function <lambda>>
                      # 2nd loop: 3
                      # 3rd loop: 70
                      # 4th loop: 1.4285714285714286

print(x[0](9, 2))     # 11
print(x[1])           # 3
print(x())            # Error






a = lambda : print('Hyd') ; print('Sec'); print('Cyb') # Defines lambda; Prints 'Sec'; Prints 'Cyb'
print(a())       # Calls lambda; Prints 'Hyd'; Prints None






a = lambda : print('Hyd') ; print('Sec'); print('Cyb') # Defines lambda; Prints 'Sec'; Prints 'Cyb'
print(a())                                 # Calls lambda; Prints 'Hyd'; Prints





a = lambda : print('Hyd') , print('Sec') , print('Cyb')
# Output: Sec
# Output: Cyb

print(type(a))        # <class 'tuple'>
print(a)              # (<function <lambda> at address>, None, None)

for x in a:
    print(x)          # <function <lambda> at address>
                      # None
                      # None

a()                 # Error

print(a[0]())         # Hyd
                      # None
