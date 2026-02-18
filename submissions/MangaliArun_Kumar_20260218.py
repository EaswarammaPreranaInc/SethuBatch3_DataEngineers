#  Find  outputs
a = 25
print(id(a)) # Address of obejct 25
a = 35
print(id(a)) # Address of obejct 35

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of obejct 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # Address of obejct 35.6
print(a) # 35.6
b = True
print(id(b)) # Address of obejct True
b = False
print(id(b)) # Address of obejct False
c = None
print(id(c)) # Address of obejct None
c = None
print(id(c)) # same

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # Address of obejct Hyd
a[1] = 'e'   # error bcz str is immutable
a = 'Sec'
print(id(a)) # Address of obejct Sec
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of obejct b
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b)) # Address of obejct b after change
c = range(5)
print(id(c)) # Address of obejct c
c[3] = 10
c = range(5)
print(id(c)) # Address of obejct c after change

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
print(g  is  h) # True

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # True
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  # Error
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  # Error

# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 7 + 10j
print(True + False) # False
print('Hyder' + 'abad') # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') # 'SankarDayalSarma'
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25,10,8,'Hyd',3+4j,True,None)
print({10 , 20} + {30 , 40}) # Error bcz dict is immutable
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error bcz dict is immutable
print(range(4) + range(5)) #(0,1,2,3,0,1,2,3,4)
print(10 + '20') # Error bcz sequence and non-sequence cannot concatinate
print([10 , 20 , 30] + 5) # Error bcz sequence and non-sequence cannot concatinate
print([10 , 20 , 30] + (40 , 50 , 60)) #Error bcz mutable and unmutable cannot concatinate

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # varies
print(True * False) # False
print((3 + 4j) * (5 + 6j)) #error 
print(3 + 4j * 5 + 6j) #error
print('25' * 3) # 252525
print(3 * '25') #252525
print('Hyd' * 4) #HydHydHydHyd
print([10 , 20 , 15] * 2) # [10,20,15][10,20,15]
print((25, 10.8, 'Hyd', True) *3) # (25, 10.8, 'Hyd', True)(25, 10.8, 'Hyd', True)(25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # error
print({10 , 20 , 15} * 2) #error
print({10 : 20 , 30 : 40} * 2) #error
print([10] * [20]) # error