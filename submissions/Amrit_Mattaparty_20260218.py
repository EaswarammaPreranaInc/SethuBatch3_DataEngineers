#1
#  Find  outputs
a = 25
print(id(a)) #Some random address assigned to 'a' by the IDE or PVM
a = 35
print(id(a)) #Some random new address assigned to 'a' by the IDE or PVM



#2
# Find  outputs (Home  work)
a = 25.7
print(id(a)) #Some random address assigned to 'a' by the IDE or PVM
print(a) #25.7
a = 35.6
print(id(a)) #Some random new address assigned to 'a' by the IDE or PVM
print(a) #35.6
b = True
print(id(b)) #Some random address assigned to 'b' by the IDE or PVM
b = False
print(id(b)) #Some random new address assigned to 'b' by the IDE or PVM
c = None
print(id(c)) #Some random address assigned to 'c' by the IDE or PVM
c = None
print(id(c)) #Same random address assigned to 'c' by the IDE or PVM



#3
#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #Some random address assigned to 'a' by the IDE or PVM
a[1] = 'e' #Error as string doesn't support indexing 
a = 'Sec'
print(id(a)) #Some random new address assigned to 'a' by the IDE or PVM
b = (10 , 20 , 15 , 18)
print(id(b)) #Some random address assigned to 'b' by the IDE or PVM
b[2] = 19 #Error as tuple is immutable which doesn't support this type of random modification
b = (30 , 40 , 35 , 32)
print(id(b)) #Some random new address assigned to 'b' by the IDE or PVM
c = range(5)
print(id(c)) #Some random address assigned to 'c' by the IDE or PVM
c[3] = 10 #Error as range object which is immutable and which doesn't support random access or modification or it doesn't even have indexes
c = range(5)
print(id(c)) #Some random new address assigned to 'c' by the IDE or PVM i.e range object can't be re-used again unlike other immutable objects



#4
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True as in simple terms references as matching
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True as in simple terms references as matching
e = False
f = False
print(e  is  f) #True as in simple terms references as matching
g = range(10)
h = range(10)
print(g  is  h) #False because referneces are not matching due to non - reusability charactersistic of range object



#5
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False as lists are mutable which results in creating two different lists having different references
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False as dictionaries are mutable which results in creating two different disctionaries having different references
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #True as tuples are mutable which doesn't result in creation of new tuple with different references instead just reference is modified
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #False as sets are mutable which results in creating two different sets having different references



#6
# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) #1
print('Hyder' + 'abad') #Hyderabad i.e. concatenation 
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma i.e concatenation
print('10' + '20') #'1020' i.e concatenation
print([10 , 20 , 30] + [1 , 2 , 3]) #[10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd', 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) #Error as a sets can't be added to each other due to 
print({10 : 'Hyd'} + {20 : 'Sec'}) #Error as a dictionaries can't be added to each other due to
print(range(4) + range(5)) #Error as a range objects can't be added to each other due to
print(10 + '20') #Error as a sequence i.e. 10 and a non-sequence i.e. '20' can't be either added or concatenated to each other
print([10 , 20 , 30] + 5) #Error as a list can be only concatenated with a list but not with an integer object
print([10 , 20 , 30] + (40 , 50 , 60)) #Error as a list can be only concatenated with a list but with a tuple



#7
# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3) #'252525'
print(3 * '25') #'252525'
print('Hyd' * 4) #'HydHydHydHyd'
print([10 , 20 , 15] * 2) #[10 , 20 , 15, 10 , 20 , 15] i.e. repetetion of list
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True) i.e. repetetion of tuple
print([10 , 20 , 15] * 3.0) #Error as a sequence i.e. list can't be multiplied to a float object but can be multiplied to a integer object
print({10 , 20 , 15} * 2) #Error as sets can't be repeated as on repetetion which ensures occurence of duplicate values which is not permitted or ignored 
print({10 : 20 , 30 : 40} * 2) #Error as dictionaries can't be repeated as on repetetion which ensures occurence of duplicate keys which is not permitted 
print([10] * [20]) #Error as we can't multiply sequence by non-integer i.e list - in this case