# Find outputs
a = 25   
print(id(a))   # address of object 25
a = 35
print(id(a))   # address of object 25 same as a

# Find outputs (Home work)
a = 25.7
print(id(a))   # address of object 25.7
print(a)  #25.7
a = 35.6
print(id(a))  #address of object 35.6
print(a)  # 35.6
b = True  
print(id(b))   #address of object True
b = False
print(id(b))   # address of object False   different address
c = None
print(id(c))    # address of object None
c = None
print(id(c))    # address of object None  same address

# Find outputs (Home work)
a = 'Hyd'
print(id(a))   # address of object 'Hyd'
a[1] = 'e' # error because string is not mutable  
a = 'Sec'     # a gets referred to  'sec' 
print(id(a)) # address of object 'sec'
b = (10 , 20 , 15 , 18)  
print(id(b))   # address of tuple 
b[2] = 19     # error because tuple is immutable
b = (30 , 40 , 35 , 32) 
print(id(b))   # address of new tuple
c = range(5)   # (0,1,2,3,4)
print(id(c))   # # address of object range
c[3] = 10      # error because range is not mutable
c = range(5)   
print(id(c))  #another address of the range object

# Find outputs (Home work)
a = 25
b = 25
print(a is b)  # True because a and b are both assigned to one int object   (can be reusable)
c = 'Hyd'
d = 'Hyd'
print(c is d)   # True because c and d are both assigned to one string i.e same string object (can be reusable)
e = False
f = False
print(e is f)  # True because e and f are both assigned to one bool object ( can be reusable)
g = range(10)
h = range(10)
print(g is h) # False  because g and h are range objects, they are not reusable

#Find outputs(Home work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a is b)    # False because lists a, b are not reusable
c = {10 : 20, 30 : 40}
d = {10 : 20, 30 : 40}
print(c is d)   # False because  dict c,d are not resuable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e is f)    # True because tuple is reusable , tuple is immutable
g = {10 , 20 , 15 , 18} 
h = {10 , 20 , 15 , 18}    
print(g is h)  # False because set is not resuable, set is mutable

# Find outputs (Home work)
print(10 + 20)   # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # 8 + 10j
print(True + False)     #1
print('Hyder' + 'abad')  # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')   # 'SankarDayalSarma'
print('10' + '20')  # '1020'
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40})  # {10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'})  # {10 : 'Hyd',20 : 'Sec'}
print(range(4) + range(5))  # error because range doesnt allow duplicates
print(10 + '20')  # error because seq and non seq cannot added 
print([10 , 20 , 30] + 5)   # error because seq and non seq cannot added 
print([10 , 20 , 30] + (40 , 50 , 60)) # [10,20,30,40,50,60]

# Find outputs (Home work)
print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # 15 + (-24)  == -9 +38j
print(3 + 4j * 5 + 6j)  # 3+26j
print('25' * 3)  # '252525'
print(3 * '25')  # '252525'
print('Hyd' * 4) # 'HydHydHydHyd'
print([10 , 20 , 15] * 2)  #[10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True ,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)   # error op2 must be int
print({10 , 20 , 15} * 2)   # error becuase set doesnt contain duplicates
print({10 : 20 , 30 : 40} * 2)  # error because dict doesnt contain dulicate keys
print([10] * [20])    #  error because seq and seq cannot be mutltiplied