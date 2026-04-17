#  Find  outputs
a = 25 
print(id(a))   # address of the int object
a = 35        # here reference has changed
print(id(a))    # address of the int object


# Find  outputs (Home  work)
a = 25.7    #  a pointing to float object
print(id(a))  # address of the float object
print(a)    # 25.7
a = 35.6    #  reference has changed
print(id(a))  # address of the float object
print(a)     # 35.6
b = True
print(id(b)) # address of the bool object
b = False     # reference has changed
print(id(b))  #  address of the bool object
c = None    # 
print(id(c))   # address of the none object
c = None      # reference has changed
print(id(c))   # same address as above None


 #  Find  outputs  (Home  work)
a = 'Hyd'    #  a is pointing to string  object
print(id(a))   # address of the str object
a[1] = 'e'     # Errror 
a = 'Sec'    # a is assigning with new string object
print(id(a))   # address of the str object
b = (10 , 20 , 15 , 18)    #  b is assigning with tuple object
print(id(b))  # address of the tuple object
b[2] = 19   # Error because tuple is immutable
b = (30 , 40 , 35 , 32)   # b is assigning with new tuple object
print(id(b))  # address of the tuple object
c = range(5)  #  here range from 0 to 4 
print(id(c))  # address of the range object
c[3] = 10  # we can't change range object because it is immutable
c = range(5)   # same range as above c 
print(id(c))  # Address will be changed.

 # Find  outputs  (Home  work)
a = 25    # a is referencing int object 25
b = 25    # a is referencing int object 25
print(a  is  b) True because a and b are pointing to the same int object 25
c = 'Hyd'    # c is referencing str object 'Hyd'
d = 'Hyd'     # d is referencing str object 'Hyd'
print(c  is  d)   #  True they both pointing to the same str object
e = False    # e is referencing bool object 25
f = False    # f is referencing bool object 25
print(e  is  f)   # True because the both e and f pointing to the same bool object
g = range(10)   # g is referencing range object 
h = range(10)    # h is referencing new range object
print(g  is  h)   # False it has same range 0 to 4 but address will be changed.


 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]  
b = [10 , 20 , 15 , 18]
print(a  is  b)           #   False  because a and b will not have the same address
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)          # False because dictionary always creates new address 
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)            # False because tuple address also changes 
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)            # False set don't have same address at all.


 # Find outputs (Home work)
print(10 + 20)    #   30
print(10.8 + 20.6)    # 31.4
print(3 + 4j + 5 + 6j)  # 7+10j
print(True + False)     # 1
print('Hyder' + 'abad')   # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')  # 'SankarDayalSarma
print('10' + '20')    # 1020
print([10 , 20 , 30] + [1 , 2 , 3])   # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   #  (25 , 10.8 , 'Hyd',(3 + 4j) , True , None)
print({10 , 20} + {30 , 40})     #  Error set don't have + operator
print({10 : 'Hyd'} + {20 : 'Sec'})    # Error
print(range(4) + range(5))   # error  can't add range object
print(10 + '20')       # Error 
print([10 , 20 , 30] + 5)      # Error list is not permitted to perform operations when 2nd object is int
print([10 , 20 , 30] + (40 , 50 , 60))    # Error list and tuple can't perform any operations


 # Find outputs (Home work)
print(25 * 3)    # 75
print(10.8 * 25.6)   # 276.48
print(True * False)   # 0  
print((3 + 4j) * (5 + 6j))   # (15 + 18j + 20j + 24j**2) = 15 + 38j + 24(-1)  = (-9 + 38j)
print(3 + 4j * 5 + 6j)  # ( 3 + 20j + 6j) == (3 + 26j)
print('25' * 3)    # 252525
print(3 * '25')   # 252525
print('Hyd' * 4)   #  ('HydHydHydHyd')
print([10 , 20 , 15] * 2)   # 
print((25, 10.8, 'Hyd', True) * 3)   # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)   # Error because 2nd operand should always int
print({10 , 20 , 15} * 2)    # Error 
print({10 : 20 , 30 : 40} * 2)
print([10] * [20])   #  Error if 1st operant is sequence 2nd must be a int