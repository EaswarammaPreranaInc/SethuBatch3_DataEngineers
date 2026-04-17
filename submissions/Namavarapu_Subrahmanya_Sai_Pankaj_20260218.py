a = 25
print(id(a))      # address of 25 with reference a
a = 35
print(id(a))      # address of 35 with reference a
a = 25.7
print(id(a))      # address 25.7 with reference a
print(a)          # 25.7

a = 35.6
print(id(a))      # address 35.6.7 with reference a
print(a)          # 35.6

b = True
print(id(b))      # address of True

b = False
print(id(b))      # adress of False

c = None
print(id(c))      # adress of None

c = None
print(id(c))      #  same address None

a = 'Hyd'
print(id(a))          # id5

#a[1] = 'e'            # Error string immutable

a = 'Sec'
print(id(a))          # new address of string object 

b = (10 , 20 , 15 , 18)
print(id(b))          # address of object tuple

#b[2] = 19             # Error tuple immutable

b = (30 , 40 , 35 , 32)
print(id(b))          # new address of tuple with reference b 

c = range(5)
print(id(c))          # address of object range

#c[3] = 10             # Error range immutable

c = range(5)
print(id(c))          # address  of new object

a = 25
b = 25
print(a is b) # True
c = 'Hyd'
d = 'Hyd'
print(c is d) # True
e = False
f = False
print(e is f) # True
g = range(10)
h = range(10)
print(g is h) # False
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a is b) # False
c = {10 : 20, 30 : 40}
d = {10 : 20, 30 : 40}
print(c is d) # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e is f) # True   (may be True due to optimization)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g is h) # False

print(10 + 20)# 30

print(10.8 + 20.6)# 31.4

print(3 + 4j + 5 + 6j)# (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3+4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
# print({10 , 20} + {30 , 40}) # TypeError

# print({10 : 'Hyd'} + {20 : 'Sec'}) # Error

# print(range(4) + range(5)) # Error

# print(10 + '20') # Error

# print([10 , 20 , 30] + 5) # Error

# print([10 , 20 , 30] + (40 , 50 , 60)) # Error

print(25 * 3)# 75

print(10.8 * 25.6)# 276.48

print(True * False)# 0

print((3 + 4j) * (5 + 6j))# (-9+38j)

print(3 + 4j * 5 + 6j)# (3+26j)
print('25' * 3)# 252525

print(3 * '25')# 252525

print('Hyd' * 4)# HydHydHydHyd
print([10 , 20 , 15] * 2)# [10, 20, 15, 10, 20, 15]

print((25,10.8,'Hyd',True) * 3)# (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
# print([10 , 20 , 15] * 3.0) # Error

# print({10 , 20 , 15} * 2) # Error

# print({10 : 20 , 30 : 40} * 2) # Error

# print([10] * [20]) # Error
