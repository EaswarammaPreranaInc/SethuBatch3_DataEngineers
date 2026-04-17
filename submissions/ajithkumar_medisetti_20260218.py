#  Find  outputs
a = 25
print(id(a)) # Address Of The Object 25 Ex: 100002
a = 35
print(id(a)) # Address Of The Object 35 Ex: 100023


# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address Of The Object 25.7 Ex:1900002
print(a) # 25.7
a = 35.6
print(id(a)) # Address Of The Object 35.6 Ex: 2091228
print(a) # 35.6
b = True
print(id(b)) # Same Address
b = False
print(id(b)) # Same Address
c = None
print(id(c)) # Same Address 
c = None
print(id(c)) # Identical Address
 

#Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # Address Of Object Hyd Ex: 2009930
a[1] = 'e'   # Error String Is Immutable
a = 'Sec' 
print(id(a)) # Address Of Object Sec Ex: 18975600
b = (10 , 20 , 15 , 18)
print(id(b)) # Address Of Object Tuple Ex:2879900
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b)) # # New Address Of The Object Tuple Ex: 246789000
c = range(5)
print(id(c)) # Address OF the Range Object Ex: 2879000
c[3] = 10
c = range(5)
print(id(c)) # New Address Of the Range Object Ex: 1380029



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
print(a  is  b)          # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)          # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)          # False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)          # False



# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) #  (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40}) # Error
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error
print(range(4) + range(5)) # 	Error
print(10 + '20') # Error
print([10 , 20 , 30] + 5) # Error
print([10 , 20 , 30] + (40 , 50 , 60)) # Error




# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j) 
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error Because Cannot multiply because its a float 
print({10 , 20 , 15} * 2) # Error Because Cannot Multiply In Set and int
print({10 : 20 , 30 : 40} * 2) # Error because Cannot Multiply dict and int
print([10] * [20]) # Error 