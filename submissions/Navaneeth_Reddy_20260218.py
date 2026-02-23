#  Find  outputs
a = 25
print(id(a)) # Address of the reference 'a' of object 25
a = 35
print(id(a)) # New address of the reference 'a' of object 25

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of the reference 'a' of object 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # New address of the reference 'a' of object 35.6
print(a) # 35.6
b = True
print(id(b)) # Address of the reference 'a' of object True
b = False
print(id(b)) # New address of the reference 'a' of object False
c = None
print(id(c)) # Address of the reference 'c'
c = None
print(id(c)) # Same address of reference 'c'

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # Some address of 'a'
a[1] = 'e'  # Error, because str is immutable
a = 'Sec'
print(id(a)) # New address of reference 'a' 
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of reference 'b' pointing the tuple
b[2] = 19 # Error, tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) # Now new address is assigned to reference 'b'
c = range(5)
print(id(c)) # address of reference 'c' 
c[3] = 10 # Error, range object is immutable and it does not have indexing
c = range(5)
print(id(c)) # New address for 'c' , as range object is not re-usable .


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True, as two references are pointing same int object
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True, as two references are pointing same str object
e = False
f = False
print(e  is  f) # True, as two references are pointing same bool object
g = range(10)
h = range(10)
print(g  is  h) # False, as they create separate range object, where it re-usablilty is not applied


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False , because Lists are mutable so it creates two different lists with different references 
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False , because dictionaries are mutable so it creates two different dictionaries with different references
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #  True because Tuples are immutable , so it will reuse the existing same object
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False , because sets are mutable so it creates two different sets with different references 



# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8 + 10j
print(True + False) # 1
print('Hyder' + 'abad') # 'Hyderabad , here '+' is concatenation
print('Sankar' + 'Dayal' + 'Sarma') # 'SankarDayalSarma , here '+' is concatenation
print('10' + '20') # '1020 , again concatenation
print([10 , 20 , 30] + [1 , 2 , 3]) # [10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd' , 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # Error, because sets can not be concatenated or added
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error because dictionaries can not be added or concatenated
print(range(4) + range(5)) # Error, range objects can not be added or concatenated
print(10 + '20') # Error, because 10 is non-sequence and '20' is sequence, this non-sequence and sequence objects can not be added or concatenated
print([10 , 20 , 30] + 5) # Error, because non-sequence and sequence can not be added or concatenated
print([10 , 20 , 30] + (40 , 50 , 60)) # Error, because same type non-sequences objecs can be concatenated


# Find outputs (Home work)
print(25 * 3) # 75, here it is multiplied
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3) # '252525' , here str is repeated
print(3 * '25') # '252525'
print('Hyd' * 4) # 'HydHydHydHyd'
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15] , here list is repeated
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True , 25, 10.8, 'Hyd', True) , here tuple is repeated
print([10 , 20 , 15] * 3.0) # Error, here sequence i.e list can not be multiplied to float, it can only multiplied to int
print({10 , 20 , 15} * 2) # Error, here sets can not be repeated, because it creates duplicate elements, where duplicates elements are not supported by sets
print({10 : 20 , 30 : 40} * 2) # Error, here dictionaries can not be repeated, because it creates duplicate keys, where duplicates keys are not supported by dictionaries
print([10] * [20]) # Error, because sequence can not be multiplied to other sequence, it can be only multiplied to int value