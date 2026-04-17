#  Find  outputs
a = 25
print(id(a)) # Address of object '25'(eg. 12784634)
a = 35
print(id(a)) # Address of object '35'(eg. 27363829)

# Find  outputs 
a = 25.7
print(id(a)) # Address of object '25.7' (eg. 1232534)
print(a) # 25.7
a = 35.6
print(id(a)) # Address of object '35.6' (eg. 72532728)
print(a) # 35.6
b = True
print(id(b)) # Address of object 'True'
b = False
print(id(b)) # Address of object 'False'
c = None
print(id(c)) # Address of object 'None'
#  Find  outputs  
a = 'Hyd'
print(id(a)) Address of object 'Hyd'
a[1] = 'e' # Error 'str' object does not support item assignment 
a = 'Sec'
print(id(a)) # Address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of object tuple
b[2] = 19 # Error 'tuple' object does not support item assignment
b = (30 , 40 , 35 , 32)
print(id(b)) # Address of object tuple
c = range(5)
print(id(c)) # Address of object range(5) (eg. 1968156247680)
c[3] = 10  # Error 'range' object does not support item assignment
c = range(5)
print(id(c)) # Address of object range(5) (eg. 1968156247648)

# Find  outputs  
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # False

#Find  outputs
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False

# Find outputs 
print(10 + 20) # 30
print(10.8 + 20.6) # 31.400000000000002
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1+0=1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') #'1020'
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None) 
print({10 , 20} + {30 , 40}) # Error unsupported operand type(s) for +: 'set' and 'set'
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error unsupported operand type(s) for +: 'dict' and 'dict'
print(range(4) + range(5)) # Error unsupported operand type(s) for +: 'range' and 'range'
print(10 + '20') # Error unsupported operand type(s) for +: 'int' and 'str'
print([10 , 20 , 30] + 5) # Error can only concatenate list (not "int") to list
print([10 , 20 , 30] + (40 , 50 , 60)) # Error can only concatenate list (not "tuple") to list

# Find outputs 
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # 3+26j
print('25' * 3) # '252525'
print(3 * '25') # '252525'
print('Hyd' * 4) # 'HydHydHydHyd'
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error can't multiply sequence by non-int of type 'float'
print({10 , 20 , 15} * 2) # Error unsupported operand type(s) for *: 'set' and 'int'
print({10 : 20 , 30 : 40} * 2) # Error unsupported operand type(s) for *: 'dict' and 'int'
print([10] * [20]) # Error can't multiply sequence by non-int of type 'list'