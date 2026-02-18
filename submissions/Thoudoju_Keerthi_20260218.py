#  Find  outputs
a = 25
print(id(a)) # <Address of object a>
a = 35
print(id(a)) # <Address of different object a>
# Find  outputs (Home  work)
a = 25.7
print(id(a)) # <Address of same object a>
print(a) # 25.7
a = 35.6
print(id(a)) # <Address of  object 35.6>
print(a) # 35.6
b = True
print(id(b))  # <Address of  object True >
b = False
print(id(b)) # <Address of  object False >
c = None
print(id(c)) # <Address of  object None >
c = None
print(id(c))  # <Address of  object None >


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # <Address of  object Hyd >
a[1] = 'e'  # Error string is immutable 
a = 'Sec'
print(id(a)) # <Address of  object Sec >
b = (10 , 20 , 15 , 18)
print(id(b)) # <Address of  tuple object b >
b[2] = 19 # Error tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b))  # <Address of   different tuple object b >
c = range(5)
print(id(c)) # <Address of range object c >
c[3] = 10 # Error range cannot be modified
c = range(5)
print(id(c)) # <Address of different range object c >


# Find  outputs  (Home  work)
a = 25
b = 25 # reference is modified a is automatically deleted
print(a  is  b) # True due to same reference
c = 'Hyd' 
d = 'Hyd'  # reference is modified d is automatically deleted
print(c  is  d) # True due to same reference
e = False
f = False # reference is modified e is automatically deleted
print(e  is  f) # True due to same reference
g = range(10)
h = range(10) # creates new range object
print(g  is  h)  # false range creates new object



 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # false list creates new object
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # false dictionary creates new object
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  # True refernce is modified
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # false dictionary creates new object



# Find outputs (Home work)
print(10 + 20) # 30 
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # Not supported
print({10 : 'Hyd'} + {20 : 'Sec'}) # Not supported
print(range(4) + range(5)) # Range objects does not support concatenation
print(10 + '20')  # Error not supported
print([10 , 20 , 30] + 5) # Error can add 5 to list
print([10 , 20 , 30] + (40 , 50 , 60)) # can combine list and tuple, tuple must be converted to tuple


 # Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # -21 + 20j
print(3 + 4j * 5 + 6j) # 3 + 26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [ 10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # second parameter must be integer
print({10 , 20 , 15} * 2) # Error does not allow duplicates
print({10 : 20 , 30 : 40} * 2) #  Error does not allow duplicates
print([10] * [20]) # seq * seq is not allowed