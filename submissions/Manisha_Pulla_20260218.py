#  Find  outputs
a = 25
print(id(a)) #Output:Address of an object
a = 35
print(id(a)) #Output: Address of an object
# Find  outputs (Home  work)
a = 25.7
print(id(a)) #Output:Address of an object
print(a) #Output: 25.7
a = 35.6
print(id(a)) #Output: Address of an object
print(a) #Output:35.6
b = True
print(id(b)) #Output: Address of an object
b = False
print(id(b)) #Output: Address of an object
c = None
print(id(c)) #Output:Address of an object
c = None
print(id(c)) #Output: Address of an object
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #Output: Address of an object
a[1] = 'e'   
a = 'Sec'
print(id(a)) #Output: Address of an object
b = (10 , 20 , 15 , 18)
print(id(b)) #Output: Address of an object
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b)) #Output: Address of an object
c = range(5)
print(id(c)) #Output: Address of an object
c[3] = 10
c = range(5)
print(id(c)) #Output: Address of an object
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #Output: True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #Output:True
e = False
f = False
print(e  is  f) #Output:True
g = range(10)
h = range(10)
print(g  is  h) #Output: False
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #Output: False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #Output: False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #Output: False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #Output: True
# Find outputs (Home work)
print(10 + 20) #Output: 30
print(10.8 + 20.6) #Output: 31.400000002
print(3 + 4j + 5 + 6j) #Output:(8+10j)
print(True + False) #Output:1
print('Hyder' + 'abad') #Output: Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #Output: Sankar Dayal Sarma
print('10' + '20') #Output:1020
print([10 , 20 , 30] + [1 , 2 , 3]) #Output: [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #Output: (25,10.8,'Hyd',(3+4j),True,None)
print({10 , 20} + {30 , 40}) #Output:(10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'}) #Output: Error
print(range(4) + range(5)) #Output:Error
print(10 + '20') #Output:Error
print([10 , 20 , 30] + 5) #Output: Error
print([10 , 20 , 30] + (40 , 50 , 60)) #Output:Error
# Find outputs (Home work)
print(25 * 3) #Output: 75
print(10.8 * 25.6) #Output: 
print(True * False) #Output: 0
print((3 + 4j) * (5 + 6j)) #Output:(-9+38j)
print(3 + 4j * 5 + 6j) #Output:(3+26j)
print('25' * 3) #Output:252525
print(3 * '25') #Output:252525
print('Hyd' * 4) #Output: HydHydHydHyd
print([10 , 20 , 15] * 2) #Output:[10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #Output: (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) #Output: Error
print({10 , 20 , 15} * 2) #Output: Error
print({10 : 20 , 30 : 40} * 2) #Output:Error
print([10] * [20]) #Output: Error