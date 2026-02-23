#  Find  outputs
a = 25
print(id(a)) # 133230868727240
a = 35
print(id(a)) # 133230868727560

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # 1405123456771232
print(a) # 25.7
a = 35.6
print(id(a)) # 135221659011216
print(a) # 35.6
b = True
print(id(b)) #136246993061312
b = False
print(id(b)) # 136246993060864
c = None
print(id(c)) #136246993026144
c = None
print(id(c)) #136246993026144

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # 134233175710704
a[1] = 'e'   # error
a = 'Sec'
print(id(a)) #135581447477968
b = (10 , 20 , 15 , 18)
print(id(b)) # 132893818127760
b[2] = 19 # error
b = (30 , 40 , 35 , 32)
print(id(b))  #138972020245904
c = range(5)
print(id(c)) # 139693304601440
c[3] = 10 # error
c = range(5)
print(id(c)) # 140003334806368

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

# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3])  # [10 ,20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', 3+4j, True, None)
print({10 , 20} + {30 , 40}) # error
print({10 : 'Hyd'} + {20 : 'Sec'})  # error
print(range(4) + range(5)) # error
print(10 + '20') # error
print([10 , 20 , 30] + 5) # error
print([10 , 20 , 30] + (40 , 50 , 60)) # error

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHyd
print([10 , 20 , 15] * 2) #[10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) #25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True
print([10 , 20 , 15] * 3.0) # error
print({10 , 20 , 15} * 2) # error
print({10 : 20 , 30 : 40} * 2) # error
print([10] * [20]) # error