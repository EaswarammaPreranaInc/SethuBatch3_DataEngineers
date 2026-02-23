#  Find  outputs
a = 25
print(id(a)) # address of int object a
a = 35
print(id(a)) # address of new int object a

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # address of float object a
print(a) # 25.7
a = 35.6 
print(id(a)) # address of new float object a
print(a) # 35.6
b = True
print(id(b)) # address of bool object b
b = False
print(id(b)) # address of new bool object b
c = None
print(id(c)) # address of NoneType object c
c = None
print(id(c)) # address of same NoneType object c

# Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of str object a
a[1] = 'e'   # ERROR because str is immutable and can't insert  
a = 'Sec'
print(id(a)) # address of new str object a
b = (10 , 20 , 15 , 18)
print(id(b)) # address of Tuple object b
b[2] = 19 # ERROR because we can't insert in tuple
b = (30 , 40 , 35 , 32)
print(id(b)) # address of new Tuple object b
c = range(5)
print(id(c)) # address of range object c
c[3] = 10 # ERROR because range is immutable and can't be modified
c = range(5)
print(id(c)) #address of new range object c

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
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # ERROR because set can't be added it causes duplicates
print({10 : 'Hyd'} + {20 : 'Sec'}) # ERROR because dict can't be added it causes duplicates
print(range(4) + range(5)) #  ERROR because range can't be added it causes duplicates
print(10 + '20') # ERROR because in addition argments should be either both sequences or both non-sequences
print([10 , 20 , 30] + 5) # ERROR because in addition argments should be either both sequences or both non-sequences
print([10 , 20 , 30] + (40 , 50 , 60)) # ERROR because list is mutable and tuple is immutable not so not defined to addition


 # Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # 15+18j+20j-24=-9+38j
print(3 + 4j * 5 + 6j) #3+26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) #HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # ERROR 2nd arg shouldn't be int object
print({10 , 20 , 15} * 2) # ERROR no repetation allowed
print({10 : 20 , 30 : 40} * 2) # ERROR no repetation allowed
print([10] * [20]) # ERROR 2nd arg should be int object and list can't be multiplied with list