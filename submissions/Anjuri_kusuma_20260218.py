#  Find  outputs
a = 25
print(id(a))  #some address of obj
a = 35
print(id(a))  #some other address of abj


# Find  outputs (Home  work)
a = 25.7
print(id(a))  #add 1
print(a)  #25.7
a = 35.6
print(id(a))  #add2
print(a)  #35.6
b = True
print(id(b))  #add3
b = False
print(id(b))   #add4
c = None
print(id(c))  #add5
c = None
print(id(c))   #add5


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  #add1 of obj
a[1] = 'e'  #invalid because strings are immutable  
a = 'Sec'
print(id(a))  #add2 
b = (10 , 20 , 15 , 18)
print(id(b))  #add3
b[2] = 19  #invalid because tuple is immutable
b = (30 , 40 , 35 , 32)  
print(id(b))  #add4
c = range(5)
print(id(c))  #add5
c[3] = 10   #not valid
c = range(5)  
print(id(c))  #add6


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)  #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  #True
e = False
f = False
print(e  is  f)  #True
g = range(10)
h = range(10)
print(g  is  h)  #False because range is not reusable so it creates new object


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)   #False bcause list is mutable cannot be reused
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)   #False bcause dict is mutable cannot be reused
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)   #True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  #False bcause set is mutable cannot be reused


# Find outputs (Home work)
print(10 + 20)  #30
print(10.8 + 20.6)  #31.4
print(3 + 4j + 5 + 6j)  #8+10j
print(True + False)  #1
print('Hyder' + 'abad')  #'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')  #'SankarDayalSarma
print('10' + '20')  #'1020'
print([10 , 20 , 30] + [1 , 2 , 3])  #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  #(25 , 10.8 , 'Hyd', 3 + 4j , True , None)
print({10 , 20} + {30 , 40})  #not valid
print({10 : 'Hyd'} + {20 : 'Sec'})  #not valid
print(range(4) + range(5))  #not valid
print(10 + '20')  #not valid
print([10 , 20 , 30] + 5)  #not valid
print([10 , 20 , 30] + (40 , 50 , 60))   #not valid


# Find outputs (Home work)
print(25 * 3)  #75
print(10.8 * 25.6)  #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j))  #
print(3 + 4j * 5 + 6j)
print('25' * 3)  #'252525'
print(3 * '25')  #'252525' 
print('Hyd' * 4)  #'HydHydHydHyd'
print([10 , 20 , 15] * 2)  #[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)  #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)   #invalid it should be integer not float
print({10 , 20 , 15} * 2)   #invalid cannot be repeated
print({10 : 20 , 30 : 40} * 2)  #invalid cannot be repeated
print([10] * [20])  #invalid 


