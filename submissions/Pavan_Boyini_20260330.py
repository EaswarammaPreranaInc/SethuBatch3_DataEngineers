
# Tricky program
# Find outputs
a = 10
b = 7
x = lambda a, b : a + b, a - b, a * b, a / b 
print(type(x))       # <class 'tuple'>
print(x)             # (<function <lambda> at ...>, 3, 70, 1.4285714)
for y in x:
    print(y)         # First loop: <function <lambda> at ...>, Second: 3, Third: 70, Fourth: 1.4285714
print(x[0](9, 2))    # 11 (Calls the lambda function with 9 and 2)
print(x[1])          # 3 (The result of the global a - b calculated at assignment)
# print(x())         # Error as 'tuple' object is not callable. x is a tuple, not a function.



# Tricky program
# Find outputs
a = lambda : print('Hyd'); print('Sec'); print('Cyb') 
# Sec
# Cyb
print(a()) # Hyd <next line> None (Because print('Hyd') returns None)



# Find outputs (Home work)
a = lambda : 'Hyd'; print('Sec'); print('Cyb')
# Sec
# Cyb
print(a()) # Hyd



# Find outputs (Home work)
a = lambda : print('Hyd'), print('Sec'), print('Cyb')
# Sec
# Cyb
print(type(a))   # <class 'tuple'>
print(a)         # (<function <lambda> at ...>, None, None)
for x in a:
    print(x)     # First: <function <lambda> at ...>, Second: None, Third: None
# a()            # Error as 'tuple' object is not callable.
print(a[0]())    # Hyd \n None (Executes the lambda, prints 'Hyd', returns None)
