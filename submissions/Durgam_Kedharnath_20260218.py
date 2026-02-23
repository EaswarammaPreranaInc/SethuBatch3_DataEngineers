

#  Find  outputs
a = 25
print(id(a)) # Address of the object 25
a = 35
print(id(a)) #Address of the object 35
# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of the object 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # Address of the object 35.6
print(a) # 35.6
b = True
print(id(b)) # Address of the object True
b = False
print(id(b)) # Address of the object False
c = None
print(id(c)) # Address of the None object
c = None
print(id(c)) # Address of the Same object None
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # Address of the str object
a[1] = 'e' # Error str is immutable
a = 'Sec'
print(id(a)) # Address of the object Sec
b = (10 , 20 , 15 , 18)
print(id(b))# Address of the tuple object
b[2] = 19 # Error tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) # Address of the object new tuple
c = range(5)
print(id(c)) # Address of the range object
c[3] = 10 # Error range object can't be modified
c = range(5)
print(id(c)) # Address of the new range object
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
print('10' + '20') # 30
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25,10.8,'Hyd',(3+4j),True, None)
print({10 , 20} + {30 , 40}) # Error set cannot perform concat
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error dict cannt perform concat
print(range(4) + range(5)) # Error range operation cannot perform concat
print(10 + '20') # Error str and int cannot be concat
print([10 , 20 , 30] + 5) # Error list and int cannot perform concat 
print([10 , 20 , 30] + (40 , 50 , 60)) # Error list and tuple cannot concat

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # 15+2 0j
print(3 + 4j * 5 + 6j) # 15+20j
print('25' * 3) # 252525
print(3 * '25') #252525
print('Hyd' * 4) # 'HydHydHydHyd'
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 15, 20]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error cannot multiply list with float
print({10 , 20 , 15} * 2) # Error set cannot perform multiply operation
print({10 : 20 , 30 : 40} * 2) # Error dict cannot perform multiply operation
print([10] * [20]) #Error  cannot multiply list with list