# Find  outputs (Home  work)
a = 25.7
print(id(a))  # address of id
print(a)  # 25.7
a = 35.6  # 5001 (new value, new id)
print(id(a))    #  address of the id of the new value
print(a) # 35.6
b = True 
print(id(b)) # address of the id of the value True
b = False 
print(id(b)) # # address of the id of the value False
c = None
print(id(c))# address of the id of the value None
c = None
print(id(c))# address of the id of the value None




#  Find  outputs
a = 25
print(id(a))  # address of the id 
a = 35
print(id(a)) # address of the id of the new value



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of the id
a[1] = 'e'    # Error because str  value cannot be changed
a = 'Sec'  #  (new value, new id)
print(id(a))    # address of the id of the new value
b = (10 , 20 , 15 , 18)
print(id(b)) # address of the id of the tuple
b[2] = 19   # Error because tuple value cannot be changed
b = (30 , 40 , 35 , 32) 
print(id(b)) # address of the id of the new tuple
c = range(5) # 0,1,2,3,4
print(id(c)) # address of the id of the range obj
c[3] = 10  # Error because range obj does not support item assignment
c = range(5) # 0,1,2,3,4 (same value, same id)
print(id(c)) # address of the id of the new range obj





# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True because small integers are cached by Python and both a and b refer to the same obj in memory
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True because str  literals are also interned by Python and both c and d refer to the same obj in memory
e = False
f = False
print(e  is  f) # True because boolean values are also singleton objects in Python and both e and f refer to the same obj in memory
g = range(10)
h = range(10)
print(g  is  h) # False because range objects are not cached and g and h refer to different objects in memory




#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)          # False because lists are mutable and each list is a separate obj in memory, so a and b refer to different objects
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)          # False because dict  are mutable and each dictionary is a separate obj in memory, so c and d refer to different objects
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)         # True because tuples are immutable and Python may optimize memory usage by reusing the same obj for identical tuples, so e and f may refer to the same obj in memory
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)         # False because sets are mutable and each set is a separate obj in memory, so g and h refer to different objects






# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6)   # 31.4
print(3 + 4j + 5 + 6j)   # (8+10j)
print(True + False)   # 1 because True is treated as 1 and False is treated as 0 in arithmetic operations
print('Hyder' + 'abad')  # Hyderabad (str  concatenation)
print('Sankar' + 'Dayal' + 'Sarma')  # SankarDayalSarma (str  concatenation)
print('10' + '20')  # 1020 (str  concatenation)
print([10 , 20 , 30] + [1 , 2 , 3])  # [10, 20, 30, 1, 2, 3] (list concatenation)
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25, 10.8, 'Hyd', (3+4j), True, None) (tuple concatenation)
print({10 , 20} + {30 , 40})  # Error because sets do not support the + operator for concatenation
print({10 : 'Hyd'} + {20 : 'Sec'})  # Error because dict  do not support the + operator for concatenation
print(range(4) + range(5))  # Error because range objects do not support the + operator for concatenation
print(10 + '20') # Error because you cannot add an integer and a str  together
print([10 , 20 , 30] + 5)  # Error because you cannot add a list and an integer together
print([10 , 20 , 30] + (40 , 50 , 60)) # Error because you cannot add a list and a tuple together







# Find outputs (Home work)
print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0 because true is 1 and false is 0
print((3 + 4j) * (5 + 6j)) # multiplication of complex numbers
print(3 + 4j * 5 + 6j)  # multiplication of complex numbers
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4)  # HydHydHydHyd
print([10 , 20 , 15] * 2)  # [10, 20, 15, 10, 20, 15] 
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True) (tuple repetition)
print([10 , 20 , 15] * 3.0)  # Error because list cannot be multiplied by a float
print({10 , 20 , 15} * 2) # Error because set  does not support multiplication
print({10 : 20 , 30 : 40} * 2)  # Error because dict  does not support multiplication
print([10] * [20]) # Error because you cannot multiply a list by another list, only by an integer



