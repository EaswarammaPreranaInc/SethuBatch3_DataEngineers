#  Find  outputs
a = 25
print(id(a)) #Address of object a 
a = 35
print(id(a)) #Address of object a


# Find  outputs (Home  work)
a = 25.7
print(id(a)) #Address of float object 25.7
print(a) #25.7
a = 35.6
print(id(a)) #Address of float object 35.6
print(a) #35.6
b = True
print(id(b)) #Address of bool object True
b = False
print(id(b)) #Address of bool object False 
c = None
print(id(c)) #Address of object c


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #Address of object a
a[1] = 'e'   
a = 'Sec'
print(id(a)) #Address of object Sec
b = (10 , 20 , 15 , 18)
print(id(b)) #Address of list b
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b)) #Address of list b[New Address]
c = range(5) #(0,1,2,3,4)
print(id(c)) #Address of range object
c[3] = 10 #invalid range is immutable it cannot be reusable
c = range(5) #(0,1,2,3,4)
print(id(c)) #Same Address



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
print(g  is  h) #True



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False because different objects and list is mutable and cannot be reusable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False because Dictionary is mutable and cannot be reusable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #True because Tuple is immutable and it can be reusable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #False because set is mutable and it  cannot be reusable


# Find outputs (Home work)
print(10 + 20) #30 Here Addition is performed between two Non-sequences
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #(8+10j)
print(True + False) #1
print('Hyder' + 'abad') #Hyderabad here Concatenation is performed between two strings
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma  Concatenation is performed
print('10' + '20') #1020 here also concatenation is performed between two strings
print([10 , 20 , 30] + [1 , 2 , 3]) #[10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd' , 3+4j , True , None)
print({10 , 20} + {30 , 40}) #Type Error because sets doesn't support +
print({10 : 'Hyd'} + {20 : 'Sec'}) #Type Error because dicts doesn't support +
print(range(4) + range(5))  #Type Error because range doesn't support +
print(10 + '20') # Type Error because int+str
print([10 , 20 , 30] + 5) #Type Error because list + int
print([10 , 20 , 30] + (40 , 50 , 60)) #Type Error because list + tuple


# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #-9+8j
print(3 + 4j * 5 + 6j) #3+26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) #HydHydHydHyd
print([10 , 20 , 15] * 2) #[10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #(25 , 10.8 , 'Hyd' , True , 25 , 10.8 , 'Hyd' , True , 25 , 10.8 , 'Hyd' , True)
print([10 , 20 , 15] * 3.0) # Type Error because it is multiplied by float i.e;it should be int
print({10 , 20 , 15} * 2) #Type Error because sets doesn't allows duplicates
print({10 : 20 , 30 : 40} * 2) # Type Error because Dictionary doesn't allows duplicates and Repetition
print([10] * [20]) # Type Error because list is a sequence * operator doesn't supports