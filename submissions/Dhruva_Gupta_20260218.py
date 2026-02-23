Name-Dhruva Gupta			Subject-Python			Date-18/2/2026

1)
#  Find  outputs
a = 25
print(id(a)) #address of object 
a = 35
print(id(a)) #address of object different from the above one

2)
# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #complex output=-9+38j
print(3 + 4j * 5 + 6j)  #3+26j
print('25' * 3) #252525
print(3 * '25') #252525
print('Hyd' * 4) #HydHydHydHyd 
print([10 , 20 , 15] * 2)  #list printed twice
print((25, 10.8, 'Hyd', True) * 3) #tuple repeated thrice
print([10 , 20 , 15] * 3.0) #list won’t be multiples with float
print({10 , 20 , 15} * 2) #sets does not have duplicate 
print({10 : 20 , 30 : 40} * 2) #dict also no duplicates
print([10] * [20]) #list can only be multiplied with integer

3)
# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) #1
print('Hyder' + 'abad') #Hyderbad 
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalsarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #tuple immutable
print({10 , 20} + {30 , 40}) #sets cannot be multiplied or added to itself
print({10 : 'Hyd'} + {20 : ‘Sec’}) #dict cannot be multiplied or added to itself
print(range(4) + range(5)) #dict cannot be multiplied or added to itself
print(10 + '20') error
print([10 , 20 , 30] + 5) #list concatenation only possible to list
print([10 , 20 , 30] + (40 , 50 , 60)) #list concatenation only possible to list

4)
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False 
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #True as tuple can be reused
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #False

5)
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True 
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True 
e = False
f = False
print(e  is  f) #True
g = range(10)
h = range(10)
print(g  is  h) #False

6)
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #object id 
a[1] = 'e'   #String immutable 
a = 'Sec'
print(id(a)) #object id 
b = (10 , 20 , 15 , 18)
print(id(b)) #object id 
b[2] = 19 #tuple immutable 
b = (30 , 40 , 35 , 32)
print(id(b)) #object id 
c = range(5)
print(id(c)) #object id 
c[3] = 10 #range immutable 
c = range(5)
print(id(c)) #object id

7)
# Find  outputs (Home  work)
a = 25.7
print(id(a)) #object id 
print(a) #25.7
a = 35.6
print(id(a)) #object id
print(a) #35.6
b = True
print(id(b)) #object id
b = False
print(id(b)) #object id
c = None
print(id(c)) #object id 
c = None
print(id(c)) #object id