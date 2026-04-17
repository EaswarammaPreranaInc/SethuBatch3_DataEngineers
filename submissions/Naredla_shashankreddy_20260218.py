#  Find  outputs
a = 25
print(id(a)) # 1000 address of object 
a = 35
print(id(a)) #2000 now a refers to object 35 

# Find  outputs (Home  work)
a = 25.7
print(id(a)) #1000 adress of object 25
print(a) #25
a = 35.6
print(id(a)) #2000 a refers to object 35.6 so address changes 
print(a) #35.6
b = True
print(id(b)) #1002
b = False 
print(id(b)) #1004 b refers to object False so address changes
c = None
print(id(c)) #3000
c = None
print(id(c)) #3000


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #1000 adress of object Hyd
a[1] = 'e'   #error 
a = 'Sec'
print(id(a)) #2000 a refers to object sec 
b = (10 , 20 , 15 , 18)
print(id(b)) #1002 address of tuple object
b[2] = 19 #error tuple is immutable
b = (30 , 40 , 35 , 32) 
print(id(b)) #1004 now b refers to other object
c = range(5)
print(id(c)) #1000 address of object c
c[3] = 10 #range is immutable
c = range(5) 
print(id(c)) #2000 c refers to other object


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True a,b refers to same object is operator checks reference 
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True
e = False
f = False
print(e  is  f) #True
g = range(10)
h = range(10)
print(g  is  h) #False g,h refers to different objects even if the elements are same 


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False a,b do not refer to same object even if the elements are same since list is immutable 
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False c,d do not refer to same object even if the elements are same since dict is immutable 
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #True  e,f refers to same object 
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #False g,h do not refer to same object even if the elements are same since set is immutable 

# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j)#8+10j
print(True + False) #1
print('Hyder' + 'abad') #'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') #'SankarDayalSarma'
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,2,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})#error sets cannot be concatenated
print({10 : 'Hyd'} + {20 : 'Sec'})#error cannot be concatenated
print(range(4) + range(5))#error range cannot be concatenated
print(10 + '20')#error int and string cannot be concatenated
print([10 , 20 , 30] + 5)#error int and list cannot be concatenated
print([10 , 20 , 30] + (40 , 50 , 60))#error tuple and list cannot be concatenated

# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3)#252525
print(3 * '25')#2525252
print('Hyd' * 4)#HydHydHyd
print([10 , 20 , 15] * 2)[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) #Error tuple cannot does not support repetition 
print([10 , 20 , 15] * 3.0) #Error repetition doesn't allow float 
print({10 , 20 , 15} * 2) #Error set doesn't support repetition