#  Find  outputs
a = 25
print(id(a)) # address of object a, containing value 25
a = 35
print(id(a)) # address of object a, containing value 35


# Find  outputs (Home  work)
a = 25.7
print(id(a)) # address of object a, containing value 25.7
print(a)  # 25.7
a = 35.6
print(id(a)) # address of object a, containing value 35.6
print(a) # 35.6
b = True
print(id(b)) # address of object b, containing True
b = False
print(id(b)) # address of object b, containing False
c = None
print(id(c)) # address of object c
c = None
print(id(c)) # we get same address



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of object a, containing 'Hyd'
a[1] = 'e'  # str does not support item assignment 
a = 'Sec'
print(id(a)) # address of object a, containing 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b)) # address of object b 
b[2] = 19  # tuple does not support item assignment
b = (30 , 40 , 35 , 32)
print(id(b)) # address of object b
c = range(5)
print(id(c)) # address of object c
c[3] = 10 # range does not support item assignment
c = range(5)
print(id(c)) # address of object c


a = 25
b = 25
print(a  is  b) # True, both the references pointing to same object
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True, both the references pointing to same object
e = False
f = False
print(e  is  f) # True, both the references pointing to same object
g = range(10)
h = range(10)
print(g  is  h) # False, range is not reusable


a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False, lists are not reusable 
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False, dictionaries are not reusable 
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True, tuples are resuable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # false, sets are not reusable


print(10 + 20) # 30
print(10.8 + 20.6) # 30.4
print(3 + 4j + 5 + 6j) # 8 + 10j
print(True + False) # 1
print('Hyder' + 'abad') # hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40}) # Error
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error
print(range(4) + range(5)) # Error
print(10 + '20') # Error
print([10 , 20 , 30] + 5) # Error
print([10 , 20 , 30] + (40 , 50 , 60)) # error, cannot concatenate list and tuple


print(25 * 3)  # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error, second operand cannot be float
print({10 , 20 , 15} * 2) # Error, set cannot be repeated
print({10 : 20 , 30 : 40} * 2) # Error, dictionaries cannot be repeated
print([10] * [20]) # Error







