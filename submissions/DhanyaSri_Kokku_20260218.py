Home Work on Feb 18 2026
#  Find  outputs
a = 25
print(id(a)) # Address of int object 25
a = 35
print(id(a)) # Address of int object 35

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of float object 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # Address of float object 35.6
print(a) # 35.6
b = True
print(id(b)) # Address of bool object True
b = False
print(id(b)) # Address of bool object False
c = None
print(id(c)) # Address of None object
c = None
print(id(c)) # Address of None object

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # Address of str object
a[1] = 'e'   # Error strngs are immutable
a = 'Sec'
print(id(a)) # Address of new str object
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of tuple object b
b[2] = 19 # Error tuple is immutable so elements cannot be modified 
b = (30 , 40 , 35 , 32) 
print(id(b)) # Address of new tuple object b
c = range(5)
print(id(c)) # Address of range object c
c[3] = 10 # Range object is immutable so it cannot be modified 
c = range(5)
print(id(c)) # Address of new range object because it is immutable but cannot be reused

# Find  outputs  (Home  work)
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

#Find  outputs(Home  work)
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

# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [ 10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # ( 25 , 10.8 , 'Hyd' , 3+4j , True , None)
print({10 , 20} + {30 , 40}) # Error set cannot be added
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error dictionary does not have add operator
print(range(4) + range(5)) # Error because range is immutable
print(10 + '20') # Error the second operand should be non sequence
print([10 , 20 , 30] + 5) # Error a sequence cannot be added with a non sequence
print([10 , 20 , 30] + (40 , 50 , 60)) # Error two sequences of different classes cannot be added

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # -9+38j
print(3 + 4j * 5 + 6j) # 3+26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # ( 25 , 10.8 , 'Hyd' , True , 25 , 10.8 , 'Hyd' , True , 25 , 10.8 , 'Hyd' , True)
print([10 , 20 , 15] * 3.0) # Error because the non sequence should be integer
print({10 , 20 , 15} * 2) # Error set cannot be repeted it does not have duplicates
print({10 : 20 , 30 : 40} * 2) # Error dictionary cannot be repeated
print([10] * [20]) # Error the second operator should be an integer